# Data Project

## Sobre o Projeto

Este repositório é uma parte integrante do workshop "Como estruturar um projeto de dados do Zero".

### Objetivos:

* **Entender a estrutura padrão de projetos**: Organização de diretórios, como o código-fonte, testes, documentação, entre outros.

* **Estruturas padrões em projetos de dados**: Refatoração do projeto utilizando classes, módulos e boas práticas em uma ETL.

* **Ambiente Virtuais**: Criação de ambiente virtuais utilizando o Pyenv e Poetry

* **Testes com Pytest**: Garanta que seu código funcione como esperado, criando testes unitários e de integração.

* **Documentação com MKDocs**: Documentação do projeto com MKDocs e publicação no [GitHub Pages](https://guimarczewski.github.io/DataProject/)

* **Automatização e CI/CD**: Configurar rotinas de integração e entrega contínua para manter a qualidade do projeto utilizando GitHub Actions.


### Instalação e Configuração

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
