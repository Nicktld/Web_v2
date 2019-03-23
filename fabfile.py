# fabfile.py
import os, re
from datetime import datetime

# Loading Fabric API:
from fabric.api import *

# Server username
env.user = 'ubuntu'
# sudo user root:
env.sudo_user = 'root'
# Server IPs
env.hosts = ['18.224.48.134']# Use AWS Elastic IPs (static IP pulled from AWS public IPv4 pool)
# SSH
env.key_filename = '~/Downloads/627project.pem'

# Server MySQl username and password
db_user = 'Leon'
db_password = 'tangledong1994'


_TAR_FILE = 'dist-blog.tar.gz'

def build():
    includes = ['static', 'templates', '*.py', 'favicon.ico']
    excludes = ['test', '.*', '*.pyc', '*.pyo']
    local('rm -f dist/%s' % _TAR_FILE)
    with lcd(os.path.join(os.path.abspath('.'), 'www')):
        cmd = ['tar', '--dereference', '-czvf', '../dist/%s' % _TAR_FILE]
        cmd.extend(['--exclude=\'%s\'' % ex for ex in excludes])
        cmd.extend(includes)
        local(' '.join(cmd))

_REMOTE_TMP_TAR = '/tmp/%s' % _TAR_FILE
_REMOTE_BASE_DIR = '/srv/blog'

def deploy():
    newdir = 'www-%s' % datetime.now().strftime('%y-%m-%d_%H.%M.%S')
    # Delete .tar that exists
    run('rm -f %s' % _REMOTE_TMP_TAR)
    # Upload new .tar
    put('dist/%s' % _TAR_FILE, _REMOTE_TMP_TAR)
    # Make new dir
    with cd(_REMOTE_BASE_DIR):
        sudo('mkdir %s' % newdir)
    # Unzip to new dir
    with cd('%s/%s' % (_REMOTE_BASE_DIR, newdir)):
        sudo('tar -xzvf %s' % _REMOTE_TMP_TAR)
    # Reset soft link
    with cd(_REMOTE_BASE_DIR):
        sudo('rm -rf www')
        sudo('ln -s %s www' % newdir)
        sudo('chown ubuntu:ubuntu www')
        sudo('chown -R ubuntu:ubuntu %s' % newdir)
    # Restart python app and nginx
    with settings(warn_only=True):
        sudo('supervisorctl stop blog')
        sudo('supervisorctl start blog')
        sudo('/etc/init.d/nginx reload')
