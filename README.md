# Template Python para desenvolvimento por requisitos

Base mínima com pacote executável, testes, uv, Ruff, mypy e CI. O Codex conduz
as tarefas a partir de requisitos verificáveis. A base não define regras de
negócio, framework, provedor, licença ou destino de entrega de projetos derivados.

## Do problema à entrega

1. Apresente o problema: `Use $prepare-issue para preparar uma tarefa sobre ...`.
   A [skill](.agents/skills/prepare-issue/SKILL.md) organiza requisitos confirmados,
   exemplos, escopo e aceite conforme o
   [formulário](.github/ISSUE_TEMPLATE/tarefa.yml). Dúvidas ficam separadas.
   Pode salvar um rascunho em [docs/tarefa.md](docs/tarefa.md); para abrir uma
   issue real, informe o repositório concreto e autorize sua criação.
2. Peça ao Codex a implementação da tarefa, indicando operações autorizadas.
   Ele lê [AGENTS.md](AGENTS.md), a tarefa e as fontes pertinentes, implementa
   dentro do escopo e verifica o aceite com testes e revisão do diff.
3. Quando a mudança alterar uso ou manutenção, atualize o README e o
   [domínio](docs/dominio.md) com o comportamento entregue. Issue guarda a
   intenção de mudança; docs guardam conhecimento atual. Decisões técnicas
   relevantes podem exigir ADR conforme `AGENTS.md`.
4. Para publicação autorizada, use o [modelo de PR](.github/pull_request_template.md),
   vinculando issue, aceite e evidências. Reutilize a branch/PR existente.
   Integre após checks aprovados e avaliação do responsável ou revisão independente
   definida por ele; autorrevisão do agente não equivale a essa avaliação.
5. Entrega externa, se fizer parte da tarefa, precisa de destino, versão,
   autorização, verificação de funcionamento e recuperação definidos. Registre
   resultado e evidências. Se falhar, registre e corrija sem desativar checks.
   Para desfazer mudança integrada, use PR de revert; segredo exposto exige revogação.

Use `Closes #123` somente quando a PR resolver toda a issue; o fechamento ocorre
após integração na branch padrão. Entrega parcial apenas referencia a issue.
Features grandes podem ser divididas em tarefas coesas com dependências reais;
prioridade, responsável e ciclo são registrados quando definidos. Não imponha
duração fixa nem feche pendências pelo fim de um ciclo. Bloqueios, cancelamentos
e duplicidades devem ser registrados com estado e próximo passo.

Este fluxo é orientado por instruções e ferramentas existentes do Codex Desktop,
sem coordenador por API ou workflow de agentes. O usuário inicia a tarefa no
aplicativo; o CI executa apenas qualidade. Deploy não é necessário para usar
ou concluir este template, e nenhum pipeline de aplicação vem configurado.

A skill é descoberta em `.agents/skills/`, sem instalação global. Ela pode ser
selecionada pelo pedido; isso não autoriza publicação. Se não aparecer, reinicie
o Codex conforme a [documentação oficial](https://learn.chatgpt.com/docs/build-skills).

Recorrência é opcional: só configurar quando solicitada, com frequência,
repositório, tarefas elegíveis e permissões de commit/publicação explícitas.
Evite PRs duplicadas e merge automático. Para execuções locais, computador e
aplicativo precisam estar ativos; valide a primeira execução. Notifique mudanças
relevantes, conclusão, falhas ou decisões necessárias; mantenha silêncio no restante.

## Ambiente e exemplo

Use uv **0.12.22**, fixado em `pyproject.toml`, e Python **3.14.8**, fixado em
`.python-version`; a compatibilidade do pacote é `>=3.14,<3.15`.
Instale uv conforme a [documentação](https://docs.astral.sh/uv/getting-started/installation/).

```bash
uv sync --locked
uv run --locked python -m python_template
uv run --locked python-template
```

Os dois comandos exibem `Hello, Python!`. O uv gerencia `.venv/` sem ativação
manual. A saudação é um exemplo substituível, não uma regra de negócio.

Execute os [checks de AGENTS.md](AGENTS.md#ambiente-e-verificações).
`uv build` gera wheel e distribuição fonte em `dist/`, sem publicar nada.
A wheel contém o pacote/CLI; a fonte também inclui testes, guias, skill, templates
e lock. Para reproduzir a instalação do CI, use `uv sync --locked --no-editable`
e acrescente `--no-editable` aos comandos `uv run --locked`.

O workflow [Testes Python](.github/workflows/tests.yml), job **Python fixado**,
verifica lock, instalação, tipos, testes, lint, formatação e build em push, PR
ou disparo manual. Confira seu resultado no commit publicado; validação local
não comprova CI remoto. Proteções de branch e revisão devem ser configuradas
conforme os recursos da conta, sem presumir que já estejam habilitadas.

No VS Code, use `.venv/` como interpretador. Pyright analisa `src/` e `tests/`
no modo `standard`; verificação opcional: `uvx pyright --pythonpath .venv/bin/python`.

## Reutilizar a base

1. Crie um repositório a partir do template ou copie os arquivos sem `.git/`,
   ambientes, caches, artefatos e configurações locais de credenciais.
2. Personalize `project.name` e `project.description` em `pyproject.toml`.
   Renomeie `src/python_template/` para um nome válido de importação e atualize
   imports, testes, nome/alvo da CLI em `[project.scripts]` e referências no
   README/AGENTS. Para biblioteca sem CLI, remova `[project.scripts]` e
   `src/python_template/__main__.py`; ajuste/remova os testes e comandos
   correspondentes, preservando os testes do pacote.
3. Adapte README/AGENTS e preencha `docs/dominio.md` com requisitos reais
   confirmados. Execute `uv lock`, `uv sync --locked` e os checks de `AGENTS.md`;
   não edite o lock manualmente. Revise configuração e lock juntos.
4. Defina o repositório/visibilidade quando for publicar e uma licença antes de
   distribuir. Confira remotos e histórico; não assuma destino do template ou
   substitua remotos automaticamente. Use autenticação local sem tokens em URLs.
   Publique somente arquivos revisados e autorizados, preservando ignorados em uso.
5. Na primeira publicação autorizada, crie um repositório vazio. Em cópia sem
   remoto/commits, use `main`, registre arquivos revisados, configure `origin`
   para o destino confirmado e publique com `git push -u origin main`. Se já houver
   histórico, siga o fluxo de PR. Configurações, segredos, Actions e proteções da
   conta precisam de configuração própria. Para disponibilizar como template,
   habilite **Settings → Template repository**, conforme o
   [guia GitHub](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-template-repository).

O template é ponto de partida: acrescente docs quando conhecimento ou decisões
duradouros precisarem de fonte própria, e skills quando procedimentos específicos
recorrentes demonstrarem essa necessidade, sem antecipar arquivos por categoria.

Se uma tarefa futura incluir pacote ou aplicação, defina nela provedor, ambiente,
gatilho, versão, nomes de configurações/segredos e comandos de publicação,
verificação e recuperação, incluindo migrações quando aplicáveis. Registre nos
guias somente o procedimento efetivamente implementado. Build, push, publicação
de pacote e deploy são operações distintas.
