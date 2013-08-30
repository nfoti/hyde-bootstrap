

from fabric.api import *
import fabric.contrib.project as project

remote_dir = '/net/grad/nfoti'
local_dir = 'deploy/'

def clean():
    local('rm -rf ./deploy')


def regen():
    clean()
    local('hyde gen')


def serve():
    local('hyde serve')


def reserve():
    regen()
    serve()


@hosts('nfoti@tahoe.cs.dartmouth.edu')
def deploy():
    regen()
    project.rsync_project(remote_dir=remote_dir,
                          local_dir=local_dir,
                          delete=True
                         )
