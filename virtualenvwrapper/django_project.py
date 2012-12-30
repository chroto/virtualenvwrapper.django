#!/usr/bin/env python
"""
Create a Django project with virtualenvwrapper
"""

import logging
import subprocess
import os

log = logging.getLogger('virtualenvwrapper.django')


def template(args):
    project = args[0]
    DJANGO_TEMPLATE = os.getenv('DJANGO_TEMPLATE', '')
    requirements = os.path.join(DJANGO_TEMPLATE, 'requirements.txt')
    pip_args = [
        'pip',
        'install'
    ]
    if os.path.exists(requirements):
        pip_args.extend(['-r', requirements])
    else:
        pip_args.append('Django')
    subprocess.check_call(pip_args)
    start_project_args = [
        'django-admin.py',
        'startproject',
        project
    ]
    if DJANGO_TEMPLATE != '':
        start_project_args.append('--template=%s' % DJANGO_TEMPLATE)
    subprocess.check_call(args)
