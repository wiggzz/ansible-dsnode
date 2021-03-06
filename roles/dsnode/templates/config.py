#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import heartbeat

# Flask
DEBUG = False
SECRET_KEY = os.urandom(32)
APPLICATION_ROOT = '/api/downstream/v1'
SERVER_ALIAS = '{{ dsnodehostname }}'

# SQLAlchemy (DB)
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{{ dsnodemysqluser }}:{{ mysqlpassword }}@{{ mysqldbserver }}/{{dsnodemysqldbname}}'  # NOQA

FILES_PATH = '{{ dsnodetmppath }}'
TAGS_PATH = '{{ dsnodetagspath }}'
MMDB_PATH = '{{ dsnodegeodbpath }}'

HEARTBEAT = heartbeat.Merkle.Merkle
HEARTBEAT_PATH = '{{ dsnodeheartbeatpath }}'

MONGO_LOGGING = True
MONGO_URI = 'mongodb://{{dsnodemongodbuser}}:{{mongodbpassword}}@{{mongodbserver}}/{{dsnodemongodbname}}'

MAX_CHUNK_SIZE = 32000
DEFAULT_CHUNK_SIZE = 100
MAX_TOKENS_PER_IP = 5
MIN_SJCX_BALANCE = 10000
MAX_SIG_MESSAGE_SIZE = 1024
REQUIRE_SIGNATURE = False
