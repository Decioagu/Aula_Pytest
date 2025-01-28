# Aula_Pytest
 Framework de teste em Python

## Pytest 
- Pytest é um framework de teste para a linguagem de programação Python, é amplamente utilizado por desenvolvedores para verificar se o código está funcionando corretamente, de forma contínua, à medida que o projeto evolui.

- No pytest, a __nomeação__ de arquivos, funções e classes de teste é essencial, pois ele __utiliza convenções de nomes para detectar automaticamente os testes a serem executados__. 

- Nomeação de __arquivos__ para teste:
    - Ter nomes que __"começam com test_"__ ou __"terminam com _test"__, exemplos:
        - test_meu_script.py
        - meu_script_test.py
        - meu_script.py (não será reconhecido automaticamente pelo pytest)

- Nomeação de __funções__ para teste:
    - As funções de teste dentro dos arquivos devem, ter nomes que __"começam com test_"__.
    - Exemplo:
        __Arquivo: test_exemplo.py__
        def test_soma():
            assert 1 + 1 == 2

- Nomeação de __classes__ de teste:
    - As classes que agrupam testes devem:
        - Ter nomes que começam com __Test__.
        - Não precisam herdar de nenhuma classe base, a menos que você esteja usando algo como unittest.
        - Exemplo:
            __Arquivo: test_exemplo.py__
            class TestOperacoes:
                def test_soma(self):
                    assert 2 + 2 == 4

                def test_subtracao(self):
                    assert 5 - 3 == 2


- Testes inválidos devido nomeação erronia, exemplos:
    __Arquivo: exemplo.py__ (não será reconhecido automaticamente pelo pytest)
        def test_soma():
            assert 1 + 1 == 2

    Arquivo: test_exemplo.py
        def __soma()__: (não será identificado como teste)
            assert 1 + 1 == 2

    Arquivo: test_exemplo.py
            class __Operacoes__: (não será identificado como teste)
                def test_soma(self):
                    assert 2 + 2 == 4

- Dicas adicionais:
    - 1. Os teste devem ser aplicados na pasta que contem os arquivos.

    - 2. Evite adicionar lógica de teste diretamente fora de funções ou classes, pois isso pode causar comportamento inesperado.
    
    - 3. __Para rodar testes específicos__:
        - Arquivo: __pytest test_meu_arquivo.py__
        - Função: __pytest -k "test_nome_funcao"__
        - Classe: __pytest -k "TestMinhaclasse"__
---

**Aula_01 e Aula_02**
- O __"assert"__ no pytest é uma ferramenta fundamental para escrever testes, pois verifica se uma condição é verdadeira. Caso a condição seja falsa, o pytest lança uma exceção (AssertionError) e considera o teste como falho.
    - Sintaxe do assert:
        assert condição, "mensagem_opcional"
            - assert: avalia uma expressão (booleana)
            - condição: A expressão ou comparação que deve ser verdadeira.
            - "mensagem_opcional": Uma mensagem personalizada que será exibida em caso de falha (opcional).
---

**Aula_03**
- Execução de testes:
    - 1º. Ativar ambiente virtual: .\venv\Scripts\activate

- Teste aplicados em uma pasta, executa sub pasta e pasta que tiverem teste a ser aplicado.
    - 2º. Testar todos os arquivo da pasta: pytest .\Aula_03\

- Dentro de uma mesma pasta é possível executar teste especifico:
    - 3º. Testar arquivo: pytest .\Aula_03\test_basic3A.py
    - 4º. Testar arquivo: pytest .\Aula_03\test_basic3B.py
    - 5º. Testar arquivo: pytest .\Aula_03\sub_pasta\test_basic3C.py
---

**Aula_04**
- Neste exemplo o arquivo __funcoes.py__ esta sendo testado por arquivo __test_basic4.py__. Esta pratica ajuda a executar teste em qualquer arquivo Python sem necessidade de alteração em arquivo original (no caso __funcoes.py__), criando apenas arquivo exclusivo para teste (no caso __test_basic4.py__).
---

**Aula_05**
- Sintaxe do __assert__:
        assert condição, "mensagem_opcional"
            - assert: avalia uma expressão (booleana)
            - condição: A expressão ou comparação que deve ser verdadeira.
            - "mensagem_opcional": Uma mensagem personalizada que será exibida em caso de falha (opcional).
---
**Aula_06**
- O decorador __@pytest.fixture__ é usado no framework de pytest para preparar funções e condicioná-las para testes. As fixtures ajudam a evitar a duplicação de código, fornecendo uma maneira reutilizável de preparar os testes com os pré-requisitos necessários.
- Pode-se definir escopos para fixtures (por exemplo, function, class, module, session) para controlar sua reutilização: 
    - function: (padrão) Cada teste usa sua própria instância da fixture.
    - class: Uma instância da fixture é criada por classe de teste.
    - module: A mesma instância é usada em todos os testes do módulo.
    - session: A mesma instância é usada em todos os testes de uma execução de pytest.
---

**Aula_07**
- O MagicMock é uma classe do módulo __unittest.mock__ em Python. Ele é usado para criar objetos simulados (mocks) que podem substituir dependências ou partes de um código durante testes, permitindo que você controle o comportamento do objeto simulado e verifique como ele foi usado. Isso é especialmente útil para testar componentes de forma isolada.

- Por que usar MagicMock?
    - Testar componentes isoladamente: Se uma função ou classe depende de um banco de dados, API ou qualquer outro serviço externo, você pode substituir essas dependências por mocks para que o teste seja mais previsível, sem risco com interações com objetos reais. 
    - __Exp: magic.py__

 - __Requests__ é uma biblioteca Python que fornece uma interface simples e elegante para __fazer solicitações HTTP__. Ela é muito popular entre desenvolvedores web e de APIs, pois permite enviar e receber dados de servidores HTTP de forma rápida e fácil.