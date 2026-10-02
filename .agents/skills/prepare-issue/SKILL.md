---
name: prepare-issue
description: Transformar um problema em rascunho ou issue com requisitos e aceite verificáveis, usando o formulário do repositório. Use para preparar ou abrir issues; não para implementar a tarefa ou publicar código.
---

# Preparar e abrir uma issue

Prepare somente o rascunho quando esse for o pedido. A abertura exige autorização
para a issue e o repositório concreto; respeite autorizações já dadas na sessão,
sem confirmação redundante. Esta skill não autoriza implementação ou entrega de código.

## Fontes

Leia [AGENTS.md](../../../AGENTS.md) e o
[formulário](../../../.github/ISSUE_TEMPLATE/tarefa.yml), fonte dos campos.
Use a seção [Entrada local](../../../docs/tarefa.md#entrada-local) quando precisar
salvar um rascunho, sem carregar registros de outras tarefas. Consulte o
[domínio](../../../docs/dominio.md) e o
[fluxo](../../../README.md#do-problema-à-entrega) somente quando afetarem o problema.
Um documento em formato de template não confirma regras.

## Do problema aos requisitos

- Produza título e corpo com os rótulos atuais do formulário, incluindo campos
  opcionais. Não mantenha outra cópia do esquema nesta skill. Uma tarefa deve
  ter resultado coeso; sugira divisão quando necessário, sem abrir subtarefas
  automaticamente.
- Detalhe os requisitos confirmados como comportamento: entradas, saídas,
  exemplos, restrições e erros pertinentes. Para correções, inclua reprodução
  e resultado atual quando conhecidos. Relacione o aceite aos requisitos que
  verifica e indique validações necessárias, sem alegar testes executados.
- Fundamente fatos no pedido e nas fontes disponíveis. Não invente regras,
  números de issues, responsáveis, estimativas ou escolhas de implementação.
  Confira caminhos no checkout e distinga novos caminhos propostos de escopo
  autorizado. Dependências desconhecidas não são `Nenhuma`; prioridade/ciclo
  só recebem sugestões fundamentadas.
- Separe **Dúvidas de domínio** de requisitos/aceite. Pergunte o que impede uma
  tarefa verificável e continue a parte independente. Uma issue de investigação
  pode registrar dúvidas quando esse for o objetivo autorizado.
- Antes de salvar, confira estado Git e preserve alterações/rascunhos existentes.
  Salve no local solicitado ou acrescente seção em `docs/tarefa.md`; registre
  título, corpo, pendências, destino/autorização e busca de duplicatas.

## Destino e duplicatas

Não deduza destino pelo nome da pasta ou pelas referências de um template.
Remotos são evidência para conferir, não autorização. Se faltar destino,
preserve o rascunho e obtenha esse dado antes de consultar um repositório presumido
ou publicar.

Com destino confirmado e acesso disponível, procure issues abertas e fechadas
por objetivo e comportamento, usando a ferramenta GitHub disponível ou `gh`
com repositório explícito. Leia candidatas; título parecido não basta. Relate
links e sobreposição. Se já houver cobertura, proponha reutilização e preserve
o rascunho; não altere a issue existente por iniciativa própria. Uma autorização
explícita para issue distinta pode ser atendida.

Se consulta/autenticação falhar, preserve o rascunho e relate que a verificação
remota não foi possível; não declare ausência de duplicatas. Falha de busca não
revoga autorização já dada: se a criação for viável, relate a limitação e prossiga
no escopo autorizado.

## Publicar e conferir

Confira o corpo final contra formulário, requisitos e destino autorizado antes
da mutação. Não publique enquanto dúvidas impedirem o aceite, salvo investigação
autorizada. Com escopo/autorização suficientes, abra a issue; se usar `gh`, passe
o corpo salvo por `--body-file` para preservar quebras de linha e evitar interpolação.

Confirme número, URL e conteúdo. Após timeout/resposta ambígua, consulte o destino
e compare título/corpo antes de repetir. Se não puder determinar se houve criação,
pare as tentativas, preserve o rascunho e relate a incerteza. Registre vínculo local
somente quando verificado; não apresente rascunho como issue publicada.
