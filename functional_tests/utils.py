# -*- coding: utf-8 -*-
import os
import unicodedata
import random

from lettuce import world

from faker.providers import BaseProvider


def captura_tela(diretorio, nome_arquivo):
    diretorio = normalize_string(diretorio)
    nome_arquivo = normalize_string(nome_arquivo)
    nome_arquivo = nome_arquivo.replace('/', '_')

    imagem = diretorio + nome_arquivo + '.png'

    cria_pasta(diretorio)

    world.browser.driver.save_screenshot(imagem)


def normalize_string(string):
    return unicodedata.normalize('NFKD', string).encode('ASCII', 'ignore')


def cria_pasta(folder):
    if not os.path.isdir(folder):
        os.makedirs(folder)
    assert os.path.isdir(folder), u'Ocorreu algum problema ao criar a pasta'


def str2bool(v):
    return v.lower() in ("yes", "true", "t", "1")


class CustomFaker(BaseProvider):

    def unique_cnpj_valid(self):
        return random.sample([
            '16.670.085/0001-55',
            '90.400.888/0001-42',
            '90.400.888/0002-23',
            '90.400.888/0003-04',
            '90.400.888/0005-76',
            '48.077.556/0116-51',
            '48.077.556/0165-30',
            '61.012.019/0609-86',
            '05.054.929/0056-90',
            '05.054.929/0057-71',
            '05.054.929/0058-52',
            '92.667.948/0040-20',
            '44.023.661/0001-08',
            '10.775.286/0042-09',
            '75.858.506/0040-41'
        ], 1)[0]
