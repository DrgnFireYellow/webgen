import markdown


def parse(file : str):
    with open(file, "r") as f:
        text = f.read()
    return markdown.markdown(text)
