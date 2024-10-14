Pour cette documentation, la bibliothèque Sphinx est utilisé en utilisant un thème fourni par Read the Docs. 
Pour compiler cette documentation, il faut avoir Python : https://www.python.org/downloads/ 
puis MikTeX : https://miktex.org/download et enfin Perl : https://strawberryperl.com/ 
Une fois cela installé, allez dans une console cmd et tapez : 'pip install sphinx'. 
Allez dans le répertoire Documentation_utilisateur_SIGOLE et lancez 'make.bat html' pour générer la page html. 
Et lancez make latexpdf pour générer un pdf de la documentation qui sera ensuite dans le répertoire build/latex.
 

Si vous voulez repartir de zéro et juste utiliser Sphinx, après le 'pip install sphinx' il faut aussi lancer : 'sphinx-quickstart'
et remplir les champs demandé. Et pour avoir le thème "Read the docs" il faut lancer cette commande : 'pip install sphinx_rtd_theme'
puis aller dans le dossier 'source' et modifier le fichier 'conf.py' pour la variable : html_theme = 'sphinx_rtd_theme.
