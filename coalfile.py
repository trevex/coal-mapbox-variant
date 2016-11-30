from coal import CoalFile
from util import git_clone, download, unzip, default_cmake_build, cp
from os import path

class MapboxVariantFile(CoalFile):
    repo = "https://github.com/mapbox/variant"
    url = "https://github.com/mapbox/variant/archive/v%s.zip"
    zipfile = "variant.zip"
    exports = ["include"]
    def prepare(self):
        if "version" in self.settings:
            version = self.settings["version"]
            download(self.url % (version), self.zipfile)
            unzip(self.zipfile, 'temp')
            cp('temp/variant-%s/' % (version), 'temp/') # TODO: mv would be cleaner
        else:
            git_clone(self.repo, 'master', 'temp')
    def build(self):
        pass
    def package(self):
        cp('temp/include', 'include')
    def info(self, generator):
        generator.add_include_dir('include/')
