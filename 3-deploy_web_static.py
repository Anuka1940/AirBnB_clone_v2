#!/usr/bin/python3
"""
Script to implement deploy to a web server
"""

from os.path import exists
from fabric.api import *
import os.path
from datetime import datetime
from fabric.api import local

env.hosts = ['100.26.168.218', '35.175.134.173']


def deploy():
    "Implements creation of tar file and deploy the project"
    path = do_pack()
    if path:
        do_deploy(path)
    return None


def do_pack():
    """Create the tar gzipped archive."""
    current_date = datetime.now().strftime("%Y%m%d%H%M%S")
    created_file = "versions/web_static_{}.tgz".format(current_date)

    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(created_file)).failed is True:
        return None
    return created_file


def do_deploy(archive_path):
    """Executing function to deploy"""
    if exists(archive_path) is False:
        return False
    try:
        fileEndpoint = archive_path.split("/")[-1]
        name = fileEndpoint.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        """ Creating dir """
        run('mkdir -p {}{}/'.format(path, name))
        """ Executign tar"""
        run('tar -xzf /tmp/{} -C {}{}/'.format(fileEndpoint, path, name))
        """ Deleting tmp file"""
        run('rm /tmp/{}'.format(fileEndpoint))
        """ Moving dir with all content"""
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, name))
        """ Deleting original"""
        run('rm -rf {}{}/web_static'.format(path, name))
        run('rm -rf /data/web_static/current')
        """ Creating S. link"""
        run('ln -s {}{}/ /data/web_static/current'.format(path, name))
        return True
    except Exception:
        return False
