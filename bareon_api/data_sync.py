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


"""
Module implements data synchronization mechanism, it might be
invoked manually using CLI or (TODO) by notification from
discovery service
"""

import six

from bareon_api import models
from bareon_api.models import generate_spaces, get_nodes_and_disks, set_spaces, set_nodes_and_disks

class DataSourceBase(object):

    def sync_all(self):
        raise NotImplemented
        
    def sync_list(self, node_ids):
        raise NotImplemented



class DiscoveryDriver(DataSourceBase):
    """Uses separate service to get discovery information
    """
    def sync_all(self):
        set_spaces(*get_nodes_and_disks())
        set_nodes_and_disks(*generate_spaces(models.NODES, models.DISKS))

    def sync_list(self, node_ids):
        raise NotImplemented


def sync_all_nodes():
    DiscoveryDriver().sync_all()


def sync_list_nodes(node_ids):
    DiscoveryDriver().sync_list(node_ids)


def sync_node(node_id):
    sync_list_nodes([node_id])
