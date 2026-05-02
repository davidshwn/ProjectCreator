from setuptools import find_packages, setup

setup(
    name="ProjectCreator",
    version="0.2",
    install_requires=["ollama"],
    packages=find_packages(),
    entry_points={"console_scripts": ["ProjectCreator=ProjectCli.main:main"]},
)
