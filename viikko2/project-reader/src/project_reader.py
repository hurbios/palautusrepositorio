from urllib import request
from project import Project
import toml

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        toml_contents = toml.loads(content, _dict=dict)
        tool = toml_contents.get('tool')
        poetry = tool.get('poetry')

        return Project(
            poetry['name'],
            poetry['description'],
            poetry['dependencies'],
            poetry['group']['dev']['dependencies'],
            poetry['license'],
            poetry['authors'],
        )
