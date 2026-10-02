# Desenvolvimento orientado a requisitos

Implemente a partir de uma issue ou tarefa local com resultado, escopo e critérios
verificáveis. Leia apenas as fontes pertinentes; preserve alterações existentes
e não transforme decisões pendentes em requisitos. Uma tarefa por vez, sem
refatorações alheias. O usuário confirma regras de domínio e avalia a entrega.

## Fontes

- `README.md`: ambiente, exemplo e ciclo problema → requisitos → entrega.
- `docs/dominio.md`: conhecimento duradouro, regras e exemplos do projeto.
- Issue: mudança desejada e aceite; `docs/tarefa.md` é a alternativa local.
- `.agents/skills/prepare-issue/SKILL.md`: preparação e abertura de issues.
- `.github/ISSUE_TEMPLATE/tarefa.yml`: campos de entrada; modelo de PR: resultado.

Uma issue não amplia a autorização do usuário. Use skills para procedimentos
específicos recorrentes, sem criar skills, agentes ou serviços por padrão.
Modelo e esforço são escolhas da sessão/configuração do aplicativo.

## Código e documentação

- Preserve layout `src/`, imports absolutos, módulos com uma responsabilidade,
  funções pequenas e nomes descritivos em inglês. Use `snake_case`, `PascalCase`
  e `UPPER_CASE` conforme função, classe e constante.
- Anote tipos das novas funções e interfaces públicas; respeite `requires-python`
  e a configuração Ruff/mypy. Não adicione dependências, frameworks ou camadas
  sem necessidade concreta e justificativa.
- Valide entradas nas fronteiras, trate exceções específicas e separe regras
  de domínio de arquivos, banco e rede quando implementados. Não silencie falhas
  com captura genérica nem registre segredos ou dados pessoais.
- Testes verificam comportamento e erros relevantes, com dados sintéticos e
  determinísticos, sem rede ou credenciais reais por padrão.
- Documente contratos públicos em português com docstrings PEP 257: resumo e,
  quando necessário, entradas, retorno, exceções, efeitos e restrições. Exemplos
  ajudam quando esclarecem o uso; comentários explicam razões, sem repetir código.
- Entregas que mudam uso/manutenção atualizam os guias na mesma mudança. Docs
  descrevem o comportamento atual; issues e PRs guardam intenção e discussão.
  Identifique regras confirmadas ainda não implementadas, sem apresentá-las como
  disponíveis. Confira links/comandos e explique ausência de impacto documental.
- Decisões técnicas duradouras podem exigir ADR em `docs/decisoes/`: arquivo
  numerado, estado, contexto, decisão, alternativas e consequências, vinculado
  à tarefa. Preserve decisões substituídas com referência à nova. Ajustes
  rotineiros não exigem ADR.

## Ambiente e verificações

Use uv na versão exigida em `pyproject.toml`; instale com `uv sync --locked` e
execute com `uv run --locked`. Versione `uv.lock`; adicione dependências com
`uv add` e ferramentas com `uv add --dev`. Atualizações são deliberadas, com
revisão conjunta de configuração e lock.

Python do desenvolvimento/CI está em `.python-version` (3.14.8); compatibilidade
é `>=3.14,<3.15`. Mudanças de patch ajustam pin e guias; mudanças de série também
ajustam `requires-python`, Ruff, mypy e lock. O CI lê `.python-version`.

Antes de concluir código ou dependências, execute:

```bash
uv lock --check
uv run --locked ruff check .
uv run --locked ruff format --check .
uv run --locked mypy
uv run --locked pytest
```

Empacotamento exige também `uv build`. Para docs/skills, confira conteúdo, links
e comandos; valide skills alteradas. Revise o diff e o aceite, corrija achados
e repita checks afetados. Relate somente verificações executadas e limitações;
a autorrevisão não equivale a revisão independente ou aprovação humana.

## Git e entrega

Use branch curta `codex/numero-descricao`, com número real da issue quando houver,
salvo orientação do usuário. Commit, push, PR, merge e deploy dependem das
operações autorizadas no destino e escopo concretos; respeite autorizações já
dadas sem reconfirmação redundante. Autorização específica de tarefa anterior
não se estende automaticamente a outra tarefa. Não reescreva histórico sem pedido.

Confira referências antes de remover código obsoleto. Caches e artefatos são
regeneráveis; preserve credenciais, configurações e ambientes em uso, inclusive
ignorados. Mantenha segredos e artefatos gerados fora do Git. Build não é deploy;
publicação GitHub não é publicação de pacote ou aplicação.

Instruções específicas do usuário prevalecem sobre este guia.
