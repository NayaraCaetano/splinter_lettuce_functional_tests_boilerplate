# -*- coding: utf-8 -*-

import re

import time

from functional_tests.features.steps.basic import error_messages
from functional_tests import settings, retries

from lettuce import world

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from retrying import retry

DEFAULT_WAIT_TIME = settings.DEFAULT_WAIT_TIME
DEFAULT_WAIT_TIME_MS = settings.DEFAULT_WAIT_TIME * 1000


def pagina_eh_valida(nome):
    assert world.pages.get(nome) is not None, u'A pagina {nome} nao esta mapeada'.format(nome=nome)


def pagina_foi_carregada_corretamente():
    pass


def usuario_eh_valido(nome):
    assert world.users.get(nome), u'O usuário {nome} nao esta mapeado'.format(nome=nome)


def encontrar_elementos_por_x_conteudos(parent_seletor, conteudos, descendant_seletor, tempo_de_espera=DEFAULT_WAIT_TIME, assert_error=False):
    seletor_inicio = u'$("' + parent_seletor + ''
    seletor_final = u':visible' + descendant_seletor + '")'
    seletor_meio = u''

    for conteudo in conteudos:
        seletor_meio = seletor_meio + u':contains(\'' + conteudo + '\')'

    seletor = seletor_inicio + seletor_meio + seletor_final
    return encontrar_elementos_por_seletor_jquery(seletor, tempo_de_espera, assert_error=assert_error)


def processa_group(super_group):
    r_get_aspas = re.compile('"([^"]*)"')
    groups = r_get_aspas.findall(super_group)
    groups = [group.replace("''", '"') for group in groups]
    group_final = []
    for group in groups:
        group_final.append(group)
    return group_final


def encontrar_links_por_texto(texto, assert_error=False):
    hrefs = [href for href in encontrar_elementos_por_x_conteudos('a', [texto], '') if (href.text.split("\n")[0] == texto)]
    if assert_error and not hrefs:
        raise AssertionError(error_messages.link_nao_encontrado(texto))
    return hrefs


def encontrar_option_de_input_por_texto(input_name, option_text, assert_error=False):
    input = encontrar_elementos_por_funcao_splinter_e_texto(input_name, assert_error=True)
    option = input.find_by_text(processa_group(option_text)[0])
    if not option and assert_error:
        raise AssertionError(error_messages.opcao_nao_encontrada(option_text))
    return option


def encontrar_botoes_por_texto(texto, assert_error=False):
    btns = [btn for btn in world.browser.find_by_css('.btn') if (btn.text == texto or btn.value == texto and btn.visible)]
    if not btns:
        btns = [btn for btn in world.browser.find_by_css('[type=submit]') if (btn.text == texto or btn.value == texto and btn.visible)]
    if not btns:
        btns = encontrar_elementos_por_x_conteudos('.btn', [texto], '')
    if assert_error and not btns:
        raise AssertionError(error_messages.botao_nao_encontrado(texto))
    return btns


def encontrar_elementos_por_funcao_splinter_e_texto(elemento_name, texto='', tipo='name', assert_error=False):
    find_functions = {
        'name': world.browser.find_by_name,
        'css': world.browser.find_by_css,
        'id': world.browser.find_by_id
    }

    elementos = find_functions[tipo](elemento_name)

    if texto:
        elementos_result = []
        for elemento in elementos:
            if texto in elemento.text:
                elementos_result.append(elemento)
    else:
        elementos_result = elementos

    if assert_error and not elementos_result:
        raise AssertionError(error_messages.elemento_nao_encontrado(elemento_name))

    return elementos_result


def encontrar_elementos_por_seletor_jquery(seletor, tempo_de_espera=DEFAULT_WAIT_TIME, assert_error=False):
    tempo_final = tempo_de_espera + time.time()

    while time.time() < tempo_final or tempo_de_espera == 0:
        element = world.browser.evaluate_script(seletor)
        if element:
            return element
        elif tempo_de_espera == 0:
            break

    if assert_error:
        raise AssertionError(error_messages.elemento_nao_encontrado(seletor))
    return []


@retry(retry_on_result=retries.retry_if_result_false, stop_max_delay=DEFAULT_WAIT_TIME_MS, wait_fixed=500)
def aguarda_pagina_ser_carregada(nome):
    pagina_eh_valida(nome)
    pagina_foi_carregada_corretamente()
    current_url = (world.browser.url).split('?')[0]
    full_url = (world.base_url + world.pages[nome]['url'])
    if current_url != full_url:
        return False
    else:
        return True


def retorna_numero_do_ordinal(nome_ordinal):
    if nome_ordinal == 'primeiro':
        return 0
    if nome_ordinal == 'segundo':
        return 1
    if nome_ordinal == 'terceiro':
        return 2
    if nome_ordinal == 'quarto':
        return 3
    if nome_ordinal == 'quinto':
        return 4
    if nome_ordinal == 'sexto':
        return 5
    if nome_ordinal == u'sétimo':
        return 6
    if nome_ordinal == 'oitavo':
        return 7
    if nome_ordinal == 'nono':
        return 8
    if nome_ordinal == u'décimo':
        return 9
    raise AssertionError(u'Ordinal {nome_ordinal} não reconhecido'.format(nome_ordinal=nome_ordinal))


@retry(stop_max_delay=DEFAULT_WAIT_TIME_MS, wait_fixed=500)
def aguarda_loading_e_executa(funcao, **kwargs):
    return funcao(**kwargs)


def retorna_apenas_elementos_visiveis(elementos_lista, assert_error=False):
    splinter_class = 'splinter.driver.webdriver.WebDriverElement object'

    for elemento in elementos_lista:
        if splinter_class in elemento.__str__() and not elemento.visible:
            elementos_lista.remove(elemento)
        elif splinter_class not in elemento.__str__() and not elemento.is_displayed():
            elementos_lista.remove(elemento)
    if assert_error and not elementos_lista:
        raise AssertionError(error_messages.elemento_nao_encontrado('Nenhum elemento visivel'))
    return elementos_lista


def elemento_encontra_se_desabilitado(elemento):
    try:
        disabled_readonly = True if (elemento['readonly'] and 'true' in elemento['readonly']) else False
        disabled_disabled = True if (elemento['disabled'] and 'true' in elemento['disabled']) else False
        disabled_disabled = disabled_disabled or elemento.has_class("disabled")
    except TypeError:
        disabled_readonly = True if elemento.get_attribute('readonly') else False
        disabled_disabled = True if elemento.get_attribute('disabled') else False

    return disabled_readonly or disabled_disabled


def fecha_modal_se_existir():
    no_wait = WebDriverWait(world.browser.driver, 0)

    try:
        no_wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'close')))
        world.browser.find_by_css('.close').click()
        time.sleep(0.5)
    except:
        pass

    try:
        no_wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'modal-footer')))
        world.browser.find_by_css('.modal-content .btn.btn-link.ng-binding').click()
        time.sleep(0.5)
    except:
        pass


def logout_user_se_logado():
    try:
        world.salva_coverage()
    except:
        pass
    world.browser.visit(world.base_url + settings.PAGES.get('Logout').get('url'))
    try:
        if world.browser.evaluate_script('$(".modal-dialog")'):
            world.browser.visit(world.base_url + settings.PAGES.get('Login').get('url'))
    except:
        pass
    aguarda_pagina_ser_carregada(u'Login')
