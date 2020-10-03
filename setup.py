import os
from setuptools import setup, find_packages
from setuptools.command.install import install as _install

class Install(_install):
    def run(self):
        _install.do_egg_install(self)
        import nltk
        nltk.download("punkt")
        #nltk.download("wordnet")
        #nltk.download("averaged_perceptron_tagger")
           
with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(...
    cmdclass={'install': Install},
    install_requires=[],
    setup_requires=[required]
   )
