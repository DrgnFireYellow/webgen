import _configparser as configparser
import _markdownparser as markdownparser
import os

def build(dir: str):
    os.makedirs(f"{dir}/build")
    config = configparser.read_yaml(f"{dir}/config.yaml")
    for page in os.listdir(f"{dir}/site"):
        html = markdownparser.parse(f"{dir}/site/{page}")
        try:
            with open(f"{dir}/build/{page[:-3]}.html", "x") as f:
                f.write(f"<style> * {{ {configparser.parse_style(config)} }}</style>{html}")
        except FileExistsError:
            with open(f"{dir}/build/{page[:-3]}.html", "w") as f:
                f.write(f"<style> * {{ {configparser.parse_style(config)} }}</style>{html}")
    return