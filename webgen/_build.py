import _configparser as configparser
import _markdownparser as markdownparser
import os

def build(dir: str):
    config = configparser.read_yaml(f"{dir}/config.yaml")
    for page in os.listdir(f"{dir}/site"):
        html = markdownparser.parse(f"{dir}/site/{page}")
        with open(f"{dir}/build/{page[:-3]}.html", "w") as f:
            f.write(f"<style> * {{ {configparser.parse_style(config)} }}</style>{html}")
    return