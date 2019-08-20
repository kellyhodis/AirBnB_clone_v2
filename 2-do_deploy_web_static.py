#!/usr/bin/python3
"""This is a module containing a Fabric script that generates a .tgz archive
from AirBnB.
"""
from fabric.api import *
from datetime import datetime


env.hosts = ['35.229.123.177', '34.73.72.195']
def do_pack():
    '''This is a function that generates a .tgz archive from
    web_static folder.
    '''
    date_time = datetime.now()
    date_time = date_time.strftime("%Y%m%d%H%M%S")
    local("mkdir -p versions")
    command = "tar -cvzf versions/web_static_" + date_time + ".tzg web_static"
    tar = local(command)
    if tar.succeeded:
        return "versions/web_static_" + date_time + ".tzg"
    else:
        return None


def do_deploy(archive_path):
    '''This is a function that distributes an archive to web servers.
    '''
    if not archive_path:
        return False
    try:
        archive_file = archive_path[9:]
        archive = archive_file[:-4]
        put(archive_path, '/tmp/')
        run('mkdir -p /data/web_static/releases/' + archive)
        run('tar -xzf /tmp/' + archive_file + ' -C /data/web_static/releases/'
            + archive + '/')
        run('rm /tmp/' + archive_file)
        run('mv /data/web_static/releases/' + archive + '/web_static/* ' +
            '/data/web_static/releases/' + archive + '/')
        run('rm -rf /data/web_static/releases/' + archive + '/web_static')
        run('rm -rf /data/web_static/current')
        run('ln -s /data/web_static/releases/' + archive + 
            '/data/web_static_current')
        return True
    except:
        return False 

