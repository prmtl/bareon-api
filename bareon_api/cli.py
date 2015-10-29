import os
import sys
import requests

from paste import deploy
from paste import httpserver

from bareon_api.common.config import CONF
from bareon_api.data_sync import sync_all_nodes


current_dir = os.path.dirname(__file__)


def data_sync():
    resp = requests.post('http://{host}:{port}/v1/actions/sync_all'.format(
        host=CONF.host_ip, port=CONF.port))
    print('Response code {0}'.format(resp.status_code))
    print(resp.text)


def run():
    sync_all_nodes()
    paste_conf = os.path.join(os.sep, 'etc', 'bareon-api', 'bareon-api-paste.ini')
    if not os.path.lexists(paste_conf):
        paste_conf = os.path.join(current_dir, '..', 'etc', 'bareon', 'bareon-api-paste.ini')

    application = deploy.loadapp(
        'config:{paste_conf}'.format(paste_conf=paste_conf),
        name='main',
        relative_to='.')

    httpserver.serve(application, host=CONF.host_ip, port=CONF.port)
