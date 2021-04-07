# -*- coding: utf-8 -*-

import time

from lettuce import step, world

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from functional_tests.features.steps.basic import utils, error_messages


@step(u'.* aguardo "([^"]*)" segundos')
@step(u'.* aguardar "([^"]*)" segundos')
@step(u'.* aguardo "([^"]*)" segundo')
@step(u'.* aguardar "([^"]*)" segundo')
def e_aguardo_group1_segundos(step, group1):
    time.sleep(int(group1))


@step(u'.* aguardo o carregamento da p[áa]gina')
@step(u'.* aguardar o carregamento da p[áa]gina')
def e_aguardo_o_carregamento_da_pagina(step):
    time.sleep(0.5)


@step(u'E aguardo o elemento de css "([^"]*)" desaparecer')
def e_aguardo_o_elemento_de_css_group1_desaparecer(step, group1):
    WebDriverWait(world.browser.driver, 60).until(
        EC.invisibility_of_element_located(
            (By.CSS_SELECTOR, group1)
        )
    )


@step(u'Então o campo que indica DDI no form deve conter o valor ("[^"]*")')
def entao_o_campo_que_indica_ddi_no_form_deve_conter_o_valor_valor(step, group1):
    existe = utils.encontrar_elementos_por_x_conteudos('.input-group-addon', utils.processa_group(group1)[0], '')
    assert existe, error_messages.elemento_nao_encontrado(group1)


@step(u'.* ativei o recaptcha')
@step(u'.* ativo o recaptcha')
@step(u'.* ativar o recaptcha')
def e_ativei_o_recaptcha(step):
    step.given(u'E checo o campo "captchaResponse"')
    step.given(u'E aguardo o carregamento da página')
