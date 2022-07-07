from typer import Typer
import os

app = Typer()

@app.command()
def build(dir: str):
    """
    Builds the webgen website.
    """
    import _build
    _build.build(dir)
@app.command()
def new(dir: str):
    """
    Creates a new webgen website.
    """
    os.makedirs(f"{dir}/site")
    with open(f"{dir}/config.yaml", "x") as f:
        f.write("""
bg: white
text-color: black
font: sans-serif
justify-text: left
""")

if __name__ == "__main__":
    app()