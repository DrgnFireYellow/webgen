from yaml import load, Loader


def read_yaml(file):
    with open(file, "r") as f:
        text = f.read()
    return load(text, Loader=Loader)


def parse_style(data: dict):
    style = ""
    style += f'background: {data["bg"]};\n'
    style += f'color: {data["text-color"]};\n'
    style += f'font-family: {data["font"]};\n'
    style += f'text-align: {data["justify-text"]};\n'
    return style
