import setuptools
with open("README.md","r",encoding="utf-8") as f:
    long_description=f.read()

__version__="0.0.0"
REPO_NAME="Text_Summarization-"
AUTHOR_USERNAME="PamuriLakshmanReddy"
SRC_REPO="src"
AUTHOR_EMAIL="lakshman2905@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USERNAME,
    author_email=AUTHOR_EMAIL,
    description="A small packagre for NLP app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USERNAME}/{REPO_NAME}",
    project_urls={"Bug_trackers":f"https://github.com/{AUTHOR_USERNAME}/{REPO_NAME}/issues"},
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)