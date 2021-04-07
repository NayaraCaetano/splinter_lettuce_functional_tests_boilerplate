# -*- coding: utf-8 -*-

from functional_tests.features.steps.basic import utils

from lettuce import step


@step(u'.* clicar no link "([^"]*)"$')
@step(u'.* clico no link "([^"]*)"$')
@step(u'.* cliquei no link "([^"]*)"$')
def e_clico_no_link_group1(step, group1):
    hrefs = utils.encontrar_links_por_texto(group1, assert_error=True)
    utils.aguarda_loading_e_executa(hrefs[0].click)


@step(u'.* clico em "([^"]*)"$')
@step(u'.* clicar em "([^"]*)"$')
def e_clicar_em_group1(step, group1):
    group = [group1]
    elementos = utils.encontrar_elementos_por_x_conteudos('', group, '', assert_error=True)
    utils.aguarda_loading_e_executa(elementos[0].click)


@step(u'.* clicar na aba "([^"]*)"')
@step(u'.* clico na aba "([^"]*)"')
@step(u'.* cliquei na aba "([^"]*)"')
def e_clicar_na_aba_aba(step, group1):
    step.given(u'E clico no elemento resultado do seletor ".lead:contains(\'{group1}\')"'.format(group1=group1))


@step(u'.* clicar no bot[ãa]o "([^"]*)"$')
@step(u'.* clico no bot[ãa]o "([^"]*)"$')
@step(u'.* cliquei no bot[ãa]o "([^"]*)"$')
@step(u'.* cliquei no bot[ãa]o de nome "([^"]*)"$')
@step(u'.* clicar no bot[ãa]o de nome "([^"]*)"$')
@step(u'.* clico no bot[ãa]o de nome "([^"]*)"$')
def e_clico_no_botao_group1(step, group1):
    btns = utils.aguarda_loading_e_executa(utils.encontrar_botoes_por_texto, texto=group1, assert_error=True)
    utils.aguarda_loading_e_executa(btns[0].click)


@step(u'.* clicar no elemento resultado do seletor "([^"]*)"')
@step(u'.* clico no elemento resultado do seletor "([^"]*)"')
def e_clico_no_elemento_resultado_do_seletor(step, group1):
    elementos = utils.encontrar_elementos_por_seletor_jquery('$("' + group1 + '")', assert_error=True)
    elementos = utils.retorna_apenas_elementos_visiveis(elementos, assert_error=True)
    utils.aguarda_loading_e_executa(elementos[0].click)


@step(u'.* clico no elemento de seletor "([^"]*)" presente na linha da tabela que cont[ée]m: (.+)$')
@step(u'.* clicar no elemento de seletor "([^"]*)" presente na linha da tabela que cont[ée]m: (.+)$')
@step(u'.* clico no elemento de seletor "([^"]*)" presente na linha da tabela que cont[ée]m (.+)$')
@step(u'.* clicar no elemento de seletor "([^"]*)" presente na linha da tabela que cont[ée]m (.+)$')
def e_clico_no_botao_de_nome_group1_presente_na_linha_da_tabela_que_contem_group2(step, group1, group2):
    elementos = utils.encontrar_elemento_por_x_conteudos('tr', utils.processa_group(group2), group1, assert_error=True)
    utils.aguarda_loading_e_executa(elementos[0].click)


@step(u'.* clico no campo "([^"]*)"$')
@step(u'.* clicar no campo "([^"]*)"$')
def e_clicar_no_campo_group1(step, group1):
    elementos = utils.encontrar_elementos_por_funcao_splinter_e_texto(group1, assert_error=True)
    elemento = utils.retorna_apenas_elementos_visiveis(elementos)
    utils.aguarda_loading_e_executa(elemento.click)


@step(u'.* clicar no elemento de id "([^"]*)"$')
@step(u'.* clico no elemento de id "([^"]*)"$')
def e_clico_no_elemento_de_id_group1(step, group1):
    elementos = utils.encontrar_elementos_por_funcao_splinter_e_texto(group1, assert_error=True, tipo='id')
    utils.aguarda_loading_e_executa(elementos[0].click)


@step(u'.* clicar no elemento de name "([^"]*)"$')
@step(u'.* clico no elemento de name "([^"]*)"$')
def e_clico_no_elemento_de_name_group1(step, group1):
    elementos = utils.encontrar_elementos_por_funcao_splinter_e_texto(group1, assert_error=True, tipo='name')
    utils.aguarda_loading_e_executa(elementos[0].click)
