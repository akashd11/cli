import typer
import comp

app = typer.Typer()


@app.command()
def create(name: str):
    comp.create(name)


@app.command()
def delete(name: str, formal: bool = False):
    comp.delete(name, formal)


def cli():
    app()






