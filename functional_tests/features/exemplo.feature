#language: pt-br


Funcionalidade: Exemplo


    Cenário: 1. Acessa o google
        Dado que visito a página "Google"
        Então eu devo ver a página "Google"

    Cenário: 2. Realiza busca no google
        Dado que visito a página "Google"
        E preencho o campo "q" com o valor "Uol"
        E clico no elemento de id "hplogo"
        E clico no botão "Pesquisa Google"
        Então o valor do campo "q" deve ser "Uol"

