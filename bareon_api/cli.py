# -*- coding: utf-8 -*-

#    Copyright 2015 Mirantis, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import os
import requests
import sys

from paste import deploy
from paste import httpserver

from bareon_api.common import config
from bareon_api.data_sync import sync_all_nodes


current_dir = os.path.dirname(__file__)

CONF = config.CONF


def data_sync():
    resp = requests.post('http://{host}:{port}/v1/actions/sync_all'.format(
        host=CONF.host_ip, port=CONF.port))
    print('Response code {0}'.format(resp.status_code))
    print(resp.text)


def run():
    config.parse_args(CONF, sys.argv[1:])
    sync_all_nodes()

    paste_conf = os.path.join(os.sep, 'etc', 'bareon-api',
                              'bareon-api-paste.ini')

    if not os.path.lexists(paste_conf):
        paste_conf = os.path.join(current_dir, '..', 'etc', 'bareon',
                                  'bareon-api-paste.ini')

    application = deploy.loadapp(
        'config:{paste_conf}'.format(paste_conf=paste_conf),
        name='main',
        relative_to='.')

    httpserver.serve(application, host=CONF.host_ip, port=CONF.port)
