# -*- coding: utf-8 -*-

from functional_tests.features.steps.basic import utils, error_messages
from functional_tests import settings

from lettuce import step, world

from retrying import retry, RetryError

DEFAULT_WAIT_TIME_MS = settings.DEFAULT_WAIT_TIME * 1000


@step(u'.*[^não] devo estar na p[áa]gina "([^"]*)"$')
@step(u'.*[^não] devo permanecer na p[áa]gina "([^"]*)"$')
@step(u'.*[^não] devo ver a p[áa]gina "([^"]*)"$')
def eu_devo_ver_alguma_pagina(step, nome):
    current_url = (world.browser.url).split('?')[0]
    full_url = (world.base_url + world.pages[nome]['url'])
    assert utils.aguarda_pagina_ser_carregada(
        nome), 'url atual: "%s" / url esperada: "%s"' % (current_url, full_url)


@step(u'.*não devo estar na p[áa]gina "([^"]*)"$')
@step(u'.*não devo permanecer na p[áa]gina "([^"]*)"$')
@step(u'.*não devo ver a p[áa]gina "([^"]*)"$')
def eu_nao_devo_ver_alguma_pagina(step, nome):
    try:
        utils.aguarda_pagina_ser_carregada(nome)
    except RetryError:
        assert True
    else:
        assert False, u'Pagina {nome} foi carregada'.format(nome=nome)


@step(u'.*[^não] devo ver a mensagem ("[^"]*")')
@step(u'E o conte[úu]do: ("[^"]*")')
@step(u'Então devo ver o conte[úu]do: ("[^"]*")')
@step(u'.*[^não] devo ver o conte[úu]do: ("[^"]*")')
@step(u'.*[^não] devo ver a mensagem contendo ("[^"]*")')
@retry(stop_max_delay=DEFAULT_WAIT_TIME_MS, wait_fixed=500)
def entao_eu_devo_ver_a_mensagem_contendo_group1(step, group1):
    assert world.browser.is_text_present(
        utils.processa_group(group1)[0])


@step(u'.* não devo ver a mensagem ("[^"]*")')
@step(u'Então não devo ver o conte[úu]do: ("[^"]*")')
@step(u'.* não devo ver o conte[úu]do: ("[^"]*")')
@step(u'.* não devo ver a mensagem contendo ("[^"]*")')
def entao_eu_nao_devo_ver_a_mensagem_contendo_group1(step, group1):
    assert not world.browser.is_text_present(
        utils.processa_group(group1)[0])


@step(u'Então devo ver a mensagem de sucesso "([^"]*)"')
@step(u'.*[^não] devo ver a mensagem de sucesso "([^"]*)"')
def entao_eu_devo_ver_a_mensagem_de_sucesso_group1(step, group1):
    assert utils.encontrar_elementos_por_funcao_splinter_e_texto('.alert.alert-success', group1, tipo='css')


@step(u'.*[^não] devo ver a mensagem de erro "([^"]*)"')
def eu_devo_ver_a_mensagem_de_erro_contendo_group1(step, group1):
    assert utils.encontrar_elementos_por_funcao_splinter_e_texto('.alert.alert-danger', group1, tipo='css')


@step(u'Então devo ver a mensagem de alerta "([^"]*)"')
@step(u'.*[^não] devo ver a mensagem de alerta "([^"]*)"')
def entao_devo_ver_a_mensagem_de_alerta_group1(step, group1):
    assert utils.encontrar_elementos_por_funcao_splinter_e_texto('.alert.alert-warning', group1, tipo='css')


# Assert tabela #########################################################


@step(u'.*[^não] devo ver na linha da tabela os conte[úu]dos: (.+)$')
@step(u'.* eu devo ver na linha da tabela os contéudos: (.+)$')
@step(u'.*[^não] devo ver na linha da tabela o conte[úu]do: (.+)$')
@step(u'.*[^não] devo ver na linha da tabela o conte[úu]do (.+)$')
def entao_eu_devo_ver_na_linha_da_tabela_os_conteudos(step, group1):
    assert utils.encontrar_elementos_por_x_conteudos(
        'tr', utils.processa_group(group1), '')


@step(u'.não devo ver na linha da tabela os conte[úu]dos: (.+)$')
@step(u'.* eu devo ver na linha da tabela os contéudos: (.+)$')
@step(u'.*não devo ver na linha da tabela o conte[úu]do: (.+)$')
@step(u'.*não devo ver na linha da tabela o conte[úu]do (.+)$')
def entao_eu_nao_devo_ver_na_linha_da_tabela_os_conteudos(step, group1):
    assert not utils.encontrar_elementos_por_x_conteudos(
        'tr', utils.processa_group(group1), '')


@step(u'.*[^não] devo ver na primeira linha do corpo da tabela os conte[úu]dos: (.+)$')
def entao_eu_devo_ver_na_primeira_linha_do_corpo_da_tabela_os_conteudos(step, group1):
    assert utils.encontrar_elementos_por_x_conteudos(
        'tr:nth(1)', utils.processa_group(group1), '')


