# Data Project from Scratch

![Flow](static/fluxo.png)

This is an example project dedicated to demonstrating refactoring practices. In this space, you will find an in-depth description of ETL, installation instructions, answers to frequently asked questions, and more. Whether you are a collaborator or simply someone interested in the project, we hope you find this documentation useful.

Additionally, this documentation can be integrated into Confluence or an internal intranet, facilitating access and collaboration for all team members.

## Sections

- [Data Project from Scratch](#Data Project from Scratch)
   - [Sections](#sections)
   - [Introduction](#introduction)
   - [Installation Guide](#installation-guide)

## Introduction

The objective of this project is to demonstrate how refactoring techniques can be applied to improve code quality, optimize performance and make software more maintainable. Refactoring is essential for keeping code clean and understandable, allowing teams to maintain high development velocity over time.

Prerequisites:

- Git for code versioning
- Pyenv for creating virtual environments
- Poetry for dependency management
- Pytest for unit and integration testing
- MKDocs for documentation and GitHub Pages to host it
- GitHub Actions for Continuous Integration

## Installation Guide

Here, you will find detailed instructions on how to install and configure the project in your local environment. Following the instructions correctly ensures that you have a smooth experience when working on the project.

### `Clone the repository`

```python
git clone https://github.com/guimarczewski/DataProject.git
cd DataProject
```

### `Configure the correct Python version with pyenv`

```python
pyenv install 3.11.3
pyenv local 3.11.3
```

### `Install project dependencies`

```python
poetry install
```

### `Activate the virtual environment`

```python
poetry shell
```

### `Run the tests`

```python
task test
```

### `Run the documentation`

```python
task doc
```

### `Run the pipeline`

```python
task run
```
