#!/usr/bin/python3
"""
distributes an archive to your web servers, using the function do_deploy
"""

from os.path import exists
from fabric.api import *
env.hosts = ['23.20.35.69', '35.227.91.66']


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
