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
- `pip install -r requirements.txt`

### Run Project
- open terminal with active virtualenv
- run luigi: ```luigid```
- open new terminal with active virtualenv
- execute ```python db_config.py```
- run ETL Job: ```PYTHONPATH='.' luigi --module luigi_worker runAllTask```
- To check the status, open web browser and type `http://localhost:8082`
- To check that ETL job was completed load to DB, run `sqlite3 academi.db` and then `.tables`