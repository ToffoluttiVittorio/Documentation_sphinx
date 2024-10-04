Import de données
===========================

.. contents:: Table des matières
   :local:
   :depth: 1

Introduction
----------------

La page Import permet d'intégrer des données de manière simplifié dans le catalogue.

.. image:: ../images/user_import/import.png
   :alt: Capture d'écran du catalogue
   :align: center
   :width: 600px

Deux format sont acceptés, le shapefile en zip et le CSV, à une limite de 500 Mo. Vous pouvez ajouter votre donnée, cliquer sur le bouton "J'ai le droit de publier cette donnée"
puis passer à l'étape suivante.

Intégration de shapefile
---------------------------

La particularité d'un shapefile est la projection : 

.. image:: ../images/user_import/import_proj.png
   :alt: Capture d'écran du catalogue
   :align: center
   :width: 700px

Pour bien renseigner la donnée, assurez vous que le carré orange qui represente l'emprise de votre donnée est au bon endroit et qu'une projection est renseigné.
De même pour l'encodage, si votre exemple d'objet possède des carractère illisible, vous pouvez changer l'encodage. 

.. note::
   Si pour une donnée, aucune projection n'est valide, veuillez le faire remonter au service informatique.


Intégration de CSV 
---------------------------

La particularité d'un CSV est la geométrie : 

.. image:: ../images/user_import/import_csv.png
   :alt: Capture d'écran du catalogue
   :align: center
   :width: 700px

Pour bien renseigner la donnée, vous pouvez choisir le séparateur de colonne, de texte et aussi renseigner une geométrie ou non. Pour ajouter une geométrie,
il faut obligatoirement un champ latitude et longitude dans le bon format comme sur la photo ci-dessus. 


Processus d'intégration
---------------------------

Vous pouvez ensuite ajouter un titre et une description : 

.. image:: ../images/user_import/import_shape_titre.png
   :alt: Capture d'écran du catalogue
   :align: center
   :width: 600px

Puis ajouter des mots clés en cliquant une fois sur le carré blanc, ce qui fera apparaître les différents mots clés.

.. image:: ../images/user_import/import_shape_keyword.png
   :alt: Capture d'écran du catalogue
   :align: center
   :width: 600px

Ensuite vient la date de création, elle se renseigne automatiquement mais vous pouvez la changer si la donnée est antérieur. 

.. image:: ../images/user_import/import_shape_time.png
   :alt: Capture d'écran du catalogue
   :align: center
   :width: 600px

En dernier, il faut décrire le processus de création de la donnée : 

.. image:: ../images/user_import/import_shape_processus.png
   :alt: Capture d'écran du catalogue
   :align: center
   :width: 600px

Et vous avez un récapitulatif de votre intégration, cliquez sur "publier" pour intégrer la donnée dans le catalogue.

.. image:: ../images/user_import/import_shape_pub.png
   :alt: Capture d'écran du catalogue
   :align: center
   :width: 600px


