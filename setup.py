from setuptools import setup


with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

REPO_NAME = "Study"
AUTHOR_USER_NAME = "DafinaZaka"
SRC_REPO = "src"
LIST_OF_REQUIREMENTS = ['streamlit']


setup(
    name=SRC_REPO,
    version="0.0.1",
    author=AUTHOR_USER_NAME,
    description="Recommender System for Online Learnig Platforms",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    author_email="zakadafinagmail.com",
    packages=[SRC_REPO],
    license="MIT",
    python_requires=">=3.9",
    install_requires=LIST_OF_REQUIREMENTS
)
