"""AS-301–306: Dijkstra propre, oráculo y contrato de consola."""
import csv
import json
import random

import networkx as nx
import pytest

from test_show import ROOT, run


def check(path, source):
    result = run('shortest', path, source)
    assert result.returncode == 0, result.stderr
    assert not result.stderr
    data = json.loads(result.stdout)
    reference = nx.DiGraph()
    with path.open(encoding='utf-8-sig', newline='') as stream:
        rows = csv.reader(stream)
        next(rows)
        for row in rows:
            if not row:
                continue
            u, v, weight = (value.strip() for value in row)
            reference.add_node(u)
            if v:
                w = int(weight)
                old = reference.get_edge_data(u, v)
                reference.add_edge(u, v, weight=min(w, old['weight']) if old else w)
    expected = nx.single_source_dijkstra_path_length(reference, source)
    assert list(data['distances']) == sorted(reference)
    assert list(data['paths']) == sorted(reference)
    assert data['distances'] == {v: expected.get(v) for v in sorted(reference)}
    for target, distance in data['distances'].items():
        path = data['paths'][target]
        if distance is None:
            assert path is None
        else:
            assert path[0] == source and path[-1] == target
            assert len(path) == len(set(path))
            assert sum(reference[u][v]['weight'] for u, v in zip(path, path[1:])) == distance
    return data


def test_AS301_AS303_fixture():
    data = check(ROOT / 'tests/data/weighted.csv', 'a')
    assert data['distances'] == {'a': 0, 'b': 3, 'c': 1, 'z': None}
    assert data['paths']['b'] == ['a', 'c', 'b']
    assert data['paths']['a'] == ['a']


def test_AS302_zero_ties_cycles(tmp_path):
    path = tmp_path / 'g.csv'
    path.write_text('source,target,weight\na,b,0\nb,a,0\na,a,0\na,c,2\nb,c,2\nz,,\n')
    check(path, 'a')


@pytest.mark.parametrize('row', ['a,b,-1', 'a,b,', 'a,b,1.5', 'a,b,NaN',
    'a,b,inf', 'a,b,+1', ',b,1', 'a,,2', 'a,b', 'a,b,2,3', '"unclosed,b,1'])
def test_AS304_invalid_rows(tmp_path, row):
    path = tmp_path / 'bad.csv'
    path.write_text('source,target,weight\na,b,2\n' + row + '\n')
    result = run('shortest', path, 'a')
    assert result.returncode == 1 and not result.stdout
    assert result.stderr.startswith('Error: línea ')
    assert 'Traceback' not in result.stderr


@pytest.mark.parametrize('content', [b'', b'source,target\na,b\n', b'wrong\n',
    b'source,target,weight\na,b,\xff\n'])
def test_AS304_header_encoding(tmp_path, content):
    path = tmp_path / 'bad.csv'
    path.write_bytes(content)
    result = run('shortest', path, 'a')
    assert result.returncode == 1 and not result.stdout
    assert result.stderr.startswith('Error:') and 'Traceback' not in result.stderr


def test_AS305_missing_source_empty_usage(tmp_path):
    path = tmp_path / 'empty.csv'
    path.write_text('source,target,weight\n')
    for file in [path, ROOT / 'tests/data/weighted.csv']:
        result = run('shortest', file, 'missing')
        assert result.returncode == 1 and not result.stdout
        assert result.stderr == 'Error: origen inexistente: missing\n'
    missing = run('shortest', tmp_path / 'missing', 'a')
    assert missing.returncode == 1 and not missing.stdout
    assert missing.stderr.startswith('Error: no se pudo leer ')
    assert run('shortest', path).returncode == 2
    help_result = run('shortest', '--help')
    assert help_result.returncode == 0 and not help_result.stderr


def test_AS306_original_contracts():
    for name in ['small-dag', 'cs-curriculum', 'build-with-cycle']:
        path = ROOT / f'data/{name}.csv'
        assert run('show', path).returncode == 0
        assert run('sort', path).returncode == (1 if name == 'build-with-cycle' else 0)
        assert run('shortest', path, 'a').returncode == 1


def test_oracle_generated_weighted(tmp_path):
    rng = random.Random(53)
    path = tmp_path / 'g.csv'
    for _ in range(8):
        rows = ['source,target,weight'] + [f'{v},,' for v in 'abcd']
        rows += [f'{u},{v},{rng.randrange(6)}' for u in 'abcd' for v in 'abcd'
                 if rng.random() < .5]
        path.write_text('\n'.join(rows) + '\n')
        check(path, 'a')
