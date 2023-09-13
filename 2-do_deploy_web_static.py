#!/usr/bin/python3
""" Fabric script that distributes an archive to your web servers,
using the function do_deploy"""
from fabric.api import *
import os

# Define the remote servers
env.hosts = ['54.160.93.171', '54.159.27.183']


def do_deploy(archive_path):
    """Define function"""
    if not os.path.exists(archive_path):
        return False

    try:
        put(archive_patch, "/tmp/")
        archive_name = os.path.basename(archive_path)
        archive_name_no_ext = os.path.splitext(archive_name)[0]
        releases_path = "/data/web_static/releases/"

        run("mkdir -p {}{}".format(
                                   release_path,
                                   archive_name_no_ext))
        run("tar -xzf /tmp/{} -C {}{}".format(
                                              archive_name,
                                              releases_path,
                                              archive_name_no_ext))
        # Delete the archive from the /tmp/
        run("rm {}".format(archive_name))
        # Delete the symbolic link /data/web_static/current
        current_path = "/data/web_static/current"
        if exists(current_path):
            run("rm {}".format(current_path))

        # Create a new symbolic link
        run("ln -s {}{} {}".format(
                                   releases_path,
                                   archive_name_no_ext,
                                   current_path))
        return True
    except Exception:
        return False
