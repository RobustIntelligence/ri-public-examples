"""Setup file for package."""

from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="ri_public_examples",
    packages=["ri_public_examples"],
    description="Package to download datasets/models/configs for use in RIME",
    long_description=long_description,
    long_description_content_type="text/markdown",
    setuptools_git_versioning={"enabled": True},
    setup_requires=["setuptools-git-versioning"],
    install_requires=["requests"],
    python_requires=">=3.6",
)
