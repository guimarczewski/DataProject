# DataProject

## About the project

This repository is an integral part of the "How to Structure a Data Project from Scratch" workshop.

### Goals:

* **Understand the standard project structure**: Organization of directories, such as source code, tests, documentation, among others.

* **Standard structures in data projects**: Project refactoring using classes, modules and best practices in an ETL.

* **Virtual Environment**: Creation of virtual environments using Pyenv and Poetry

* **Tests with Pytest**: Ensure your code works as expected by creating unit and integration tests.

* **Documentation with MKDocs**: Project documentation with MKDocs and publication on [GitHub Pages](https://guimarczewski.github.io/DataProject/)

* **Automation and CI/CD**: Configure integration and continuous delivery routines to maintain project quality using GitHub Actions.


### Installation and Configuration

1. Clone the repository:

```bash
git clone https://github.com/guimarczewski/DataProject.git
cd DataProject
```

2. Configure the correct Python version with pyenv:

```bash
pyenv install 3.11.3
pyenv local 3.11.3
```

3. Install project dependencies:

```bash
poetry install
```

4. Activate the virtual environment:

```bash
poetry shell
```

5. Run the tests:

```bash
task test
```

6. Run the documentation:

```bash
task doc
```

7. Run the ETL pipeline:

```bash
task run
```

8. Check in the data/output folder if the file was generated correctly.
