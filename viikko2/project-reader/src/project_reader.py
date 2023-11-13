from urllib import request
from project import Project
import toml

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        # deserialisoi
        kontsa = toml.loads(content)
        #helpota elämää
        poetry_dict = kontsa['tool']['poetry']

        # lataa yksittäiset arvot
        nimi = poetry_dict['name']
        kuvaus = poetry_dict['description']
        lisenssi = poetry_dict['license']
        tekijat = poetry_dict['authors']
        riippuvuudet = list(poetry_dict['dependencies'].keys())
        kehitysriippuvuudet = list(poetry_dict['group']['dev']['dependencies'].keys())

        # Muodosta Project-olio tietojen perusteella
        return Project(nimi, kuvaus, lisenssi, tekijat, riippuvuudet, kehitysriippuvuudet)
