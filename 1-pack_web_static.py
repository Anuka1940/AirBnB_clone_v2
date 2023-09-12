#!/usr/bin/python3
""" A fabric scrip that generates a .tgz archive 
from the contents of the web_static folder using the do_pack function"""
from fabric.api import local
from datetime import datetime

def do_pack():
    try:
        # Create the "version" directory if it doesn't exist
        local("mkdir -p versions")

        # Generate the archive name based on the current date and time
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_name = f"web_static_{timestamp}.tgz"

        # Compress the contents of the "web_static" folder into the archive
        local(f"tar -czvf versions/{archive_name} web_static")

        #Return the path to the created archive
        return f"versions/{archive_name}"
    except Exception:
        return None
