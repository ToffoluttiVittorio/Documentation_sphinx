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

- Clone the source, le code est issue du repo "ansible" de georchestra :

.. code-block:: bash

   sudo apt install git
   sudo git clone https://github.com/ToffoluttiVittorio/ansible.git
   

- Aller dans le répertoire du repo git, toutes les commandes de cette partie se lance à partir de ce repertoire si non spécifié :

.. code-block:: bash
   
   cd ansible

- Installer les rôles de GeoNetwork :

.. code-block:: bash

   sudo ansible-galaxy install -r requirements.yaml
   sudo chmod -777 chemin/vers/ansible/roles/

- Ajouter les clés manquantes (clés pour les applications): 

.. code-block:: bash

   sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 0E98404D386FA1D9
   sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 6ED0E7B82643E131
   sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 605C66F00D6C9793

- Run the playbook for ansible : 

.. code-block:: bash

   sudo ansible-playbook playbooks/georchestra.yml

L'installation de l'infrastructure de geOrchestra est faite, il reste à installer un serveur de mail et les scripts de personnalisation pour avoir
l'application fonctionnel et complète pour l'Office de l'eau Réunion.


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

   smtpd_relay_restrictions = permit_mynetworks permit_sasl_authenticated defer_unauth_destination
   myhostname = Ansible-42.myguest.virtualbox.org
   alias_maps = hash:/etc/aliases
   alias_database = hash:/etc/aliases
   mydestination = $myhostname, localhost, localhost.$mydomain, mail.$mydomain, www.$mydomain, localhost, $mydomain
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

Voici les scripts commenté :

.. code-block:: bash

   #!/bin/bash

   # Mise à jour du fichier de propriétés pour le changement de langue
   echo "Remplacement de 'language=en' par 'language=fr' dans le fichier de propriétés..."
   sed -i 's/language=en/language=fr/' /etc/georchestra/default.properties
   echo "Mise à jour du fichier de propriétés terminée."

   # Mise à jour du fichier de propriétés pour le changement d'URL du logo
   echo "Remplacement de l'URL du logo dans le fichier de propriétés..."
   sed -i 's|logoUrl=https://www.georchestra.org/public/georchestra-logo.svg|logoUrl=https://raw.githubusercontent.com/ToffoluttiVittorio/ansible/master/Configuration/georchestra-logo.svg|' /etc/georchestra/default.properties
   echo "Mise à jour de l'URL du logo terminée."

   # Remplacement de l'URL de la feuille de style commentée dans le fichier de propriétés
   echo "Remplacement de l'URL de la feuille de style commentée dans le fichier de propriétés..."
   sed -i 's|# georchestraStylesheet=http://my-domain-name/stylesheet.css|georchestraStylesheet=./stylesheet.css|' /etc/georchestra/default.properties
   echo "Mise à jour de l'URL de la feuille de style terminée."

   # Activation des analytics dans le fichier de propriétés
   echo "Activation des analytics dans le fichier de propriétés..."
   sed -i 's/analyticsEnabled=false/analyticsEnabled=true/' /etc/georchestra/default.properties
   echo "Activation des analytics terminée."

   # Mise à jour de la timezone dans le fichier de propriétés
   echo "Remplacement de la timezone dans le fichier de propriétés..."
   sed -i 's|#localTimezone=Europe/Paris|localTimezone=Indian/Reunion|' /etc/georchestra/analytics/analytics.properties
   echo "Mise à jour de la timezone terminée."

   # Traduction des valeurs de orgTypeValues dans le fichier de propriétés
   echo "Remplacement des valeurs de orgTypeValues par leur traduction en français..."
   sed -i 's/orgTypeValues=Association,Company,NGO,Individual,Other/orgTypeValues=Association,Entreprise,ONG,Individu,Autre/' /etc/georchestra/console/console.properties
   echo "Traduction des valeurs de orgTypeValues terminée."

