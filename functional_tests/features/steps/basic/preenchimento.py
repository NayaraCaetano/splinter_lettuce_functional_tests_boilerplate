# -*- coding: utf-8 -*-

import time

from functional_tests.utils import normalize_string
from functional_tests.features.steps.basic import utils

from lettuce import step, world


# Ações de preenchimento #######################################################

@step(u'.* preencher o campo "([^"]*)" com o valor ("[^"]*")')
@step(u'.* preencho o campo "([^"]*)" com o valor ("[^"]*")')
@step(u'E o campo "([^"]*)" com o valor ("[^"]*")')
@step(u'.* preencher o campo "([^"]*)" com a ("[^"]*")')
@step(u'.* preencho o campo "([^"]*)" com a ("[^"]*")')
@step(u'E o campo "([^"]*)" com a ("[^"]*")')
@step(u'.* preencher o campo "([^"]*)" com o ("[^"]*")')
@step(u'.* preencho o campo "([^"]*)" com o ("[^"]*")')
@step(u'E o campo "([^"]*)" com o ("[^"]*")')
def e_preencho_o_campo_group1_com_o_valor_group2(step, group1, group2):
    elementos = utils.encontrar_elementos_por_funcao_splinter_e_texto(group1, assert_error=True)
    elemento = utils.retorna_apenas_elementos_visiveis(elementos)
    utils.aguarda_loading_e_executa(elemento.fill, value=utils.processa_group(group2)[0])


# Preenchimento de campo search ##########################################

@step(u'.* preencher o campo de search "([^"]*)" com o valor ("[^"]*")')
@step(u'.* preencho o campo de search "([^"]*)" com o valor ("[^"]*")')
@step(u'E o campo de search "([^"]*)" com o valor ("[^"]*")')
@step(u'.* preencher o campo de search "([^"]*)" com a ("[^"]*")')
@step(u'.* preencho o campo de search "([^"]*)" com a ("[^"]*")')
@step(u'E o campo de search "([^"]*)" com a ("[^"]*")')
@step(u'.* preencher o campo de search "([^"]*)" com o ("[^"]*")')
@step(u'.* preencho o campo de search "([^"]*)" com o ("[^"]*")')
@step(u'E o campo de search "([^"]*)" com o ("[^"]*")')
def e_preencho_o_campo_de_search_group1_com_o_valor_group2(step, group1, group2):
    div_campo = utils.encontrar_elementos_por_funcao_splinter_e_texto(group1, assert_error=True)
    utils.aguarda_loading_e_executa(div_campo[0].click)

    busca = normalize_string(utils.processa_group(group2)[0].partition(' ')[0])
    div_campo.find_by_tag('input')[0].type(busca)
    time.sleep(0.1)

    opcao_seletor = u'$(\'[name="{group1}"] .ui-select-choices-row-inner:contains("{group2}")\')'.format(
        group1=group1, group2=utils.processa_group(group2)[0]
    )
    opcao = utils.encontrar_elementos_por_seletor_jquery(opcao_seletor, assert_error=True)
    utils.aguarda_loading_e_executa(opcao[0].click)


# Preenchimento de campo select ##########################################

@step(u'.* preencher o campo de select "([^"]*)" com o valor ("[^"]*")')
@step(u'.* preencho o campo de select "([^"]*)" com o valor ("[^"]*")')
@step(u'E o campo de select "([^"]*)" com o valor ("[^"]*")')
@step(u'.* preencher o campo de select "([^"]*)" com a ("[^"]*")')
@step(u'.* preencho o campo de select "([^"]*)" com a ("[^"]*")')
@step(u'E o campo de select "([^"]*)" com a ("[^"]*")')
@step(u'.* preencher o campo de select "([^"]*)" com o ("[^"]*")')
@step(u'.* preencho o campo de select "([^"]*)" com o ("[^"]*")')
@step(u'E o campo de select "([^"]*)" com o ("[^"]*")')
def e_preencho_o_campo_de_select_group1_com_o_valor_group2(step, group1, group2):
    option = utils.encontrar_option_de_input_por_texto(group1, group2)[0]
    world.browser.select(group1, option.value)


# Seleção de Radio Box ##########################################

@step(u'.* seleciono o "([^"]*)" radio box disponível')
@step(u'.* selecionar o "([^"]*)" radio box disponível')
@step(u'.* selecionei o "([^"]*)" radio box disponível')
def e_checo_o_group1_radio_box_disponivel(step, group1):
    posicao = utils.retorna_numero_do_ordinal(group1)
    elementos = utils.encontrar_elementos_por_funcao_splinter_e_texto('[type="radio"]', tipo='css')
    utils.aguarda_loading_e_executa(elementos[posicao].check)


# Seleção de Check box #############################################

@step(u'.* checar o campo ("[^"]*")')
@step(u'.* checo o campo ("[^"]*")')
def e_checo_o_campo_group1(step, group1):
    utils.aguarda_loading_e_executa(
        utils.encontrar_elementos_por_funcao_splinter_e_texto(utils.processa_group(group1)[0])[0].check
    )


@step(u'.* remover a sele[cç][ãa]o do campo ("[^"]*")')
@step(u'.* removo a sele[cç][ãa]o do campo ("[^"]*")')
def e_removo_a_selecao_do_campo_group1(step, group1):
    utils.encontrar_elementos_por_funcao_splinter_e_texto(utils.processa_group(group1)[0])[0].uncheck()


@step(u'.* checo o campo cuja linha da tabela cont[ée]m: (.+)$')
@step(u'.* checar o campo cuja linha da tabela cont[ée]m: (.+)$')
def e_checo_o_campo_cuja_linha_da_tabela_contem_group1(step, group1):
    elementos = utils.encontrar_elementos_por_x_conteudos('tr', utils.processa_group(group1), ' [type=checkbox]')
    elementos[0].click()
