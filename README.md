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
- O decorador __@pytest.fixture__ é usado no framework de pytest para preparar funções e condicioná-las para testes. As __fixtures__ ajudam a evitar a duplicação de código, fornecendo uma maneira reutilizável de preparar os testes com os pré-requisitos necessários.
- __Fixtures__ são funções que fornecem dados ou recursos necessários para a execução dos testes. Elas são como "montagens" que preparam o ambiente para que os testes possam ser realizados de forma consistente e isolada.
- Pode-se definir escopos para __fixtures__ (por exemplo, function, class, module, session) para controlar sua reutilização: 
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
 ---

 **Aula_08**
 - __SQLAlchemy__ é uma biblioteca de __ORM__ (__Object-Relational Mapping__) em Python que permite interagir com bancos de dados usando classes e objetos, abstraindo as consultas SQL complexas. Além de funcionar como ORM, SQLAlchemy também oferece ferramentas para executar consultas SQL diretamente. Ex: __text__.
 ---

 **Aula_09**
- Em pytest, o __escopo de uma fixture__ define o período de tempo (ou ciclo de vida):
    - Pode-se definir escopos para __fixtures__ (por exemplo, function, class, module, session) para controlar sua reutilização: 
        - function: (padrão) Cada teste usa sua própria instância da fixture.
        - class: Uma instância da fixture é criada por classe de teste.
        - module: A mesma instância é usada em todos os testes do módulo.
        - session: A mesma instância é usada em todos os testes de uma execução de pytest.
---

 **Aula_10, Aula_11 & Aula_12**
- Em pytest, um __teste parametrizado__ permite rodar o mesmo caso de teste várias vezes com diferentes conjuntos de dados. Isso evita a repetição de código e facilita a cobertura de múltiplos cenários. O decorador __@pytest.mark.parametrize()__ permite rodar um teste várias vezes com diferentes conjuntos de entradas e saídas esperadas.

- Exp:

    @pytest.mark.parametrize("a, b, resultado", [(1, 2, 3), (4, 5, 9), (10, 20, 30)])

    def test_soma(a, b, resultado):
        assert a + b == resultado

Onde: @pytest.mark.parametrize("a+b=resposta",[(1 + 2 = 3),(4 + 5 = 9),(10 + 20 = 30)]) 
 ---

  **Aula_13 & Aula_14**
  - O decorador __@pytest.mark__ em pytest é utilizado para marcar testes, permitindo categorização, personalização e controle sobre a execução dos testes por nome (apelido).
  Exemplo:  __@pytest.mark.meu_teste__
            __Terminal: pytest -m meu_teste__
  - Um complemento para utilização do decorador __@pytest.mark__ é o arquivo __pytest.ini__, __embora não seja obrigatório__, o arquivo __pytest.ini__ desempenha um papel crucial no uso de __@pytest.mark__ em testes com pytest. Ele serve como um arquivo de configuração centralizado que permite definir e gerenciar as marcações personalizadas que você utiliza em seus testes.
---

 **Aula_15 & Aula_16**
 - A função __pytest.raises()__ do Pytest é uma ferramenta poderosa que permite verificar se um determinado bloco de código lança uma exceção específica. A função __pytest.raises(__) é usada como um gerenciador de contexto __(with statement)__. O código que se espera que lance a exceção é colocado dentro desse bloco. Se a exceção esperada for lançada, o teste passa. Caso contrário, o teste falha.
 ---
 
 **Aula_17**
 - No pytest, __plugins__ são extensões que adicionam funcionalidades extras ao framework de testes. Eles podem modificar o comportamento padrão, adicionar novos recursos ou facilitar integrações com outras ferramentas.

- Aqui estão alguns dos plugins mais usados no pytest:
    - pytest-cov → Relatórios de cobertura de código
    - pytest-xdist → Execução paralela de testes
    - pytest-django → Integração com Django
    - pytest-mock → Suporte para mocks usando unittest.mock
    - pytest-randomly → Executa testes em ordem aleatória

- Exemplo de pytest-cov: 
    - __test_funcoes_cov.py__
---

**Aula_18**
- Exemplo de pytest em Class (Classe).
---

**Aula_19**


