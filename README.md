# Documentation de Sphinx pour SIGOLE

Cette documentation utilise la bibliothèque **Sphinx** avec le thème **Read the Docs**. Pour compiler cette documentation, vous devez suivre les étapes ci-dessous :

## Prérequis

1. **Installer Python** : 
   - Téléchargez Python à partir de [python.org](https://www.python.org/downloads/).

2. **Installer MikTeX** pour le pdf: 
   - Téléchargez MikTeX depuis [miktex.org](https://miktex.org/download).

3. **Installer Perl** pour le pdf: 
   - Téléchargez Strawberry Perl à partir de [strawberryperl.com](https://strawberryperl.com/).

## Installation de Sphinx

Après avoir installé les prérequis, ouvrez une console `cmd` et exécutez la commande suivante pour installer Sphinx :

```
pip install sphinx
```


## Génération de la documentation

1. **Accédez au répertoire** de votre projet :

```
cd Documentation_utilisateur_SIGOLE
```

2. **Générez la page HTML** :

```
make html
```

3. **Générez un PDF de la documentation** :

```
make latexpdf
```

Le PDF sera disponible dans le répertoire `build/latex`, il faudra ensuite le copier à coté de index.html pour que le code fonctionne correctement. 


## Repartir de zéro avec Sphinx

Si vous souhaitez repartir de zéro et juste utiliser Sphinx en ayant au préalable installé python et sphinx avec `pip`, exécutez la commande suivante :

```
sphinx-quickstart
```

Remplissez les champs demandés pour configurer votre projet.

### Installation du thème "Read the Docs"

Pour utiliser le thème **Read the Docs**, exécutez la commande suivante :

```
pip install sphinx_rtd_theme
```

Ensuite, accédez au dossier `source` et modifiez le fichier `conf.py` en changeant la variable :

```
html_theme = 'sphinx_rtd_theme'
```