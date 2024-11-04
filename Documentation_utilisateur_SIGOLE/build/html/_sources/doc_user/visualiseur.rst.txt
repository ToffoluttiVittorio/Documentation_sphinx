Le visualiseur
====================

.. _visualiseur:

.. contents:: Table des matières
   :local:
   :depth: 1


Introduction
------------

Le module cartographique de cette plateforme permet de présenter des couches de données géographiques dans un environnement technique. 
Cette interface permet de représenter plusieurs couches géographiques mais ne peut pas se substituer à l'utilisation complète d'un outil SIG bureautique type QGIS.

L'interface se présente comme ceci : 

.. image:: ../images/user_visualiseur/visu_nbr.png
   :alt: Options de filtrage
   :align: center
   :width: 600px

|espace|

- 1 : l'arborescence des couches 
- 2 : recherche d'un lieu 
- 3 : les fonctionnalités 
- 4 : les outils de navigation
- 5 : les fonds de plans

.. note::
   La donnée peut ne pas s'afficher si elle n'est pas disponible ou alors dans le mauvais référentiel de coordonnée.


La gestion des couches
----------------------------------

Si vous cliquez sur 1, l'arborescence des couches va apparaître et vous pourrez : 

- rendre visible ou non la couche
- modifier l'ordre des couches 
- modifier l'opacité en pourcentage

.. image:: ../images/user_visualiseur/visu_couches_details.png
   :alt: Options de filtrage
   :align: center
   :width: 600px

|espace|


Ajouter des données dans l'interface
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Si vous n'avez pas séléctionné de données, dans l'arborescence des couches, vous pouvez, à l'aide de ces 3 boutons : 

.. image:: ../images/user_visualiseur/visu_couches_button.png
   :alt: Options de filtrage
   :align: center
   :width: 200px

|espace|


- ajouter des données directement dans le visualiseur, du catalogue interne et d'autre catalogue enregistré |ajout_couche|: 

.. image:: ../images/user_visualiseur/visu_cat.png
   :alt: Options de filtrage
   :align: center
   :width: 600px

|espace|

Dans cet onglet vous pouvez choisir le catalogue, par défaut, le catalogue est celui de l'office de l'eau mais vous pouvez faire dérouler
la liste pour choisir un autre catalogue. Puis vous pouvez chercher par mots clés des données et les ajouter à l'interface. 

.. note:: 

   Vous pouvez demander au service informatique de rajouter un catalogue de données géographiques dans cet onglet. 

- ajouter des groupes pour vos données avec ce boutton |ajout_group|
- créer des annotations |annotations|: 

.. image:: ../images/user_visualiseur/visu_annotation.png
   :alt: Options de filtrage
   :align: center
   :width: 600px

|espace|


Changer les paramètre de la couches - Style - Informations - Légende 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Lorsque vous cliquez sur une couche, plusieurs fonctions apparaissent : 

.. image:: ../images/user_visualiseur/visu_couches_barre.png
   :alt: Options de filtrage
   :align: center
   :width: 500px

|espace|

**Zoomer sur la couche** |logo-zoom|

**Modifier les réglages de la couche** |logo-reglage|

.. image:: ../images/user_visualiseur/visu_couches_reglages.png
   :alt: Options de filtrage
   :align: center
   :width: 500px

|espace|

Dans ces réglages vous pouvez modifier, les informations, l'affichage, et surtout modifier le style des couches en cliquant sur la pipette |pinceau-blanco| : 

.. image:: ../images/user_visualiseur/visu_style_1.png
   :alt: Options de filtrage
   :align: center
   :width: 600px

|espace|

Si vous ne pouvez pas modifier le style directement il faudra en définir un nouveau et le modifier, cliquez sur le pinceau |logo-pinceau| pour définir
un nouveau style puis modifier le en cliquant sur ce boutton |logo-modif|.

.. image:: ../images/user_visualiseur/visu_styyle.png
   :alt: Options de filtrage
   :align: center
   :width: 600px

|espace|

Une fois dans l'interface de mofication du style, vous pouvez modifier le style actuel et ajouter d'autres règles. Les styles fonctionnent
avec des règles superposées les unes aux autres, cliquez sur cet icone pour ajouter une règle |logo-rond| et sur cet icone |logo-entonnoir|
pour filtrer le style en fonction des attributs: 

