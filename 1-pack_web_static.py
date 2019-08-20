#!/usr/bin/python3
"""This is a module containing a Fabric script that generates a .tgz archive
from AirBnB.
"""
import tarfile
from fabric.api import *
from datetime import datetime


def do_pack():
    '''This is a function that generates a .tgz archive from
    web_static folder.
    '''
    try:
        date_and_time = datetime.now()
        date_and_time = date_and_time.strftime("%Y%m%d%H%M%S")
        local("mkdir -p versions")
        command = "tar -cvzf versions/web_static_" + date_and_time +\
            ".tzg web_static"
        local(command)
        return "versions/web_static_" + date_and_time + ".tzg"
    except:
        return None


do_pack()