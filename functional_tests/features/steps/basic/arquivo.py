# -*- coding: utf-8 -*-

from lettuce import step
from functional_tests import settings

import os.path
from os import listdir

from retrying import retry


@step(u'Então o arquivo "([^"]*)" deve ter sido baixado')
@retry(stop_max_attempt_number=10, wait_fixed=5000, wrap_exception=True)
def entao_o_arquivo_group1_deve_ter_sido_baixado(step, group1):
    full_path = settings.DOWNLOAD_FILE_PATH + group1
    if not os.path.exists(full_path):
        raise Exception(u'Arquivo não encontrado')


@step(u'Então o arquivo que contém "([^"]*)" deve ter sido baixado')
@retry(stop_max_attempt_number=10, wait_fixed=5000, wrap_exception=True)
def entao_o_arquivo_que_contem_group1_deve_ter_sido_baixado(step, group1):
    for filename in listdir(settings.DOWNLOAD_FILE_PATH):
        if group1 in filename:
            assert True
            return
    raise Exception(u'Arquivo não encontrado')
