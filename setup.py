''' This script prepares the configuration needed for packaging the Python module 
so that it can be easily distributed and installed by others'''

import setuptools
'''setuptools is a library, which is a collection of utilities that aids in the 
packaging, distribution, and installation of Python packages.'''

with open("README.md","r",encoding="utf-8") as f:
    long_description = f.read()

#Package information
__version__ = "0.0.0"

REPO_NAME = "Chicken-Disease"
AUTHOR_USER_NAME = "syedsabeel88"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "syedsabeel88@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version= __version__,
    author=AUTHOR_USER_NAME,
    author_email= AUTHOR_EMAIL,
    description= "A smally python package for CNN app",
    long_description= long_description,
    long_description_content = "text/markdown",
    url= f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls = {
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages= setuptools.find_packages(where="src")
)