.. image:: ../images/user_visualiseur/regles_sup.png
   :alt: Options de filtrage
   :align: center
   :width: 600px

|espace|

Par exemple vous pouvez ajouter une règle qui colore les stations de Saint-Denis en vert : 

.. image:: ../images/user_visualiseur/visu_couche_sup.png
   :alt: Options de filtrage
   :align: center
   :width: 600px

|espace|

Vous pouvez aussi styliser les éléments en fonction d'un attribut, il faut cliquer sur |trois| : 

.. image:: ../images/user_visualiseur/filtre/classif.png
   :alt: Options de filtrage
   :align: center
   :width: 500px

|espace|

Puis vous pourrez attribuer un style qui classifie les éléments en fonction d'un attribut : 

.. image:: ../images/user_visualiseur/filtre/classif_2.png
   :alt: Options de filtrage
   :align: center
   :width: 500px

|espace|

Pour enregistrer le style il faudra le valider en cliquant sur |button_valid|. 

**Filtrer les éléments de la couche** |logo-filtre|

.. image:: ../images/user_visualiseur/visu_filtre.png
   :alt: Options de filtrage
   :align: center
   :width: 600px

|espace|

Vous pouvez filtrer sur un attribut, filtrer en dessinant une zone géographique, ou encore filtrer en fonction d'un attribut d'une autre couche.

**Ouvrir la table attributaire** |logo-table|

.. image:: ../images/user_visualiseur/visuu_table.png
   :alt: Capture d'écran du catalogue
   :align: center
   :width: 600px

Vous pouvez filtrer et télécharger le tableau. Il faut ensuite avoir des droits pour modifier et rajouter des éléments, ces modifications se repportent directement dans le catalogue. 

|espace|

**Supprimer la couche** |logo-bin|

**Créer des graphiques** |logo-graph|

.. image:: ../images/user_visualiseur/widgets.png
   :alt: Capture d'écran du catalogue
   :align: center
   :width: 600px

|espace|

Vous pouvez créer 4 types de gaphiques différents, et ensuite les ajouter sur la carte :

.. image:: ../images/user_visualiseur/graphiques.png
   :alt: Capture d'écran du catalogue
   :align: center
   :width: 600px

|espace|

**Exporter les données de la couche** |logo-down|

**Afficher les informations de la couche** |logo-i|


.. note::
   Les options sont dépendantes de la donnée, elle peuvent ne pas être toutes disponible en fonction de la donnée. 

Pour les fonds de plans, vous pouvez en changer en cliquant sur l'imagette en bas à gauche; : 

.. image:: ../images/user_visualiseur/visu_fonds.png
   :alt: Options de filtrage
   :align: center
   :width: 600px

|espace|



Les fonctionnalités techniques
--------------------------------------------------

Pour ce qui est des différentes fonctionnalités :

.. image:: ../images/user_visualiseur/visu_fct.png
   :alt: Capture d'écran du catalogue
   :align: center
   :width: 50px

|espace|

Dans l'ordre, vous pouvez : 

**Imprimer** une réalisation |print|: 

.. image:: ../images/user_visualiseur/visu_print.png
   :alt: Capture d'écran du catalogue
   :align: center
   :width: 600px

|espace|

Choisir le titre, le format et si la légende apparaît ou non 


**Importer** des données |import|

**Exporter** la carte au format WMC, ne peut pas être exporté puis ajouté à QGIS |export|

**Ajouter** des données à la carte |ajout|

**Charger** des cartes déjà enregistrées |app|

**Mesurer** des distances |mesure|

**Enregistrer** la carte |enreg| : 


.. image:: ../images/user_visualiseur/visu_download.png
   :alt: Capture d'écran du catalogue
   :align: center
   :width: 600px

|espace|

Vous pouvez choisir une imagette, le titre, vous pouvez aussi, en cliquant sur le crayon, définir un texte qui sera visible à l'ouverture de la carte.
Pour définir des droits de lecture et d'édition, vous devez sélectionner un groupe et spécifier si il à les droits de lecture ou d'écriture.
L'enregistrement ira dans la page :ref:`Application <application>`.

