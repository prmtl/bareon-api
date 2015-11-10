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

import logging

from oslo_config import cfg
from oslo_log import log


API_SERVICE_OPTS = [
    cfg.StrOpt('host_ip',
               default='0.0.0.0',
               help='The IP address on which api listens.'),
    cfg.IntOpt('port',
               default=9322,
               min=1, max=65535,
               help='The TCP port on which api listens.'),
]

DISCOVERY_SERVICE_OPTS = [
    cfg.StrOpt('discovery_host_ip',
               default='0.0.0.0',
               help='The IP address on which discovery api listens.'),
    cfg.IntOpt('discovery_port',
               default=8881,
               min=1, max=65535,
               help='The TCP port on which dsiscovry api listens.'),
]

opt_group = cfg.OptGroup(
    name='api',
    title='Options for the api service')


def make_config():
    conf = cfg.ConfigOpts()

    conf.register_group(opt_group)

    conf.register_opts(API_SERVICE_OPTS, opt_group)
    conf.register_cli_opts(API_SERVICE_OPTS)

    conf.register_opts(DISCOVERY_SERVICE_OPTS, opt_group)
    conf.register_cli_opts(DISCOVERY_SERVICE_OPTS)

    log.register_options(conf)
    return conf


def parse_args(conf, args=None):
    import sys

    conf(args=args if args else sys.argv[1:],
         project='bareon-api',
         version='1.0.0')


CONF = make_config()
logging.getLogger(__name__)
parse_args(CONF)
