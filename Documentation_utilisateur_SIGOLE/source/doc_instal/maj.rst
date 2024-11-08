Mise à jour
=================

.. contents:: Table des matières
   :local:
   :depth: 1

Introduction
------------

La version actuelle de geOrchestra est la version 24, les versions sont supporté pendant 1 an avec des patchs mineurs qui ne demande pas de 
configuration supplémentaire et peuvent être installées avec les paquets debians directement. 

Pour ce qui est de l'installation de versions majeurs, elle se font en modifiant le fichier ``georchestra.yml``,
il faudra relancer toute l'installation et potentiellement faire des ajustements.

Ne pas lancer la mise à jour de tous les paquets de georchestra d'un coup, des versions peuvent ne pas être compatible entre elles,
veuillez vous référer aux différentes releases et leurs compatibilités : https://github.com/georchestra/georchestra/releases 

Paquets debians
-----------------------

Voici la liste des paquets debians installé par georchestra : 

.. image:: ../images/install/debian_paquet.png
   :alt: Capture d'écran du catalogue
   :align: center
   :width: 700px

|espace|

Lancer la mise à jour des paquets debians si des patchs mineurs ont été apportés. 

D'autres paquets sont aussi installé sur la machine : 

- tomcat9
- nginx
- postgresql
- elasticsearch
- kibana


.. |espace| unicode:: 0xA0 