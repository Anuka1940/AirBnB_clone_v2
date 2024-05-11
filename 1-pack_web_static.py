#!/usr/bin/python3
"""
Fabric script to distribute an archive to web servers using do_deploy function
"""
from fabric.api import *
from os.path import exists

env.hosts = ['100.26.168.218', '35.175.134.173']  # Replace with your server IPs
env.user = 'ubuntu'  # Replace with your SSH username
env.key_filename = '~/.ssh/id_rsa'  # Replace with your SSH private key path


def do_deploy(archive_path):
    """
    Distributes an archive to web servers
    """
    if not exists(archive_path):
        return False

    try:
        put(archive_path, "/tmp/")
        filename = archive_path.split("/")[-1].split(".")[0]
        run("mkdir -p /data/web_static/releases/{}/".format(filename))
        run("tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/"
            .format(filename, filename))
        run("rm /tmp/{}.tgz".format(filename))
        run("mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/"
            .format(filename, filename))
        run("rm -rf /data/web_static/releases/{}/web_static".format(filename))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(filename))
        return True
    except Exception as e:
        return False

