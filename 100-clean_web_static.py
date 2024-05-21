#!/usr/bin/python3
"""
deletes out-of-date archives, using the function do_clean
"""
from fabric.api import *
import os
env.hosts = ['100.26.168.218', '35.175.134.173']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'


def sort_versions(versions):
    """Return sorted versions"""
    return sorted(versions[:])


def delete_versions_local(versions):
    """Deleting from local server"""
    with lcd("versions"):
        [local("rm ./{}".format(version)) for version in versions]


def delete_versions_remote(number=0):
    """Deleting from remote servers"""
    with cd("/data/web_static/releases"):
        versions = run("ls -rt").split()
        versions = [
            version for version in versions if "web_static" in version]
        [versions.pop() for _ in range(number)]
        [run("rm -rf ./{}".format(version)) for version in versions]


def do_clean(number=0):
    """deletes out of date archives"""
    number = 1 if int(number) == 0 else int(number)
    versions = sort_versions(os.listdir("versions"))
    try:
        """ excluding version of this list to save them"""
        [versions.pop() for _ in range(number)]
        delete_versions_local(versions)
        delete_versions_remote(number)
    except BaseException as _:
        pass