@step(u'.* a tabela deve ter "([^"]*)" linhas')
def entao_a_tabela_deve_ter_group1_linhas(step, group1):
    resultado = world.browser.evaluate_script('$("tr")')
    assert len(resultado) == int(group1), 'resultado: "%s" / esperado: "%s"' % (len(resultado), int(group1))


# Assert elementos ###########################################################


@step(u'.* o bot[ãa]o de nome "([^"]*)" deve estar visível')
@step(u'.*[^não] devo ver o bot[ãa]o "([^"]*)"')
def entao_eu_devo_ver_o_botao_group1(step, group1):
    assert utils.encontrar_botoes_por_texto(group1)


@step(u'.* o bot[ãa]o de nome "([^"]*)" não deve estar visível')
@step(u'.* não devo ver o bot[ãa]o "([^"]*)"')
def entao_eu_nao_devo_ver_o_botao_group1(step, group1):
    assert not utils.encontrar_botoes_por_texto(group1)


@step(u'.*[^não] devo ver o link "([^"]*)"')
@step(u'.* o link "([^"]*)" deve estar vis[ií]vel')
def entao_eu_devo_ver_o_link_group1(step, group1):
    assert utils.encontrar_links_por_texto(group1, assert_error=True)


@step(u'.* não devo ver o link "([^"]*)"')
@step(u'.* o link "([^"]*)" n[aã]o deve estar vis[ií]vel')
def entao_eu_nao_devo_ver_o_link_group1(step, group1):
    assert not utils.encontrar_links_por_texto(group1)


@step(u'.* o campo "([^"]*)" deve estar visível')
@step(u' [^não] devo ver o campo "([^"]*)"')
def entao_o_campo_group1_deve_estar_visivel(step, group1):
    assert utils.retorna_apenas_elementos_visiveis(
        utils.encontrar_elementos_por_funcao_splinter_e_texto(group1)
    )


@step(u'.* o campo "([^"]*)" não deve estar visível')
@step(u'.* não devo ver o campo "([^"]*)"')
def entao_o_campo_group1_nao_deve_estar_visivel(step, group1):
    assert not utils.retorna_apenas_elementos_visiveis(
        utils.encontrar_elementos_por_funcao_splinter_e_texto(group1)
    )


@step(u'.* o elemento resultado do seletor "([^"]*)" não deve estar visível')
@step(u'.* não devo ver o elemento resultado do seletor "([^"]*)"')
def e_nao_devo_ver_o_elemento_elemento_resultado_do_seletor(step, group1):
    elementos = utils.encontrar_elementos_por_seletor_jquery('$("' + group1 + '")', assert_error=False)
    assert not elementos


@step(u'.* o elemento resultado do seletor "([^"]*)" deve estar visível')
@step(u'.* [^não] devo ver o elemento resultado do seletor "([^"]*)"')
def e_devo_ver_o_elemento_elemento_resultado_do_seletor(step, group1):
    elementos = utils.encontrar_elementos_por_seletor_jquery('$("' + group1 + '")', assert_error=False)
    assert elementos

# Assert validação do campo ##################################################


@step(u'.*[^não] devo ver a validação no campo "([^"]*)" com a mensagem "([^"]*)"')
@retry(stop_max_delay=DEFAULT_WAIT_TIME_MS, wait_fixed=500)
def entao_eu_devo_ver_a_validacao_no_campo_campo_com_a_mensagem_group1(step, group1, group2):
    form_group_seletor = '$("[name={group1}]").parents(".form-group.has-error")'.format(group1=group1)
    form_group = utils.encontrar_elementos_por_seletor_jquery(form_group_seletor, assert_error=True)[0]
    assert form_group, u'O campo {group1} nao recebeu classe has-error'.format(group1=group1)
    world.browser.is_text_present(group2)
    elementos = utils.retorna_apenas_elementos_visiveis(
        form_group.find_elements_by_tag_name('span'), True
    )

    assert [x for x in elementos if group2 in x.text], error_messages.mensagem_nao_esperada(group2, '')


# Assert valor de campo ----------------------

@step(u'.* o valor do campo "([^"]*)" deve ser ("[^"]*")')
@step(u'.* o valor do campo "([^"]*)" deve ser a ("[^"]*")')
@step(u'.*[^não] devo ver no campo "([^"]*)" o valor ("[^"]*")')
@retry(stop_max_delay=DEFAULT_WAIT_TIME_MS, wait_fixed=500)
def o_valor_do_campo_group1_deve_ser_group2(step, group1, group2):
    elementos = utils.encontrar_elementos_por_funcao_splinter_e_texto(group1)
    elemento = utils.retorna_apenas_elementos_visiveis(elementos)[0]
    assert utils.processa_group(group2)[0] == elemento.value.rstrip(), u'Valor obtido: {valor}'.format(valor=elemento.value)


