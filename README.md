# Cadastramento e avaliação de restaurantes

Aplicação desenvolvida em Python com o intuito de aprofundar na orientação a objetos, auxiliado pela plataforma Alura. 
Projeto1 contém o código feito com funções (app2.py) e utilizando classes (app.py) com as respectivas classes na pasta modelos. Foi desenvolvida a compreensão de POO, herança, polimorfismo, variáveis de ambiente (usando venv do Python), refatoração e os decorators do Python, como @classmethod, @property. 
Projeto2 contém um projeto utilizando FastAPI, desenvolvido para aprender e compreender o uso de APIs, arquivos .json, variáveis de ambiente e a biblioteca requests.

### Instalação
### 📋 Projeto 1 -> Classes e Funções

Para clonar o repositório na sua máquina basta clonar:
```
git clone 
```
No terminal, para executar o projeto1, utilizando o conecito de classes:
```
python3 .\app.py
```
No terminal, para executar o projeto1, utilizando o conecito de funções
```
python3 .\app2.py
```

### Projeto 2 -> Json e FastAPI

Para o PROJETO2 , é necessário criar uma variável de ambiente, ativa-la e instalar os requisitos.
No terminal do projeto, após ter clonado-o:
```
python -m venv venv
```
```
.\venv\Scripts\activate 
```
```
pip install -r requirements.txt 
```
Como utiliza o framework FastAPI, é necessário instala-lo, utilizando o pip, dentro da variável de ambiente. Para isso, basta digitar no terminal:
```
pip install fastapi
pip install uvicorn
```
Ative o servido e clique no ip que irá aparecer no terminal.
```
uvicorn main:app --reload
```
Digite: ```http://127.0.0.1:8000/docs``` para visualizar todos os endpoints da aplicação.

### 🔧 Funcionamento
O projeto 1 têm o intuito de: a partir do app.py, criar um restaurante a partir da classe Restaurante, criar pratos e bebidas através de suas respectivas classes, aplicar a função desconto e adiciona-los ao cardápio, no final listar o caardápio no console. Para criar novos pratos, deve-se alterar no próprio arquivo app.py

O projeto 2 têm o intuito de: a partir do app.py separar os itens dos cardápios dos restaurantes por restaurante, por meio de uma api, criando assim um arquivo .json para cada restaurante com seu cardápio.
Além disso, por meio do FastAPI criar uma 'api' que disponibilizar esse cardápio.


## 🛠️ Construído com

* [Visual Studo Code](https://code.visualstudio.com/) - Editor de texto 
* [Python](https://www.python.org/) - Linguagem usada
* [FastAPI](https://fastapi.tiangolo.com/) - Framework usado
* [GIT](https://git-scm.com/) - Controle de versionamento 

## 🎁 Conclusão

* Projeto desenvolvido para aprofundar em POO, com python, e iniciar no caminho do backend;
* Compreensão de API's, git e variáveis de ambientes;
* Desenvolvido com ajuda da plataforma Alura;