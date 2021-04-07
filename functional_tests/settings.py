# -*- coding: utf-8 -*-

import os

from functional_tests.utils import str2bool

BASE_URL = 'https://'
# Eg. BASE_URL = 'localhost/'

PAGES = {
    u'Google': {'url': u'www.google.com.br/', 'delay': 0},
    u'Uol': {'url': u'www.uol.com.br/', 'delay': 0},
    u'Logout': {'url': u'www.google.com.br/', 'delay': 0},
    u'Login': {'url': u'www.google.com.br/', 'delay': 0}
}


class Usuario(object):

    def __init__(self, username, email, senha):
        self.username = username
        self.email = email
        self.senha = senha


USERS = {
    u'Teste': Usuario(u'teste', u'teste@teste.com.br', u'123456').__dict__,
}

env_backgroud_mode = os.environ.get('TESTS_BACKGROUND_MODE')
env_debug_mode = os.environ.get('TESTS_DEBUG_MODE')

BACKGROUND_MODE = str2bool(env_backgroud_mode) if env_backgroud_mode is not None else False
DEBUG_MODE = str2bool(env_debug_mode) if env_debug_mode is not None else True

EMAIL_FILE_PATH = '/tmp/email-messages'
DOWNLOAD_FILE_PATH = os.environ.get('TESTS_DOWNLOAD_PATH')

DEFAULT_WAIT_TIME = 3

LANGUAGE = 'pt_BR'
