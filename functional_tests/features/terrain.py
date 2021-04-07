# -*- coding: utf-8 -*-

import os
import json
import ipdb
import random

from lettuce import before, after, world
from splinter.browser import Browser
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from pyvirtualdisplay import Display
from faker import Faker
from functional_tests import settings
from functional_tests.utils import (
    captura_tela, CustomFaker, cria_pasta)
from functional_tests.features.steps.basic.utils import (
    logout_user_se_logado, fecha_modal_se_existir)


def start_webdriver():
    d = DesiredCapabilities.CHROME
    d['loggingPrefs'] = {'browser': 'ALL'}
    world.browser = Browser('chrome', desired_capabilities=d)
    world.browser.wait_time = settings.DEFAULT_WAIT_TIME


def quit_webdriver():
    file = open('/tmp/console.log', 'w')
    for line in world.browser.driver.get_log('browser'):
        file.write("%s\n" % line)
    file.close()
    world.browser.quit()


def delete_emails_files():
    if os.path.isdir(settings.EMAIL_FILE_PATH):
        filelist = [f for f in os.listdir(settings.EMAIL_FILE_PATH)]
        for f in filelist:
            os.remove(settings.EMAIL_FILE_PATH + '/' + f)


def delete_download_files():
    if os.path.isdir(settings.DOWNLOAD_FILE_PATH):
        filelist = [f for f in os.listdir(settings.DOWNLOAD_FILE_PATH)]
        for f in filelist:
            os.remove(settings.DOWNLOAD_FILE_PATH + '/' + f)


def limpa_ambiente():
    logout_user_se_logado()
    fecha_modal_se_existir()
    world.browser.cookies.delete()
    delete_emails_files()
    delete_download_files()
    world.ultimo_email_acessado = None


@world.absorb
def salva_coverage_browser():
    json_coverage = world.browser.evaluate_script('window.__coverage__')
    if json_coverage:
        with open('coverage_browser/{i}.json'.format(i=str(random.randint(0, 99999999999999999999))), 'w') as outfile:
            json.dump(json_coverage, outfile)


@before.all
def initial_setup():
    if settings.BACKGROUND_MODE:
        world.display = Display(visible=0, size=(1024, 1700))
    else:
        world.display = Display(visible=1, size=(1024, 1700))
    world.display.start()

    world.base_url = settings.BASE_URL

    world.pages = settings.PAGES
    world.users = settings.USERS

    world.faker = Faker(settings.LANGUAGE)
    world.faker.add_provider(CustomFaker)
    cria_pasta('coverage_browser')
    cria_pasta('junit')
    cria_pasta(settings.DOWNLOAD_FILE_PATH)

    start_webdriver()


@before.each_feature
def setup_some_feature(feature):
    pass


@before.each_scenario
def initialize_scenario(scenario):
    pass


@before.each_outline
def initialize_outline(scenario, outline):
    pass


@after.each_step
def teardown_some_step(step):
    if step.failed:
        diretorio = 'functional_tests/screenshots/' + step.scenario.feature.name + '/'
        nome_arquivo = step.scenario.name + " - " + step.sentence
        captura_tela(diretorio, nome_arquivo)
        if settings.DEBUG_MODE:
            ipdb.set_trace()


@after.each_outline
def teardown_outline(scenario, outline):
    limpa_ambiente()


@after.each_scenario
def teardown_scenario(scenario):
    limpa_ambiente()


@after.each_feature
def feature_teardown(feature):
    pass


@after.all
def teardown_environment(total):
    world.salva_coverage_browser()
    quit_webdriver()
    world.display.stop()
