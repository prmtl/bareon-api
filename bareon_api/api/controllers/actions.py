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

import pecan
from pecan import rest

from bareon_api.common import utils
from bareon_api.data_sync import sync_all_nodes


LOG = utils.getLogger(__name__)

class SyncAllController(rest.RestController):

    @pecan.expose(template='json')
    def post(self):
        sync_all_nodes()


class GlobalActionsController(rest.RestController):
    """Global Actions controller"""

    sync_all = SyncAllController()

    @pecan.expose(generic=True)
    def index(self):
        pecan.abort(405)  # HTTP 405 Method Not Allowed as default
