"""AS-005/006: lector e integración de errores sin salida parcial."""
import pytest
from test_show import run


@pytest.mark.parametrize('content', [b'', b'a,b\n', b'source,target\na\n',
    b'source,target\na,b,c\n', b'source,target\n,b\n', b'source,target\n,\n',
    b'source,target\na,b\nc\n', b'source,target\n"unclosed,b\n',
    b'source,target\n   \n'])
def test_AS006_invalid_structure(tmp_path, content):
    path = tmp_path / 'bad.csv'
    path.write_bytes(content)
    result = run('show', path)
    assert result.returncode == 1 and result.stdout == ''
    assert result.stderr.startswith('Error: línea ')
    assert 'Traceback' not in result.stderr


def test_AS006_encoding(tmp_path):
    path = tmp_path / 'bad.csv'
    path.write_bytes(b'source,target\n\xff,b\n')
    result = run('show', path)
    assert result.returncode == 1 and result.stdout == ''
    assert result.stderr.startswith('Error: no se pudo leer ')


def test_AS005_permissions(monkeypatch):
    from pathlib import Path
    from graph_lab.cli import main
    def denied(*args, **kwargs):
        raise PermissionError('denied')
    monkeypatch.setattr(Path, 'open', denied)
    assert main(['show', 'denied.csv']) == 1
