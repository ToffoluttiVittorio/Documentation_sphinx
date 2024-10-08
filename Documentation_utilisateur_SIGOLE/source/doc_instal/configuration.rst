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

Si vous voulez que les modifications dans ce fichiers s'execute il faut relancer cette commande dans le dossier du clone du repo git: 

.. code-block:: bash

   sudo ansible-playbook playbooks/georchestra.yml

Base de donnée 
------------------------------

La base de donnée est accessible avec psql : 

.. code-block:: bash

   psql -U georchestra -h localhost

Elle stocke les données dans différents schémas. Il n'est pas nécéssaire de l'utiliser.

Relancer l'infrastructure
---------------------------

Pour relancer l'infrastructure, il faut relancer les 3 tomcats et potentiellement nginx : 

- sudo systemctl restart tomcat@georchestra.service
- sudo systemctl restart tomcat@geoserver.service
- sudo systemctl restart tomcat@proxycas.service
- sudo systemctl restart nginx