**Afficher** les réglages
**Partager** la réalisation
**Afficher la documentation** la documentation
**Faire** le tutoriel 
**Effacer** la session




.. |logo-zoom| image:: ../images/user_visualiseur/button_zoom.png
   :alt: Options de réglage
   :width: 30px

.. |logo-reglage| image:: ../images/user_visualiseur/button_reglage.png
   :alt: Options de réglage
   :width: 30px

.. |logo-filtre| image:: ../images/user_visualiseur/button_filtre.png
   :alt: Options de réglage
   :width: 30px

.. |logo-table| image:: ../images/user_visualiseur/button_table.png
   :alt: Options de réglage
   :width: 30px

.. |logo-bin| image:: ../images/user_visualiseur/button_bin.png
   :alt: Options de réglage
   :width: 30px

.. |logo-graph| image:: ../images/user_visualiseur/button_graph.png
   :alt: Options de réglage
   :width: 30px

.. |logo-down| image:: ../images/user_visualiseur/button_down.png
   :alt: Options de réglage
   :width: 30px

.. |logo-i| image:: ../images/user_visualiseur/button_i.png
   :alt: Options de réglage
   :width: 30px

.. |espace| unicode:: 0xA0 

.. |logo-pinceau| image:: ../images/user_visualiseur/button_pinceau.png
   :alt: Options de réglage
   :width: 30px

.. |logo-modif| image:: ../images/user_visualiseur/button_modif.png
   :alt: Options de réglage
   :width: 30px

.. |pinceau-blanco| image:: ../images/user_visualiseur/visu_pinceau_blanco.png
   :alt: Options de réglage
   :width: 30px

.. |logo-rond| image:: ../images/user_visualiseur/logo_rond.png
   :alt: Options de réglage
   :width: 30px

.. |logo-entonnoir| image:: ../images/user_visualiseur/logo_ento.png
   :alt: Options de réglage
   :width: 30px

.. |button_valid| image:: ../images/user_visualiseur/button_valid.png
   :alt: Options de réglage
   :width: 30px

.. |ajout_couche| image:: ../images/user_visualiseur/button/ajout_couche.png
   :alt: Options de réglage
   :width: 30px

.. |ajout_group| image:: ../images/user_visualiseur/button/ajout_group.png
   :alt: Options de réglage
   :width: 30px

.. |annotations| image:: ../images/user_visualiseur/button/annotation.png
   :alt: Options de réglage
   :width: 30px

.. |ajout| image:: ../images/user_visualiseur/button/ajout.png
   :alt: Options de réglage
   :width: 30px

.. |app| image:: ../images/user_visualiseur/button/app.png
   :alt: Options de réglage
   :width: 30px

.. |bin_session| image:: ../images/user_visualiseur/button/bin_session.png
   :alt: Options de réglage
   :width: 30px

.. |doc| image:: ../images/user_visualiseur/button/doc.png
   :alt: Options de réglage
   :width: 30px

.. |enreg| image:: ../images/user_visualiseur/button/enreg.png
   :alt: Options de réglage
   :width: 30px

.. |export| image:: ../images/user_visualiseur/button/export.png
   :alt: Options de réglage
   :width: 30px

.. |import| image:: ../images/user_visualiseur/button/import.png
   :alt: Options de réglage
   :width: 30px

.. |mesure| image:: ../images/user_visualiseur/button/mesure.png
   :alt: Options de réglage
   :width: 30px

.. |partage| image:: ../images/user_visualiseur/button/partage.png
   :alt: Options de réglage
   :width: 30px

.. |print| image:: ../images/user_visualiseur/button/print.png
   :alt: Options de réglage
   :width: 30px

.. |reglages| image:: ../images/user_visualiseur/button/reglages.png
   :alt: Options de réglage
   :width: 30px

.. |tuto| image:: ../images/user_visualiseur/button/tuto.png
   :alt: Options de réglage
   :width: 30px

.. |trois| image:: ../images/user_visualiseur/filtre/trois.png
   :alt: Options de réglage
   :width: 30px


