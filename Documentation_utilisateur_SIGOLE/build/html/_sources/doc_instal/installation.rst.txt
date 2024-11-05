Installation
=================

.. contents:: Table des matières
   :local:
   :depth: 1

Introduction
------------

Georchestra est une IDG qui intègre plusieurs modules et donc plusieurs technologies, il y'a plusieurs façon d'installer cette infrastructure

- par docker
- par Ansible
- à la main

Le choix pour l'Office de l'eau Réunion à été Ansible qui permet d'installer des paquets Debians rapidement et automatiquement.

Le lien pour le github et la documentation dans son ensemble de georchestra est le suivant : https://github.com/georchestra


Ansible
-----------------------

Prérequis : 

- Debian Bookworm (12.x) VM

- Mettre à jour les paquets :

.. code-block:: bash

   apt update

- Ansible : sudo apt install ansible

.. code-block:: bash

   apt install ansible

- Java 17 : 

.. code-block:: bash

   apt install openjdk-17-jdk

- Si votre VM est nouvelle ou si vous avez apache qui tourne sur le port 80, veuillez l'enlever : 

.. code-block:: bash

   apt remove apache2

- Clone the source, le code est issue du repo "ansible" de georchestra :

.. code-block:: bash

   apt install git
   git clone https://github.com/ToffoluttiVittorio/ansible.git


- Aller dans le répertoire du repo git, toutes les commandes de cette partie se lance à partir de ce repertoire si non spécifié :

.. code-block:: bash
   
   cd ansible

- Changer le fqdn dans le fichier ``playbooks/georchestra`` ligne 88 avec la variable ``fqdn`` et modifier ``georchestra.ole.re`` : 

.. code-block:: bash
   
   nano playbooks/georchestra.yml

dans la ligne : 

.. code-block:: bash

   fqdn: georchestra.ole.re

- et dans le fichier de personnalisation ``Configuration/last.sh``, remplacer ``georchestra.ole.re`` par votre fqdn : 

.. code-block:: bash

   nano Configuration/last.sh

dans la ligne : 

.. code-block:: bash

   echo '127.0.0.1 georchestra.ole.re' | sudo tee -a /etc/hosts > /dev/null

- Installer les rôles de GeoNetwork :

.. code-block:: bash

   ansible-galaxy install -r requirements.yaml
   chmod -777 roles/

- Il faut run le playbooks qui est l'installation de tous les modules : 

.. code-block:: bash

   ansible-playbook playbooks/georchestra.yml

.. note::

   Des erreurs peuvent apparaître lors de cette étape, veuillez consulter le chapitre juste en dessous "Erreurs fréquentes" si cela arrive.

L'installation de l'infrastructure de geOrchestra est faite, il reste à installer un serveur de mail et les scripts de personnalisation pour avoir
l'application fonctionnel et complète pour l'Office de l'eau Réunion.


Erreurs fréquentes 
----------------------------

Une erreur lors de la première installation mais n'est asbsolument pas blocante : 

.. code-block:: bash

   TASK [openldap : check if the root already exists] ******************************************************************
   fatal: [localhost]: FAILED! => {"changed": true, "cmd": ["ldapsearch", "-x", "-b", "dc=georchestra,dc=org", "dc=georchestra"], "delta": "0:00:00.009190", "end": "2024-10-09 09:19:33.368546", "msg": "non-zero return code", "rc": 32, "start": "2024-10-09 09:19:33.359356", "stderr": "", "stderr_lines": [], "stdout": "# extended LDIF\n#\n# LDAPv3\n# base <dc=georchestra,dc=org> with scope subtree\n# filter: dc=georchestra\n# requesting: ALL\n#\n\n# search result\nsearch: 2\nresult: 32 No such object\n\n# numResponses: 1", "stdout_lines": ["# extended LDIF", "#", "# LDAPv3", "# base <dc=georchestra,dc=org> with scope subtree", "# filter: dc=georchestra", "# requesting: ALL", "#", "", "# search result", "search: 2", "result: 32 No such object", "", "# numResponses: 1"]}
   ...ignoring


Si vous avez des erreurs sur ``sviewer`` ou ``htodcs`` de ce type : 

.. code-block:: bash

   TASK [georchestra : checkout sviewer] *******************************************************************************************************************************************************************************************************
   fatal: [localhost]: FAILED! => {"changed": false, "msg": "Unable to parse submodule hash line: Entrée dans 'lib/ol3'"}

Il faut supprimer le repertoire htdocs, et relancer le run du playbook : 

.. code-block:: bash

   rm -r /var/www/georchestra/htdocs

