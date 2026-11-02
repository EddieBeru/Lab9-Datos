"""Feature 2 AS-201–207, invariantes y oráculo independiente solo en tests."""
import csv
import io
import json
import random

import networkx as nx
import pytest

from test_show import ROOT, run

CYCLE_ERROR = 'Error: el grafo contiene un ciclo; no existe orden topológico\n'


def oracle(path):
    graph = nx.DiGraph()
    with path.open(encoding='utf-8-sig', newline='') as stream:
        rows = csv.reader(stream)
        next(rows)
        for row in rows:
            if not row:
                continue
            source, target = map(str.strip, row)
            graph.add_node(source)
            if target:
                graph.add_edge(source, target)
    return graph


def check_order(path):
    reference = oracle(path)
    result = run('sort', path)
    assert result.returncode == 0, result.stderr
    assert result.stderr == ''
    order = json.loads(result.stdout)['order']
    assert len(order) == len(set(order)) == len(reference)
    assert set(order) == set(reference)
    positions = {vertex: index for index, vertex in enumerate(order)}
    assert all(positions[u] < positions[v] for u, v in reference.edges)
    assert order == list(nx.lexicographical_topological_sort(reference))
    return order


@pytest.mark.parametrize('name', ['small-dag', 'cs-curriculum'])
def test_AS201_AS202_original_dags(name):
    check_order(ROOT / f'data/{name}.csv')


@pytest.mark.parametrize('content', ['source,target\n',
    'source,target\na,b\nx,y\nwatch,\n', 'source,target\na,b\na,b\n'])
def test_AS203_empty_disconnected_duplicate(tmp_path, content):
    path = tmp_path / 'g.csv'
    path.write_text(content)
    check_order(path)


def test_AS204_original_cycle():
    path = ROOT / 'data/build-with-cycle.csv'
    assert not nx.is_directed_acyclic_graph(oracle(path))
    result = run('sort', path)
    assert result.returncode == 1 and not result.stdout
    assert result.stderr == CYCLE_ERROR


@pytest.mark.parametrize('content', ['a,b\nb,a\n', 'metrics,metrics\n',
    'a,b\nb,a\nx,y\n', 'a,b\nb,c\nc,a\n'])
def test_AS205_cycles_no_partial(tmp_path, content):
    path = tmp_path / 'g.csv'
    path.write_text('source,target\n' + content)
    assert not nx.is_directed_acyclic_graph(oracle(path))
    result = run('sort', path)
    assert result.returncode == 1 and not result.stdout
    assert result.stderr == CYCLE_ERROR


def test_AS206_errors_help_regression(tmp_path):
    missing = run('sort', tmp_path / 'missing.csv')
    assert missing.returncode == 1 and not missing.stdout
    assert missing.stderr.startswith('Error: no se pudo leer ')
    invalid = tmp_path / 'bad.csv'
    invalid.write_text('source,target\n,b\n')
    result = run('sort', invalid)
    assert result.returncode == 1 and not result.stdout
    assert result.stderr.startswith('Error: línea 2:')
    usage = run('sort')
    assert usage.returncode == 2 and not usage.stdout
    help_result = run('sort', '--help')
    assert help_result.returncode == 0 and not help_result.stderr
    shown = run('show', ROOT / 'data/build-with-cycle.csv')
    assert shown.returncode == 0 and not shown.stderr


def test_AS207_deterministic_permuted(tmp_path):
    path = tmp_path / 'g.csv'
    for content in ['b,c\na,c\n', 'a,c\nb,c\n']:
        path.write_text('source,target\n' + content)
        assert check_order(path) == ['a', 'b', 'c']
        assert check_order(path) == ['a', 'b', 'c']


def test_oracle_generated_dags(tmp_path):
    rng = random.Random(402)
    path = tmp_path / 'g.csv'
    for _ in range(10):
        nodes = list('abcdef')
        rng.shuffle(nodes)
        output = io.StringIO()
        writer = csv.writer(output)
        writer.writerow(['source', 'target'])
        for vertex in nodes:
            writer.writerow([vertex, ''])
        for i, u in enumerate(nodes):
            for v in nodes[i + 1:]:
                if rng.random() < .4:
                    writer.writerow([u, v])
        path.write_text(output.getvalue())
        check_order(path)


def test_graph_not_mutated():
    from graph_lab.reader import read_graph
    graph = read_graph(ROOT / 'data/small-dag.csv')
    before = graph.as_dict()
    assert graph.topological_order() == graph.topological_order()
    assert graph.as_dict() == before
