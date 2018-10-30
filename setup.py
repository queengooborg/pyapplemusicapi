# -*- coding: utf-8 -*-
import itunes
from setuptools import setup

with open('README.md') as f:
    readme = f.read()
with open('requirements.txt') as f:
    requires = [line.strip() for line in f if line.strip()]

setup(
    name='pitunes',
    version=itunes.__version__,
    description="A simple python wrapper to access iTunes Store API",
    long_description=readme,
    long_description_content_type="text/markdown",
    author=itunes.__author__[0],
    author_email=itunes.__email__[0],
    maintainer=itunes.__maintainer__,
    maintainer_email=itunes.__email__[0],
    license='http://www.gnu.org/copyleft/gpl.html',
    platforms=['any'],
    url='https://github.com/vinyldarkscratch/pitunes',
    packages=['itunes'],
    install_requires=requires,
    zip_safe=False,
)