@step(u'.* o valor do "([^"]*)" campo "([^"]*)" deve ser ("[^"]*")')
def e_o_valor_do_group1_campo_group2_deve_ser_group3(step, group1, group2, group3):
    posicao = utils.retorna_numero_do_ordinal(group1)
    elementos = utils.encontrar_elementos_por_funcao_splinter_e_texto(group2)
    elemento = utils.retorna_apenas_elementos_visiveis(elementos)[posicao]
    assert utils.processa_group(group3)[0] == elemento.value.rstrip(), u'Valor obtido: {valor}'.format(valor=elemento.value)


@step(u'.* o valor do campo "([^"]*)" não deve ser ("[^"]*")')
@step(u'.* o valor do campo "([^"]*)" não deve ser a ("[^"]*")')
@step(u'.* não devo ver no campo "([^"]*)" o valor ("[^"]*")')
@retry(stop_max_delay=DEFAULT_WAIT_TIME_MS, wait_fixed=500)
def o_valor_do_campo_group1_nao_deve_ser_group2(step, group1, group2):
    elementos = utils.encontrar_elementos_por_funcao_splinter_e_texto(group1)
    elemento = utils.retorna_apenas_elementos_visiveis(elementos)[0]
    assert utils.processa_group(group2)[0] != elemento.value.rstrip(), u'Valor obtido: {valor}'.format(valor=elemento.value)


@step(u'.* o valor do campo de select "([^"]*)" deve ser ("[^"]*")')
@retry(stop_max_delay=DEFAULT_WAIT_TIME_MS, wait_fixed=500)
def e_o_valor_do_campo_de_selecao_group1_deve_ser_group2(step, group1, group2):
    option = utils.encontrar_option_de_input_por_texto(group1, group2)[0]
    assert option.selected, u'A opcao nao esta selecionada'


# Assert situação campo -----------------------------------------------------------

@step(u'.* o campo "([^"]*)" deve estar desabilitado')
def entao_o_campo_campo_deve_estar_desabilitado(step, group1):
    elementos = utils.encontrar_elementos_por_funcao_splinter_e_texto(group1, assert_error=True)
    elemento = utils.retorna_apenas_elementos_visiveis(elementos)[0]
    assert utils.elemento_encontra_se_desabilitado(elemento)


@step(u'.* o "([^"]*)" campo "([^"]*)" deve estar desabilitado')
def entao_o_group1_campo_group2_deve_estar_desabilitado(step, group1, group2):
    posicao = utils.retorna_numero_do_ordinal(group1)
    elementos = utils.encontrar_elementos_por_funcao_splinter_e_texto(group2, assert_error=True)
    elemento = utils.retorna_apenas_elementos_visiveis(elementos)[posicao]
    assert utils.elemento_encontra_se_desabilitado(elemento)


@step(u'.* o botão "([^"]*)" deve estar desabilitado')
def entao_o_botao_group1_deve_estar_desabilitado(step, group1):
    elementos = utils.encontrar_botoes_por_texto(group1, assert_error=True)
    elemento = utils.retorna_apenas_elementos_visiveis(elementos)[0]
    assert utils.elemento_encontra_se_desabilitado(elemento)


# Assert aba ativa --------------------------------------------------------------------


@step(u'.* devo ver a aba ativa de nome "([^"]*)"')
@step(u'.* aba ativa deve ser "([^"]*)"')
@retry(stop_max_delay=DEFAULT_WAIT_TIME_MS, wait_fixed=500)
def e_devo_ver_a_aba_ativa_de_nome_group1(step, group1):
    assert utils.encontrar_elementos_por_funcao_splinter_e_texto(
        '.active', group1, 'css'
    ), error_messages.elemento_nao_encontrado()


@step(u'.* aba "([^"]*)" não deve estar visível')
def entao_a_aba_group1_nao_deve_estar_visivel(step, group1):
    assert not utils.encontrar_elementos_por_funcao_splinter_e_texto(
        '.lead', group1, 'css'
    ), error_messages.elemento_nao_encontrado()


@step(u'.* aba "([^"]*)" deve estar visível')
def entao_a_aba_group1_deve_estar_visivel(step, group1):
    assert utils.encontrar_elementos_por_funcao_splinter_e_texto(
        '.lead', group1, 'css'
    ), error_messages.elemento_nao_encontrado()


# Assert check campo ---------------------------------------------------------------


@step(u'.* o campo "([^"]*)" deve estar checado')
def e_o_o_campo_group1_deve_estar_checado(step, group1):
    assert utils.encontrar_elementos_por_funcao_splinter_e_texto(group1)[0].checked


@step(u'.* o campo "([^"]*)" não deve estar checado')
def e_o_o_campo_group1_nao__deve_estar_checado(step, group1):
    assert not utils.encontrar_elementos_por_funcao_splinter_e_texto(group1)[0].checked