.. note::

   Si vous avez encore une erreur lors de l'installation après avoir supprimer le repertoire htdocs, il faut souvent relancer encore le playbook sans rien toucher


Si vous avez des erreurs de versions de paquets, il faut mettre les bonnes versions, conforme au fichier ``ansible/playbooks/georchestra.yml``. 


Serveur mail 
---------------

Pour le serveur mail, un postfix est installé sur la vm et est réliée à carbonio, copier la configuration faite dans la vm dev-carto.ole.re, 
le mail de l'administrateur se définit dans ``ansible/playbooks/georchestra.yml`` et les templates des mails sont dans ``/etc/georchestra/datafeeder``
et ``/etc/georchestra/``

Script de personnalisation
---------------------------------

Les scripts de personnalisation servent à ajouter les spécifications pour l'Office de l'eau Réunion sans directement changer le code d'installation.

Il y'a trois script bash qui modifient les logos, couleurs, référentiel de coordonée ... dans le dossier "Configuration", les lancer depuis ``ansible/Configuration``
voici la commande pour les rendre executable et les lancer : 

.. code-block:: bash

   cd Configuration

.. code-block:: bash

   chmod 777 script_remplacement.sh
   chmod 777 other.sh
   chmod 777 last.sh

.. code-block:: bash

   ./script_remplacement.sh
   ./other.sh
   ./last.sh


Thesaurus
---------------

Le thesaurus est le catalogue de mots clés utilisé lors de l'intégration de données par les agents.
Par defaut, georchestra utilise le catalogue INSPIRE, vous pouvez le modifier en allant sur :ref:`thesaurus <thesaurus>`.

Activer le module analytics
-------------------------------

Pour activer le module analytics, il faut changer les droits du schéma "ogcstatistics" de postgres à georchestra. 
La base de donnée est accessible avec psql : 

.. code-block:: bash

   psql -U postgres -h localhost -d georchestra

Puis il faut lancer :

.. code-block:: bash

   ALTER SCHEMA ogcstatistics OWNER TO georchestra;


Certificat ssl 
--------------------

Pour autoriser le geoserver et mapstore à communiquer entre eux pour la fonction print de mapstore, il est nécéssaire d'ajouter le certificat ssl à java,
cette documentation fonctionne parfaitement : https://stackoverflow.com/questions/14947517/pkix-path-building-failed-sun-security-provider-certpath-suncertpathbuilderexce.

IL faut copier la valeur du certificat qui apparaît dans votre navigateur et l'enregistrer avec ".der", puis localiser votre $JAVA_HOME, et dans lib puis security se trouve 
un fichier "cacerts", il faudra lancer : 

.. code-block:: bash

   sudo keytool -import -alias mysitedev -keystore  $JAVA_HOME/jre/lib/security/cacerts -file dev.der

où "mysitedev" est votre fqdn et dev.der le certificat, le mot de passer par défaut est : "changeit". 


Personnalisation du GeoServer
--------------------------------------

Il faut changer à la main certaines configuration du GeoServer : 

- modifier l'url du proxy en y rajoutant votre fqdn et décocher "Utiliser les entêtes pour l'url proxy" en allant dans la page "Services" puis dans "Global" : 

 .. image:: ../images/install/geoserver_global.png
   :alt: Capture d'écran du catalogue  
   :align: center
   :width: 700px

|espace|

- modifier les services pour modifier les données depuis mapstore et faire des graphiques, enlever les 2 règels wfs.Transaction et wps.* en allant dans "Sécurité des services" 
   si vous le souhaitez : 

 .. image:: ../images/install/geoserver_services.png
   :alt: Capture d'écran du catalogue  
   :align: center
   :width: 700px

|espace|



Une fois l'installation terminé, il faudra relancer le datafeeder et le reste de l'infrastructure: 

.. code-block:: bash

   systemctl restart datafeeder.service 


Relancer l'infrastructure
---------------------------

Pour relancer l'infrastructure, il faut relancer les 3 tomcats et potentiellement nginx : 

.. code-block:: bash

   sudo systemctl restart tomcat@georchestra.service

.. code-block:: bash

   sudo systemctl restart tomcat@geoserver.service

.. code-block:: bash

   sudo systemctl restart tomcat@proxycas.service

.. code-block:: bash
   
   sudo systemctl restart nginx


Se rendre sur l'application 
----------------------------------

Pour se rendre sur l'application, aller à l'addresse : 

.. code-block:: bash

   https://le_fqdn_renseigné/


.. |espace| unicode:: 0xA0 