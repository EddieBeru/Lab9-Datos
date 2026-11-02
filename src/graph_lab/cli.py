"""Interfaz de consola y conversión de errores esperados."""
import argparse
import json
import sys

from .reader import read_graph


def main(argv=None):
    parser = argparse.ArgumentParser(description='Grafos dirigidos desde CSV')
    commands = parser.add_subparsers(dest='command', required=True)
    for name, description in [('show', 'Mostrar vértices y aristas'),
                              ('sort', 'Obtener un orden topológico')]:
        command = commands.add_parser(name, help=description)
        command.add_argument('file', help='Archivo CSV source,target')
    args = parser.parse_args(argv)
    try:
        graph = read_graph(args.file)
        result = ({'order': graph.topological_order()} if args.command == 'sort'
                  else graph.as_dict())
    except (OSError, UnicodeError):
        print(f'Error: no se pudo leer {args.file}', file=sys.stderr)
        return 1
    except ValueError as exc:
        print(f'Error: {exc}', file=sys.stderr)
        return 1
    print(json.dumps(result, ensure_ascii=False))
    return 0
