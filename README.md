# desafio-técnico-jusbrasil

Para executar projeto é preciso seguir todos os passo a baixo para que funcione adequadamente.

## Requisitos

* [Django](https://www.djangoproject.com/)
* [Scrapy](https://scrapy.org/)
* [Git](http://git-scm.com/)
* [Python](https://www.python.org/)
* [Pip](http://www.pip-installer.org/en/latest/)
* [Virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/)

## Configuração de Ambiente

### **Instalando todas as dependências**

```
$ mkvirtualenv jusbrasil -p python3
$ pip install -r requirements.txt
```
### **Executando o crawler**

```
$ scrapy crawl tjal_primeiro_grau
```
### **Carregar todos os dados**

```
$ python manage.py makemigrations
$ python manage.py migrate
```
## Executando o Api

```
$ python manage.py runserver
```
Após subir o projeto verifique na porta 8000:

http://localhost:8000/