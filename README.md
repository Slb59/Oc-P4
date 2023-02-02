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
$ flake8 model view controller chess.py --format html --htmldir flake8_html_report
```

Le script ``report_flake8.sh`` fait cela.

```
$ chmod +x make_report.sh
$ ./make_report.sh
```