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
- Ansible : sudo apt install ansible

.. code-block:: bash

   sudo apt install ansible

- Java 17 : 

.. code-block:: bash

   sudo apt install openjdk-17-jdk

- Si votre VM est neuve ou si vous avez apache qui tourne sur le port 80, veuillez l'enlever : 

.. code-block:: bash

   sudo apt remove apache2

- Clone the source, le code est issue du repo "ansible" de georchestra :

.. code-block:: bash

   sudo apt install git
   sudo git clone https://github.com/ToffoluttiVittorio/ansible.git


- Aller dans le répertoire du repo git, toutes les commandes de cette partie se lance à partir de ce repertoire si non spécifié :

.. code-block:: bash
   
   cd ansible

- Changer le fqdn dans le fichier ``playbooks/georchestra`` ligne 88 avec la variable ``fqdn`` : 

.. code-block:: bash
   
   fqdn: georchestra.ole.re

- et dans le fichier de personnalisation ``Configuration/last.sh``, remplacer georchestra.ole.re par votre fqdn : 

.. code-block:: bash

   echo '127.0.0.1 georchestra.ole.re' | sudo tee -a /etc/hosts > /dev/null

- Installer les rôles de GeoNetwork :

.. code-block:: bash

   sudo ansible-galaxy install -r requirements.yaml
   sudo chmod -777 roles/

- Run the playbook for ansible : 

.. code-block:: bash

   sudo ansible-playbook playbooks/georchestra.yml

L'installation de l'infrastructure de geOrchestra est faite, il reste à installer un serveur de mail et les scripts de personnalisation pour avoir
l'application fonctionnel et complète pour l'Office de l'eau Réunion.


Erreurs fréquentes 
----------------------------

Si vous avez des erreurs sur sviewer ou htodcs de ce type : 

.. code-block:: bash

   TASK [georchestra : checkout sviewer] *******************************************************************************************************************************************************************************************************
   fatal: [localhost]: FAILED! => {"changed": false, "msg": "Unable to parse submodule hash line: Entrée dans 'lib/ol3'"}

Il faut supprimer repertoire htdocs, parfois 2 fois :

.. code-block:: bash

   rm -r /var/www/georchestra/htdocs

Si vous avez des erreurs de versions de paquets, il faut mettre les bonnes versions, conforme au fichier ``playbooks/georchestra.yml``. 


Serveur mail 
---------------

Pour le serveur mail, pour l'instant un serveur postfix est installé : 

.. code-block:: bash

   sudo apt install postfix 
   sudo systemctl start postfix.service


avec cette configuration dans le fichier /etc/postfix/main.cf : 

.. code-block:: bash

   nano /etc/postfix/main.cf

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

Il y'a trois script bash qui modifient les logos, couleurs et référentiel de coordonée dans le dossier "Configuration" : 

.. code-block:: bash

   cd Configuration
   chmod 777 script remplacement.sh
   chmod 777 other.sh
   chmod 777 last.sh
   ./script_remplacement.sh
   ./other.sh
   ./last.sh


Une fois l'installation terminé, il faudra relancer le datafeeder et le reste de l'infrastructure: 

.. code-block:: bash

   systemctl restart datafeeder.service 


Relancer l'infrastructure
---------------------------

Pour relancer l'infrastructure, il faut relancer les 3 tomcats et potentiellement nginx : 

- sudo systemctl restart tomcat@georchestra.service
- sudo systemctl restart tomcat@geoserver.service
- sudo systemctl restart tomcat@proxycas.service
- sudo systemctl restart nginx

Se rendre sur l'application 
----------------------------------

Pour se rendre sur l'application, aller à l'addresse : 

.. code-block:: bash

   https://le_fqdn_renseigné/