# Oc-P4 Développez un programme logiciel en Python
---
![logo](data/Logo.png)

## Objectif

## Fonctionnement

## Installation
```bash
# Creer l'environnement virtuel
python -m venv env
source env/bin/activate

# cloner le projet
git clone https://github.com/Slb59/Oc-P4.git
cd Oc-P4

# installer les dépendances
pip install -r requirements.txt

# executer le programme
python chess.py
```

## Utilisation

## Rapport flake
Il est possible de générer un rapport flake8 en utilisant flake8-html.

```
$ flake8 chessmanager chess.py
```

Le script ``report_flake8.sh`` fait cela.

```
$ chmod +x report_flake8.sh
$ ./report_flake8.sh
```

Avec Pycharm, flake8 doit être installé comme outil externe

Il est également possible de générer un rapport avec pycodestyle dans le répertoire outputs :

```
$ chmod +x pep.sh
$ ./pep.sh
```
