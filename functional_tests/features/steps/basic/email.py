# -*- coding: utf-8 -*-
import re

from email import message_from_file
from functional_tests import settings
from functional_tests.features.steps.basic import error_messages

from retrying import retry

from lettuce import step, world


EMAILS_MAP = {
}


def busca_email_em_emails(email_nome, emails):
    world.salva_coverage_browser()
    for email in emails:
        world.browser.visit(email)
        html = world.browser.html
        for chave in EMAILS_MAP[email_nome]['chave']:
            if chave in html:
                return email


@step(u'.* acessar o email de "([^"]*)" recebido')
@step(u'.* acesso o email de "([^"]*)" recebido')
@retry(stop_max_attempt_number=3, wait_fixed=5000)
def quando_eu_acessar_o_email_de_group1_recebido(step, group1):
    emails = retorna_ultimos_emails_recebidos()
    world.ultimo_email_acessado = busca_email_em_emails(group1, emails)
    if not world.ultimo_email_acessado:
        raise AssertionError('Email nao recebido')


@step(u'.* não devo ter recebido nenhum email de "([^"]*)"')
def e_nao_devo_ter_recebido_nenhum_email_de_group1(step, group1):
    step.given(u'E aguardo "2" segundos')
    emails = retorna_ultimos_emails_recebidos()
    if busca_email_em_emails(group1, emails):
        raise AssertionError('Email foi recebido')


@step(u'.* visualizar novamente o último email acessado')
def quando_eu_visualizar_novamente_o_ultimo_email_acessado(step):
    if not world.ultimo_email_acessado:
        raise AssertionError(u'Nenhum email anteriormente acessado')
    world.salva_coverage_browser()
    world.browser.visit(world.ultimo_email_acessado)


@step(u'.* clicar no link "([^"]*)" presente no corpo de email')
@step(u'.* clico no link "([^"]*)" presente no corpo de email')
@step(u'.* cliquei no link "([^"]*)" presente no corpo de email')
def e_clicar_no_link_group1_presente_no_corpo_de_email(step, group1):
    elemento = world.browser.find_link_by_partial_text(group1)
    if not elemento:
        raise AssertionError(error_messages.link_nao_encontrado(group1))
    elemento.click()


@step(u'Então o destinatário deve ser "([^"]*)"')
def entao_o_remente_deve_ser_group1(step, group1):
    regex = 'To: (.*) Date'
    match = re.search(regex, world.browser.find_by_css('body').text)
    assert group1 in match.group(), u'Destinatário esperado: {group1} / Destinatário obtido: {remetentes}'.format(group1=group1, remetentes=match.group())


def retorna_ultimos_emails_recebidos():
    from os import listdir
    from os import rename

    file_folder = listdir(settings.EMAIL_FILE_PATH)
    file_folder.sort()
    file_folder.reverse()  # Organiza do mais novo ao mais antigo

    list_paths = []

    for file in file_folder:
        if file.endswith('.log'):
            file_name_old = settings.EMAIL_FILE_PATH + '/' + file
            parse_emails(file_name_old)
            file_name_new = file_name_old.replace('.log', '.html')
            rename(file_name_old, file_name_new)
            list_paths.append('file://' + file_name_new)

    return list_paths


def parse_emails(email_path):
    bb = message_from_file(open(email_path))
    body_list = [
        'From: {from_email}'.format(from_email=bb['from']),
        'To: {to}'.format(to=bb['to']),
        'Date: {date}'.format(date=bb['date'])
    ]
    if bb.is_multipart():
        for payload in bb.get_payload():
            # if payload.is_multipart()
            body_list.append(payload.get_payload(None, True))
    else:
        body_list.append(bb.get_payload(None, True))
    open(email_path, 'w').write(' '.join(body_list))
