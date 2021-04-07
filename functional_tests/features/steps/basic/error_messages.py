# -*- coding: utf-8 -*-


def mensagem_nao_esperada(esperada, obtida):
    return u'Mensagem esperada: {esperada} / Mensagem obtida: {obtida}'.format(esperada=esperada, obtida=obtida)


def campo_nao_encontrado(nome=''):
    return u'Campo nao encontrado: {nome}'.format(nome=nome)


def elemento_nao_encontrado(nome=''):
    return u'Elemento nao encontrado: {nome}'.format(nome=nome)


def opcao_nao_encontrada(nome=''):
    return u'Opcao nao encontrada: {nome}'.format(nome=nome)


def link_nao_encontrado(nome=''):
    return u'Link nao encontrado: {nome}'.format(nome=nome)


def botao_nao_encontrado(nome=''):
    return u'Botao nao encontrado: {nome}'.format(nome=nome)
