import setuptools

with open("README.md" , "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "deepClassifier"
AUTHOR_USER_NAME = "ywaquar"
SRC_REPO = "deepClassifier"
AUTHOR_EMAIL = "ywaquar@gmail.com"

setuptools.setup(
    name = SRC_REPO,
    version=__version__,
    author= AUTHOR_USER_NAME,
    author_email= AUTHOR_EMAIL,
    description= "A small python package for CNN App",
    long_description=long_description,
    long_description_content_type = "text/markdown",  # Fixed here
    url = f"http://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls = {
        "Bug Tracker" : f"http://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
    },
    package_dir={"": "src"},  # Fixed here
    packages=setuptools.find_packages(where="src")
)
