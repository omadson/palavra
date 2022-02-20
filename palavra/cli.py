"""palavra

Um clone to term.ooo
"""
import typer

app = typer.Typer(help=__doc__, add_completion=False)


@app.callback(invoke_without_command=True)
def play():
    typer.echo("Tela de jogo")


@app.command()
def statistics():
    typer.echo("Suas estatísticas")


if __name__ == "__main__":
    app()
