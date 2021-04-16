# Academi

## Get started:

### Install Python
Source: https://www.python.org/downloads/

### Install Python Virtual Environment
On terminal, type:
- ```sudo pip install virtualenv```
- ```mkdir Academi && cd Academi``` *(Make directory and enter to it)*
- ```virtualenv venv_academi``` *(Create virtualenv named venv_academi or etc, up to you)*
- ```source venv_academi/bin/activate``` *(Activated python virtual env)*


### Install Requirements
- sqlite *https://www.servermania.com/kb/articles/install-sqlite/*
- `sqlite3 academi.db`
- `pip install -r requirements.txt`
- run luigi: ```luigid```
- run ETL Job: ```PYTHONPATH='.' luigi --module luigi_worker runAllTask```