.. code-block:: bash

   #!/bin/bash

   # Vérifier si la nouvelle projection existe déjà dans le fichier JSON et ajouter si elle n'existe pas
   echo "Vérification et ajout de la nouvelle entrée à la liste 'projections' dans le fichier JSON..."
   if ! grep -q '"value": "EPSG:2975"' /etc/georchestra/datafeeder/frontend-config.json; then
      sed -i '/"projections": \[/a \
      {\
         "label": "RGR92 / UTM zone 40S",\
         "value": "EPSG:2975"\
      },' /etc/georchestra/datafeeder/frontend-config.json
      echo "Nouvelle entrée ajoutée à la liste 'projections'."
   else
      echo "La projection 'EPSG:2975' existe déjà dans la liste 'projections'."
   fi

   echo "Mise à jour du fichier JSON terminée."

   # Remplacement des valeurs dans le fichier XML
   echo "Remplacement de 'codeListValue=\"eng\"' par 'codeListValue=\"fre\"' dans le fichier XML de datafeeder"
   sed -i 's/codeListValue="eng"/codeListValue="fre"/g' /etc/georchestra/datafeeder/metadata_template.xml
   echo "Remplacement dans le fichier XML terminé."

   # Suppression du fichier header_bg.web et copie du fichier header_bg.webp
   echo "Suppression du fichier header_bg.web et copie du fichier header_bg.webp..."
   rm -f /etc/georchestra/datahub/assets/img/header_bg.web
   cp header_bg.webp /etc/georchestra/datahub/assets/img/
   echo "Fichier header_bg.web remplacé par header_bg.webp."

   # Remplacement dans le fichier TOML pour les langues
   echo "Remplacement de '# languages = ['en', 'fr', 'de']' par 'languages = ['en', 'fr', 'de']' dans le fichier TOML..."
   sed -i "s/# languages = \['en', 'fr', 'de'\]/languages = \['en', 'fr', 'de'\]/" /etc/georchestra/datahub/conf/default.toml
   echo "Remplacement dans le fichier TOML terminé."

   # Remplacement de la couleur primaire dans le fichier TOML
   echo "Remplacement de 'primary_color = \"#85127e\"' par 'primary_color = \"#0a397f\"' dans le fichier TOML..."
   sed -i 's/primary_color = "#85127e"/primary_color = "#0a397f"/' /etc/georchestra/datahub/conf/default.toml
   echo "Remplacement de la couleur primaire dans le fichier TOML terminé."

   # Remplacement de la couleur secondaire dans le fichier TOML
   echo "Remplacement de 'secondary_color = \"#1b1f3b\"' par 'secondary_color = \"#225ea8\"' dans le fichier TOML..."
   sed -i 's/secondary_color = "#1b1f3b"/secondary_color = "#225ea8"/' /etc/georchestra/datahub/conf/default.toml
   echo "Remplacement de la couleur secondaire dans le fichier TOML terminé."

   # Suppression du commentaire et activation de la ligne dans le fichier TOML
   echo "Remplacement de '# enabled = true' par 'enabled = true' pour activer le % de qualité de métadonnée"
   sed -i 's/# enabled = true/enabled = true/' /etc/georchestra/datahub/conf/default.toml
   echo "Activation de la ligne dans le fichier TOML terminée."

   # Suppression des sections 'en' et 'it' dans le fichier JSON
   #echo "Suppression des sections 'en' et 'it' dans le fichier JSON..."
   #sed -i '/"en": {/,/},/d' /etc/georchestra/mapstore/configs/localConfig.json
   #sed -i '/"it": {/,/},/d' /etc/georchestra/mapstore/configs/localConfig.json
   #echo "Suppression des sections terminée."

   # Vérifier si la nouvelle projection existe déjà dans la section 'projectionDefs' et ajouter si elle n'existe pas
   echo "Vérification et ajout de la nouvelle projection à la section 'projectionDefs'..."
   if ! grep -q '"code": "EPSG:2975"' /etc/georchestra/mapstore/configs/localConfig.json; then
      sed -i '/"projectionDefs": \[/a \
         "code": "EPSG:2975",\
         "def": "+proj=lcc +lat_1=48.5 +lat_2=49.5 +lat_0=48.0 +lon_0=-123.0 +x_0=1000000 +y_0=0 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs",\
         "extent": [-600000, 1500000, 1200000, 5000000],\
         "worldExtent": [-130, 24, -66, 49]\
      },{' /etc/georchestra/mapstore/configs/localConfig.json
      echo "Nouvelle projection ajoutée à la section 'projectionDefs'."
   else
      echo "La projection 'EPSG:2975' existe déjà dans la section 'projectionDefs'."
   fi

   echo "Mise à jour du fichier terminé."

