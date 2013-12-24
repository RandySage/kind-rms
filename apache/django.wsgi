# From https://library.linode.com/frameworks/django-apache-mod-wsgi/debian-6-squeeze#sph_configure-django-applications-for-wsgi

import os
import sys
import site

BASE_DIR = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
site.addsitedir(os.path.join(BASE_DIR,'env/lib/python2.6/site-packages/'))

sys.path.insert(0, os.path.join(BASE_DIR,'env/lib/python2.6/site-packages/') )
sys.path.insert(0, os.path.join(BASE_DIR,'django_project') )
sys.path.insert(0, os.path.join(BASE_DIR,'django_project', 'django_project') )
sys.path.insert(0, os.path.join(BASE_DIR,'django_project', 'kind') )

#os.environ['PYTHON_EGG_CACHE'] = os.path.join(BASE_DIR,'.python-egg')
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings_production'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()


## For apache - also based off of link at top
# <VirtualHost *:80>
#    ServerName ducklington.org
#    ServerAlias www.ducklington.org
#    ServerAdmin squire@ducklington.org

#    DocumentRoot //public_html

#    WSGIScriptAlias / /path_to_install_folder/apache/django.wsgi
#    <Directory /path_to_install_folder/apache>
#       Order allow,deny
#       Allow from all
#    </Directory>
#    <Directory /path_to_install_folder/static>
#       Order allow,deny
#       Allow from all
#    </Directory>
#    <Directory /path_to_install_folder/media>
#       Order allow,deny
#       Allow from all
#    </Directory>

#    Alias /robots.txt /path_to_install_folder/apache/robots.txt
#    Alias /favicon.ico /path_to_install_folder/apache/favicon.ico
#    Alias /media /path_to_install_folder/media
#    Alias /static /path_to_install_folder/static

#    ErrorLog /path_to_install_folder/logs/error.log
#    CustomLog /path_to_install_folder/logs/access.log combined
# </VirtualHost>
