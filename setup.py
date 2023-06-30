from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.1.0'
DESCRIPTION = 'A package that implements zdd algorithms'

# Setting up
setup(
    name="zdd_algorithms",
    version=VERSION,
    author="Thilo Langensteiner",
    author_email="<thilo.j.la@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=open('README.md').read(),
    url="https://github.com/Thilo-J/zdd_algorithms",
    packages=find_packages(),
    install_requires=['graphviz'],
    keywords=['python', 'zdd', 'bdd', 'zsdd', 'zero-suppressed', 'decision diagram'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)