.. code-block:: bash

   #!/bin/bash

   # Copier le fichier stylesheet.css dans les répertoires de destination
   echo "Copie du fichier stylesheet.css dans les répertoires de destination..."

   # Répertoires de destination
   DESTINATIONS=(
   "/var/www/georchestra/htdocs/datahub/"
   "/srv/tomcat/georchestra/webapps/analytics/"
   "/srv/tomcat/proxycas/webapps/cas/WEB-INF/classes/static/"
   "/srv/tomcat/georchestra/webapps/console/account/"
   )

   # Boucle pour copier le fichier dans chaque répertoire
   for DEST in "${DESTINATIONS[@]}"; do
   cp ./stylesheet.css "$DEST"
   echo "Fichier stylesheet.css copié avec succès dans $DEST."
   done

   # Remplacement des couleurs dans le fichier CSS
   echo "Remplacement des couleurs dans le fichier cas.css"
   # Remplacer #540069 par #0a397f
   sed -i 's/#540069/#0a397f/g' "/srv/tomcat/proxycas/webapps/cas/WEB-INF/classes/static/themes/georchestra/css/cas.css"
   # Remplacer #720e9e par #0a397f
   sed -i 's/#720e9e/#0a397f/g' "/srv/tomcat/proxycas/webapps/cas/WEB-INF/classes/static/themes/georchestra/css/cas.css"
   # Remplacer #845490 par #225ea8
   sed -i 's/#845490/#225ea8/g' "/srv/tomcat/proxycas/webapps/cas/WEB-INF/classes/static/themes/georchestra/css/cas.css"
   echo "Remplacement des couleurs terminé."

   # Remplacement des valeurs de langue dans le fichier JSP
   #echo "Remplacement des valeurs de langue dans le fichier JSP..."

   # Remplacer lang = forcedLang par lang = "fr"
   #sed -i 's/lang = forcedLang/lang = "fr"/g' "/srv/tomcat/georchestra/webapps/analytics/WEB-INF/jsp/index.jsp"

   # Remplacer lang = detectedLanguage par lang = "fr"
   #sed -i 's/lang = detectedLanguage/lang = "fr"/g' "/srv/tomcat/georchestra/webapps/analytics/WEB-INF/jsp/index.jsp"

   #echo "Remplacement des valeurs de langue terminé."

   # Changement de couleurs dans le css de mapstore
   echo "Changement de couleurs dans le css de mapstore"
   sed -i 's/#85127e/#0a397f/g' /srv/tomcat/georchestra/webapps/mapstore/dist/themes/default.css

   echo "Changement de couleurs dans le css de mapstore terminé."


   # Changement du header de datahub
   echo "Changement du header de datahub"
   # Chemin vers votre fichier HTML
   file="/var/www/georchestra/htdocs/datahub/index.html"

   # Attributs à vérifier
   attr_check="lang='fr' stylesheet='./stylesheet.css' logo-url='./georchestra-logo.svg'"

   # Vérifier si la balise <geor-header> avec les attributs existe déjà
   if grep -q "<geor-header.*$attr_check.*>" "$file"; then
   echo "Les attributs existent déjà dans la balise <geor-header>."
   else
   echo "Les attributs n'existent pas. Ajout en cours..."
   # Commande sed pour ajouter les attributs
   sed -i "s/<geor-header active-app='datahub' legacy-header='false' legacy-url='\/header\/' style='height:90px'>/<geor-header active-app='datahub' legacy-header='false' legacy-url='\/header\/' lang='fr' stylesheet='.\/stylesheet.css' logo-url='.\/georchestra-logo.svg' style='height:90px'>/g" "$file"
   echo "Les attributs ont été ajoutés."
   fi

   #Ajout du logo pour le header de datahub
   echo "Ajout du logo pour le header de datahub"
   cp ./georchestra-logo.svg /var/www/georchestra/htdocs/datahub/
   echo "Ajout du logo pour le header de mapstore terminé"

   #Changement du favicon 
   echo "Remplacement du favicon" 
   rm /var/www/georchestra/htdocs/favicon.ico
   cp ./favicon.ico /var/www/georchestra/htdocs/favicon.ico
   echo "Ramplacement du favicon" 

   #Changement des couleurs de mapstore 
   echo "Changement des couleurs pour mapstore"
   sed -i 's/#6f0f69/#0a397f/g' /srv/tomcat/georchestra/webapps/mapstore/dist/themes/default.css
   sed -i 's/#ed76e5/#0a397f/g' /srv/tomcat/georchestra/webapps/mapstore/dist/themes/default.css
   sed -i 's/#df1ed3/#0a397f/g' /srv/tomcat/georchestra/webapps/mapstore/dist/themes/default.css
   sed -i 's/#708/#0a397f/g' /srv/tomcat/georchestra/webapps/mapstore/dist/themes/default.css
   sed -i 's/#d97fff/#0a397f/g' /srv/tomcat/georchestra/webapps/mapstore/dist/themes/default.css
   sed -i 's/#6e296a/#0a397f/g' /srv/tomcat/georchestra/webapps/mapstore/dist/themes/default.css
   sed -i 's/#800080/#0a397f/g' /srv/tomcat/georchestra/webapps/mapstore/dist/themes/default.css
   sed -i 's/#b218a9/#0a397f/g' /srv/tomcat/georchestra/webapps/mapstore/dist/themes/default.css
   sed -i 's/#610/#0a397f/g' /srv/tomcat/georchestra/webapps/mapstore/dist/themes/default.css
   sed -i 's/#d5c/#0a397f/g' /srv/tomcat/georchestra/webapps/mapstore/dist/themes/default.css
   sed -i 's/#8e1387/#0a397f/g' /srv/tomcat/georchestra/webapps/mapstore/dist/themes/default.css
   sed -i 's/#7c1175/#0a397f/g' /srv/tomcat/georchestra/webapps/mapstore/dist/themes/default.css
   sed -i 's/#42093e/#0a397f/g' /srv/tomcat/georchestra/webapps/mapstore/dist/themes/default.css
   sed -i 's/#150314/#0a397f/g' /srv/tomcat/georchestra/webapps/mapstore/dist/themes/default.css
   sed -i 's/#390836/#0a397f/g' /srv/tomcat/georchestra/webapps/mapstore/dist/themes/default.css
   sed -i 's/#4f0b46/#0a397f/g' /srv/tomcat/georchestra/webapps/mapstore/dist/themes/default.css
   sed -i 's/#680c63/#0a397f/g' /srv/tomcat/georchestra/webapps/mapstore/dist/themes/default.css
   sed -i 's/#73106d/#0a397f/g' /srv/tomcat/georchestra/webapps/mapstore/dist/themes/default.css
   sed -i 's/#73106d/#0a397f/g' /srv/tomcat/georchestra/webapps/mapstore/dist/themes/default.css
   echo "Changement des couleur terminés" 

   # Copie du favicon.png dans le repertoire de geonetwork
   echo "Copie du favicon.png dans le repertoire de geonetwork"
   cp ./favicon.png /srv/data/geonetwork/data/resources/images/logos/
   echo "Copie du favicon.png dans le repertoire de geonetwork terminé"

   # Vérification et ajout des redirections
   echo "Vérification des redirections"

   # Vérifiez si le pattern existe déjà dans le fichier
   if ! grep -q 'Redirect the stylesheet' /etc/nginx/sites-available/georchestra; then
      # Ajouter les redirections juste avant la dernière occurrence du pattern spécifique
      sed -i '/# redirect default to datahub/i \
         # Redirect the stylesheet.css url of geoserver to something known\
         location /geoserver/web/wicket/bookmarkable/stylesheet.css {\
               alias /etc/georchestra/stylesheet.css;\
         }\
         # Same for another url\
         location /geoserver/web/stylesheet.css {\
               alias /etc/georchestra/stylesheet.css;\
         }\
         # Redirect the stylesheet.css url of geonetwork to something known\
         location ~ ^/geonetwork/.*/.*/stylesheet\\.css$ {\
               alias /etc/georchestra/stylesheet.css;\
         }\
         # Redirect the stylesheet.css of the console admin account url to something known\
         location /console/account/stylesheet.css {\
               alias /etc/georchestra/stylesheet.css;\
         }\
         # Redirect the stylesheet.css of the console admin manager url to something known\
         location /console/manager/stylesheet.css {\
               alias /etc/georchestra/stylesheet.css;\
         }\
         ' /etc/nginx/sites-available/georchestra

      echo "Les redirections ont été ajoutées"
   else
      echo "Les redirections ont déjà été ajoutées"
   fi
   echo "Mise à jour des redirections terminée."