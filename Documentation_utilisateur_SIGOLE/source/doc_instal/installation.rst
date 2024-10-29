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


Si vous avez des erreurs de versions de paquets, il faut mettre les bonnes versions, conforme au fichier ``playbooks/georchestra.yml``. 


Serveur mail 
---------------

Pour le serveur mail, pour l'instant un serveur postfix est installé : 

.. code-block:: bash

   apt install postfix 

avec cette configuration dans le fichier /etc/postfix/main.cf : 

.. code-block:: bash

   nano /etc/postfix/main.cf

puis lancer le service : 

.. code-block:: bash

   systemctl start postfix.service

.. code-block:: bash

   # See /usr/share/postfix/main.cf.dist for a commented, more complete version


   # Debian specific:  Specifying a file name will cause the first
   # line of that file to be used as the name.  The Debian default
   # is /etc/mailname.
   #myorigin = /etc/mailname

   smtpd_banner = $myhostname ESMTP $mail_name (Debian/GNU)
   biff = no

   # appending .domain is the MUA's job.
   append_dot_mydomain = no

   # Uncomment the next line to generate "delayed mail" warnings
   #delay_warning_time = 4h

   readme_directory = no

   # See http://www.postfix.org/COMPATIBILITY_README.html -- default to 3.6 on
   # fresh installs.
   compatibility_level = 3.6



   # TLS parameters
   smtpd_tls_cert_file=/etc/ssl/certs/ssl-cert-snakeoil.pem
   smtpd_tls_key_file=/etc/ssl/private/ssl-cert-snakeoil.key
   smtpd_tls_security_level=may

   smtp_tls_CApath=/etc/ssl/certs
   smtp_tls_security_level=may
   smtp_tls_session_cache_database = btree:${data_directory}/smtp_scache



   smtpd_relay_restrictions = permit_mynetworks permit_sasl_authenticated defer_unauth_destination
   myhostname = Ansible-42.myguest.virtualbox.org
   alias_maps = hash:/etc/aliases
   alias_database = hash:/etc/aliases
   mydestination = $myhostname, localhost, localhost.$mydomain, mail.$mydomain, www.$mydomain, localho                                                                                                                                          st, $mydomain
   relayhost =
   mynetworks = 127.0.0.0/8 [::ffff:127.0.0.0]/104 [::1]/128
   mailbox_size_limit = 0
   recipient_delimiter = +
   inet_interfaces = all
   inet_protocols = all


Script de personnalisation
---------------------------------

Les scripts de personnalisation servent à ajouter les spécifications pour l'Office de l'eau Réunion sans directement changer le code d'installation.

Il y'a trois script bash qui modifient les logos, couleurs et référentiel de coordonée dans le dossier "Configuration", voici la commande pour les rendre executable
et les lancer : 

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



Personnalisation du GeoServer
--------------------------------------

Il faut changer à la main certaines configuration du GeoServer : 

- modifier l'url du proxy en y rajoutant votre fqdn et décocher "Utiliser les entêtes pour l'url proxy" en allant dans la page "Services" puis dans "Global" : 

 .. image:: ../images/install/geoserver_global.png
   :alt: Capture d'écran du catalogue  
   :align: center
   :width: 700px

|espace|

- modifier les services pour faire des graphiques, enlever les 2 règels wfs.Transaction et wps.* en allant dans "Sécurité des services" : 

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