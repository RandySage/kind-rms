#!/usr/bin/env python

import subprocess

try:
    with open('./env/bin/pip'):
        subprocess.call("./env/bin/pip install -r requirements.txt",shell=True)
except IOError:
    print '''
Unable to pen ./env/bin/pip - did you run:
  virtualenv env
???
'''


print '''


This should be cleaned up to follow standard setup.py paradigms

Also, run following to set up an admin user:
   ./env/bin/python django_project/manage.py createsuperuser
'''

# from setuptools import setup, find_packages
# DESCRIPTION = ("DOORS'-style Requirements Management System - KIND Is Not DOORS")

# setup(
#     name='KIND',
#     version='0.0-dev',
#     description=DESCRIPTION,
#     url='https://github.com/ransage/kind',
#     packages=['django_project'],
#     install_requires=['setuptools'],
#     tests_require=['nose'],
#     test_suite='src'
# )
