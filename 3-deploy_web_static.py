#!/usr/bin/python3
"""
Fabric script that creates and distributes an archive to me web servers,
using the function deploy"""

from fabric.api import *
from datetime import datetime
import os


env.hosts = ['54.160.93.171', '54.159.27.183']


def do_pack():
    """Define the do_pack function"""
    try:
        local("mkdir -p versions")
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_name = f"web_static_{timestamp}.tgz"
        local(f"tar -czvf versions/{archive_name} web_static")
        return f"versions/{archive_name}"
    except Exception:
        return None


def do_deploy(archive_path):
    """Define the do_deploy function"""
    if not os.path.exists(archive_path):
        return False
    try:
        put(archive_path, "/tmp/")
        archive_name = os.path.basename(archive_name)
        archive_name_no_ext = os.path.splitext(archive_name)[0]
        releases_path = "/data/web_static/releases/"

        run("mkdir -p {}{}".format(releases_path, archive_name))
        run("tar -xzf /tmp/{} -C {}{}".format(
                                              archive_name,
                                              releases_path,
                                              archive_name_no_ext))
        run("rm /tmp/{}".format(archive_name))
        current_path = "/data/web_static/current"
        if exists(current_path):
            run("rm {}".format(current))

        run("ln -s {}{} {}".format(
                                   releases_path,
                                   archive_name_no_ext,
                                   current_path))
        return True
    except Exception:
        return False


def deploy():
    archive_path = do_pack()
    if not archive_path:
        return False

    return do_deploy(archive_path)
