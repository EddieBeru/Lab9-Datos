"""Escenarios AS-001–AS-009 de Feature 1, contrato observable."""
import json
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]


def run(*args):
    return subprocess.run([sys.executable, '-m', 'graph_lab', *map(str, args)],
                          capture_output=True, text=True, cwd=ROOT)


def show(path):
    result = run('show', path)
    assert result.returncode == 0, result.stderr
    assert result.stderr == ''
    data = json.loads(result.stdout)
    assert data['vertices'] == sorted(set(data['vertices']))
    assert data['edges'] == sorted(map(list, set(map(tuple, data['edges']))))
    return data


def test_AS001_valid(tmp_path):
    path = tmp_path / 'g.csv'
    path.write_text('source,target\na,b\nb,c\n')
    assert show(path) == {'vertices': ['a', 'b', 'c'], 'edges': [['a', 'b'], ['b', 'c']]}


def test_AS002_curriculum():
    data = show(ROOT / 'data/cs-curriculum.csv')
    assert len(data['edges']) == 23
    assert data['edges'].count(['Data Structures', 'Algorithms']) == 1
    assert set(data['vertices']) == {v for edge in data['edges'] for v in edge}


def test_AS003_isolated_watch():
    data = show(ROOT / 'data/small-dag.csv')
    assert len(data['vertices']) == 9 and len(data['edges']) == 9
    assert 'watch' in data['vertices']
    assert all('watch' not in e for e in data['edges'])


def test_AS004_cycles_displayed():
    data = show(ROOT / 'data/build-with-cycle.csv')
    assert len(data['edges']) == 13
    for edge in [['auth', 'session'], ['session', 'user-profile'],
                 ['user-profile', 'auth'], ['metrics', 'metrics']]:
        assert edge in data['edges']


@pytest.mark.parametrize('name', ['missing.csv', '.'])
def test_AS005_unreadable_path(name):
    result = run('show', ROOT / name)
    assert result.returncode == 1 and result.stdout == ''
    assert result.stderr.startswith('Error: no se pudo leer ')
    assert 'Traceback' not in result.stderr


@pytest.mark.parametrize('args', [[], ['show'], ['unknown'], ['show', 'x', '--bad']])
def test_AS007_bad_usage(args):
    result = run(*args)
    assert result.returncode == 2 and result.stdout == ''
    assert 'usage:' in result.stderr and 'Traceback' not in result.stderr


def test_AS007_help():
    result = run('--help')
    assert result.returncode == 0 and 'show' in result.stdout and not result.stderr


def test_AS008_empty_graph(tmp_path):
    path = tmp_path / 'g.csv'
    path.write_text('source,target\n\n')
    assert show(path) == {'vertices': [], 'edges': []}


def test_AS009_names_csv_bom(tmp_path):
    path = tmp_path / 'g.csv'
    path.write_text('\ufeffsource,target\r\n A , a \r\n"with,comma",inside space\r\n')
    assert show(path) == {'vertices': ['A', 'a', 'inside space', 'with,comma'],
                          'edges': [['A', 'a'], ['with,comma', 'inside space']]}
