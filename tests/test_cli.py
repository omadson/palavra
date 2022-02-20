from typer.testing import CliRunner

from palavra.cli import app

runner = CliRunner()


def test_tela_de_jogo(capsys):
    result = runner.invoke(app)
    assert result.exit_code == 0
    assert "Tela de jogo" in result.stdout
