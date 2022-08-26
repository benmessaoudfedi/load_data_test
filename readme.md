# TEST DJANGO - FEDI BEN MESSAOUD

# installation 
- Use python 3.10

Lancer les commandes suivantes.

#### Création de l'environement virtuel
```bash
> python -m venv env
> cd env/scripts
> activate
> cd ../..
```
#### Configuration requise pour l’installation
```bash
> pip install -r requirements.txt
```

# Démarrer le serveur: 

```bash
> py manage.py runserver
```
# Insertion des Données dans la table Documents:
Lien :
```bash
> http://127.0.0.1:8000/load_csv/
```
# Récupération des données et des supports d'un document donné sur base de sa clef. 

Merci de vérifier que la base est bien alimentée.
Exp:
```bash

> http://127.0.0.1:8000/document-support/DD241051
```

# Démarrer le Test:
Lancer la commande suivante dans le Terminal.
```bash

> pytest
```
