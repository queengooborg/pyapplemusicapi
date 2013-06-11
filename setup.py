import os.path
try:
    from setuptools import setup, Extension
except ImportError:
    from distutils.core import setup, Extension

VERSION = "1.1"

setup(
    name = "python-itunes",
    version = VERSION,
    description="A simple python wrapper to access iTunes Store API",
    author='Jonathan Nappi',
    author_email='moogar@comcast.net',
    maintainer='Jonathan Nappi',
    maintainer_email='moogar@comcast.net',
    license = "http://www.gnu.org/copyleft/gpl.html",
    platforms = ["any"],    
    url="https://github.com/moogar0880/python-itunes",
    packages=['itunes'],
)
