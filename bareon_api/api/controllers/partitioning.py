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
from bareon_api import models


LOG = utils.getLogger(__name__)


def get_or_404(model, obj_id):
    try:
        return model[obj_id]
    except (IndexError, KeyError):
        pecan.abort(404)


class DisksController(rest.RestController):

    @pecan.expose(template='json')
    def get_one(self, node_id, disk_id):
        node_id = int(node_id)
        # NOTE(prmtl): since this is just a list, lets not
        # force to use ids starting with 0
        disk_id = int(disk_id) - 1
        node_disks = get_or_404(models.DISKS, node_id)
        return get_or_404(node_disks, disk_id)

    @pecan.expose(template='json')
    def get_all(self, node_id):
        node_id = int(node_id)
        return get_or_404(models.DISKS, node_id)


class NodesController(rest.RestController):

    disks = DisksController()

    @pecan.expose(template='json')
    def get_one(self, node_id):
        node_id = int(node_id)
        return get_or_404(models.NODES, node_id)

    @pecan.expose(template='json')
    def put(self, node_id):
        node_id = int(node_id)
        models.NODES[node_id] = pecan.request.json
        return models.NODES[node_id]

    @pecan.expose(template='json')
    def get_all(self):
        return models.NODES.values()
