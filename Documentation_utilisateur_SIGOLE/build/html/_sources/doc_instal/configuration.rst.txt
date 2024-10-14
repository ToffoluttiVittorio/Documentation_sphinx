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

Les dossiers de configuration se trouve dans : ``/etc/georchestra/``

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

Il est très simple à lire et comprendre :

.. code-block:: bash

   ---
   - name: georchestra deployment
   hosts: localhost
   # note: above host must match the content of the "hosts" file
   become: true
   roles:
      - { role: georchestra, tags: georchestra }
      - { role: elastic.elasticsearch, tags: es }
      - { role: geerlingguy.kibana, tags: kibana }

   vars:

      georchestra_versions:
         # master version
         # datadir: 24.0 # or, see https://github.com/georchestra/datadir/branches
         # debian_repository_url: deb [signed-by=/etc/apt/keyrings/packages.georchestra.org.gpg] https://packages.georchestra.org/debian master main # or 24.0.x
         # georchestra_repository: 24.0.x # see https://github.com/georchestra/georchestra/branches
         # geonetwork_datadir: gn4.2.7 # see https://github.com/georchestra/geonetwork_minimal_datadir/branches
         # geoserver_datadir: 2.25.0 # https://github.com/georchestra/geoserver_minimal_datadir/branches
         # 24.0.x

         datadir: "24.0"
         debian_repository_url: "deb [signed-by=/etc/apt/keyrings/packages.georchestra.org.gpg] https://packages.georchestra.org/debian 24.0.x main"
         georchestra_repository: "24.0.x"
         geonetwork_datadir: "gn4.2.7"
         geoserver_datadir: "24.0"


      java_version: java-17-openjdk-amd64
      tomcat_version: 9
      kibana_server_host: 127.0.0.1
      es_version: 7.17.22
      es_data_dirs:
         - /srv/elasticsearch/data
      es_log_dir: /srv/elasticsearch/logs
      es_config:
         cluster.name: "{{ georchestra.fqdn }}"
         bootstrap.memory_lock: true
      es_heap_size: 1g
      cadastrapp:
         enabled: false
         db:
         name: georchestra
         user: georchestra
         schema: cadastrapp
         pass: georchestra
         qgisdb:
         host: localhost
         port: 5432
         name: georchestra
         user: georchestra
         pass: georchestra
         schema: qadastre
         gitrepo: https://github.com/georchestra/cadastrapp
         gitversion: master
         debsrc:
         path: /data/src/georchestra/cadastrapp/cadastrapp/target/
         pkg: georchestra-cadastrapp_99.master.202108020909~80b14a6-1_all.deb
         host: build.fluela
         workdir: /tmp/cadastrapp/tmp
      # Set here your Github token, which should at least have the 'actions' scope
      github_action_token: secret
      # if deploying an ms2 artifact from gh
      # mapstore: {
      #  enabled: True,
      #  repo: georchestra/mapstore2-georchestra,
      #  artifact_id: 119135632,
      #  artifact_sha256: b2803ecc76a3768fdc5e358f23b5c5ce10b02ddc #git commit hash
      # }
      openldap:
         topdc: georchestra
         basedn: dc=georchestra,dc=org # has to be in the form dc={{ topdc }},dc=xx
         rootdn: cn=admin,dc=georchestra,dc=org
         rootpw: secret
         gitrepo: https://raw.github.com/georchestra/georchestra
         ldifs:
         - bootstrap
         - docker-root/georchestraSchema
         - docker-root/etc/ldap.dist/modules/groupofmembers
         - docker-root/etc/ldap.dist/modules/openssh
         - docker-root/memberof
         - docker-root/lastbind
         - root
         - docker-root/georchestra
         gitversion: "{{ georchestra_versions.georchestra_repository }}"

      georchestra:
         fqdn: georchestra.ole.re
         max_body_size: 100M
         ign_api_key: luvs4p9c4yq5ewfwqcqgm83f # invalid key only used in sviewer
         db:
         name: georchestra
         user: georchestra
         pass: georchestra
         datadir:
         path: /etc/georchestra
         gitrepo: https://github.com/georchestra/datadir
         gitversion: "{{ georchestra_versions.datadir }}"
         debian:
         repo: "{{ georchestra_versions.debian_repository_url }}"
         key: https://packages.georchestra.org/debian/landry%40georchestra.org.gpg.pubkey
      geonetwork:
         db:
         schema: geonetwork
         datadir:
         path: /srv/data/geonetwork/
         gitrepo: https://github.com/georchestra/geonetwork_minimal_datadir
         gitversion: "{{ georchestra_versions.geonetwork_datadir }}"
      geoserver:
         privileged:
         user: geoserver_privileged_user
         pass: gerlsSnFd6SmM
         datadir:
         path: /srv/data/geoserver/
         gitrepo: https://github.com/georchestra/geoserver_minimal_datadir
         gitversion: "{{ georchestra_versions.geoserver_datadir }}"
         wms_srslist:
         - 2154
         - 3857
         - 3942
         - 3943
         - 3944
         - 3945
         - 3946
         - 3947
         - 3948
         - 3949
         - 3950
         - 4171
         - 4258
         - 4326
         - 23030
         - 23031
         - 23032
         - 32630
         - 32631
         - 32632
         - 4171
         - 4271
         - 3758
      geowebcache_datadir: /srv/data/geowebcache/
      tomcat_keystore_pass: tomcatkstp
      tomcat_basedir: /srv/tomcat
      system_locale: en_US.UTF-8
      logs_basedir: /srv/log
      force_https: true # set to false if running behind a reverse proxy that does SSL
      # if running behind a reverse proxy, uncomment/fill so that you get the real client ip in accesslogs
      #reverse_proxy_real_ip: 10.0.0.1
      #reverse_proxy_real_ip_header: X-Forwarded-For
      console_adminemail: admin@example.org
      console_captcha:
         privateKey: ""
         publicKey: ""
      tomcat_instances:
         proxycas:
         port: 8180
         control_port: 8105
         xms: 256m
         xmx: 512m
         georchestra:
         port: 8280
         control_port: 8205
         xms: 1G
         xmx: 2G
         geoserver:
         port: 8380
         control_port: 8305
         xms: 1G
         xmx: 1G
      georchestra_wars:
         analytics:
         pkg: georchestra-analytics
         tomcat: georchestra
         enabled: true
         cas:
         pkg: georchestra-cas
         tomcat: proxycas
         enabled: true
         geonetwork:
         pkg: georchestra-geonetwork
         tomcat: georchestra
         enabled: true
         # mapstore: # using a github action artifact
         #   url: https://api.github.com/repos/{{ mapstore.repo }}/actions/artifacts/{{ mapstore.artifact_id }}/zip
         #   tomcat: georchestra
         #   artifact_sha256: "{{ mapstore.artifact_sha256 }}"
         #   enabled: "{{ mapstore.enabled }}"
         mapstore: # using the package from packages.georchestra.org
         pkg: georchestra-mapstore
         tomcat: georchestra
         enabled: true
         geoserver:
         pkg: georchestra-geoserver
         tomcat: geoserver
         enabled: true
         geowebcache:
         pkg: georchestra-geowebcache
         tomcat: georchestra
         enabled: true
         import:
         pkg: georchestra-datafeeder-ui
         tomcat: georchestra
         enabled: true
         header:
         pkg: georchestra-header
         tomcat: georchestra
         enabled: true
         console:
         pkg: georchestra-console
         tomcat: georchestra
         enabled: true
         cadastrapp:
         pkg: georchestra-cadastrapp
         tomcat: georchestra
         enabled: false
         ROOT:
         pkg: georchestra-security-proxy
         tomcat: proxycas
         enabled: true
      datafeeder:
         enabled: true
         port: 8480
      # not yet, doesnt work standalone ?
      #    cas:
      #      pkg: georchestra-cas
      #      enabled: true
      #      port: 8980
      gn_cloud_searching:
         enabled: true
         port: 8580
         url: https://packages.georchestra.org/bot/wars/geonetwork-microservices/searching.jar
      gn_ogc_api_records:
         enabled: true
         port: 8880
         url: https://packages.georchestra.org/bot/wars/geonetwork-microservices/gn-ogc-api-records.jar
      datahub:
         enabled: true
         url: https://packages.georchestra.org/bot/datahub/datahub.zip
         default_api_url: /geonetwork/srv/api # could be set to any other GeoNetwork catalogue, even remote if CORS allows it
      mviewer:
         enabled: false
         port: 8680
         gitrepo: https://github.com/mviewer/mviewer
         gitversion: master
      mviewerstudio:
         enabled: false
         port: 8780
         gitrepo: https://github.com/mviewer/mviewerstudio
         gitversion: master
      gateway:
         enabled: false
         port: 8980
   tasks:
      - name: reconfigure Kibana after geerlingguy.kibana
         copy:
         src: resources/kibana.yml
         dest: /etc/kibana/kibana.yml
         owner: root
         group: root
         mode: "0644"
         notify: restart kibana

   handlers:
      - name: restart kibana
         service: name=kibana state=restarted

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

Voici les scripts commentés qui sont facile à comprendre et modifier selon les besoins:

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

