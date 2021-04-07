# -*- coding: utf-8 -*-

import time

from functional_tests.features.steps.basic import utils
from functional_tests import settings

from lettuce import step, world

from retrying import retry

DEFAULT_WAIT_TIME_MS = settings.DEFAULT_WAIT_TIME * 1000


@step(u'Dado que estou na tela de "([^"]*)"')
@step(u'Dado que estou na p[áa]gina "([^"]*)"')
@step(u'.* visitar a p[áa]gina "([^"]*)"')
@step(u'.* visito a p[áa]gina "([^"]*)"')
@step(u'.* acesso a p[áa]gina "([^"]*)"')
@step(u'.* acessar a p[áa]gina "([^"]*)"')
@retry(stop_max_delay=DEFAULT_WAIT_TIME_MS, wait_fixed=500)
def eu_estou_em_alguma_url(step, nome):
    utils.pagina_eh_valida(nome)
    world.salva_coverage_browser()
    world.browser.visit(world.base_url + world.pages[nome]['url'])
    time.sleep(world.pages[nome]['delay'])
    utils.pagina_foi_carregada_corretamente()


@step(u'.* atualizo a p[áa]gina')
@step(u'.*atualizar a p[áa]gina')
@retry(stop_max_delay=DEFAULT_WAIT_TIME_MS, wait_fixed=500)
def quando_eu_atualizar_a_pagina(step):
    world.salva_coverage_browser()
    world.browser.visit(world.browser.url)
    time.sleep(2)
    utils.pagina_foi_carregada_corretamente()


@step(u'.* trocar a aba do navegador')
@step(u'.* acessar a nova aba do navegador que foi aberta')
@step(u'.* acesso a nova aba do navegador que foi aberta')
@step(u'.* retornar à aba do navegador')
@step(u'.*alterar a aba do navegador')
def e_alterar_a_aba(step):
    current = world.browser.windows[0]
    world.salva_coverage_browser()
    world.browser.driver.switch_to_window(world.browser.driver.window_handles[1])
    current.close()
    time.sleep(1)
