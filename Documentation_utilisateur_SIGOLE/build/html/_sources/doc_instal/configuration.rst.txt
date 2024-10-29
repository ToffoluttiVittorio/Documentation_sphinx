Configuration
=================

.. contents:: Table des matières
   :local:
   :depth: 1

Introduction
------------

Le code étant très dense et compilé, il faudra comprendre la structure et les fichiers de configuration mis à dispostion plutôt que le code en profondeur.

Localisation des différents répertoires
------------------------------------------------

Les logs des différents modules sont dans : ``/srv/log/``

Les binaires et le code source sont divisée en trois :  

- ``/srv/tomcat/georchestra/webapps`` pour les modules analytics, console, geonetwork, geowebcache, header, import, mapstore
- ``/srv/tomcat/geoserver/webapps`` pour le module geoserver
- ``/srv/tomcat/proxycas/webapps`` pour les modules cas et ROOT    

Les données de geonetwork et geoserver sont dans le repertoire : ``/srv/data/``

Les pages web statiques sont dans : ``/var/www/georchestra/htdocs/``

Le module nginx est lui dans : ``/etc/nginx/``

Les dossiers de configuration se trouve dans : ``/etc/georchestra/``, ils sont documentés, facile à parcourir et modifier.

Fichiers de configuration du datadir 
-----------------------------------------

GeOrchestra possèdent un "datadir" qui est un repertoire de fichiers de configuration qui sert à modifier rapidement certaines configurations.
Il se situe dans : ``/etc/georchestra``
Il faut ensuite naviguer dans les différents répertoies pour modifier la configuration de chaque module.

Les paramètres généraux peuvent être modfiées dans le fichier ``/etc/georchestra/default.properties`` où il est possible de modifier : 

- le logo
- le style du header
- les paramètre de postgresql
- les paramètre du ldap
- les paramètres du rabittmq
- les paramètres SMTP

Ensuite il faut naviguer dans les différents sous-répertoire pour modifier spécifiquement les configs, voici le lien
de la documentation qui explique cela plus en détails : https://github.com/georchestra/datadir

Versionnement des modules 
--------------------------------

Le versionnement s'effectue dans le fichier issue du clone du repo git ``ansible/playbooks/georchestra.yml`` qui est le fichier qui va spécifier les versions et les modules à installer
lors du lancement de l'installation.

Ce fichier sert à configurer : les versions, les chemins, les ports, les modules ... 

Il est très simple à lire et comprendre et se trouve dans ``ansible/playbooks/georchestra.yml``. 

Si vous voulez que les modifications dans ce fichiers s'execute il faut relancer l'installation dans le repo du git cloné: 

.. code-block:: bash

   sudo ansible-playbook playbooks/georchestra.yml
   
Base de donnée 
------------------------------

La base de donnée est accessible avec psql : 

.. code-block:: bash

   psql -U georchestra -h localhost

Elle stocke les données dans différents schémas. Il n'est pas nécéssaire de l'utiliser.


Scripts de personnalisation
----------------------------

Les scripts sont écris en shell, facile à comprendre et facilement modifiable, ils sont au nombre de 3 :

- script_remplacement.sh
- other.sh
- last.sh

et sont dans ``ansible/Configuration``. 