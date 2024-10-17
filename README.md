<div name="top-readme" align=center>
  <h1>Python e GPT</h1>
</div>

CURSO ALURA | Python e GPT: crie seu chatbot com IA

---

# 📌 Table of Contents

- [01. Playground e a API da OpenAI](#01-playground-e-a-api-da-openai)
  - [Parâmetros do Palyground](#parâmetros-do-palyground)
  - [Playground](#playground)
- [04. Batch e Controle de Erros](#04-batch-e-controle-de-erros)
  - [Caminho de Arquivos em Python](#caminho-de-arquivos-em-python)
  - [Códigos de Erro](#códigos-de-erro)

<p align="right"><a href="#top-readme">(back to top)</a></p>

---

# 01. Playground e a API da OpenAI

## Parâmetros do Palyground

Como vimos durante a aula, os parâmetros controlam o comportamento e a saída do modelo de linguagem gerado no Playground da plataforma da OpenAI. Entender para que servem os parâmetros é essencial para atender às necessidades de seu projeto com qualidade e comportamento desejado.

Os principais parâmetros, do modo chat, têm a seguinte funcionalidade:

- **Mode (modo)**: define como você deseja que o modelo se comporte, e cada um dos modos tem seu próprio contexto e aplicação específicos. Atualmente, temos os modos:
    - `chat`: usado para criar interações de conversa com o modelo;
    - `complete`: uma forma de solicitar ao modelo que complete um texto ou código fornecido;
    - `edit`: projetado para auxiliar na edição e revisão de textos.
- **Model (modelo)**: refere-se à arquitetura específica do modelo de linguagem que você deseja usar. No playground da OpenAI, você pode escolher entre vários modelos, cada um com diferentes capacidades de processamento de instruções e tamanhos de tokens. Você pode verificar [todos os modelos disponíveis e suas especificações na documentação da OpenAI](https://platform.openai.com/docs/models/models).

- **Temperature (temperatura)**: controla a aleatoriedade da saída gerada pelo modelo. Valores mais altos de temperatura (por exemplo, 0,8) produzem saídas mais criativas e imprevisíveis, enquanto valores mais baixos (por exemplo, 0,2) geram saídas mais determinísticas e seguras.

- **Maximum length (comprimento máximo)**: limita o tamanho da resposta gerada pelo modelo. Você pode definir um número máximo de tokens (unidades de texto) que a resposta deve conter. Isso é útil para evitar que a saída seja muito longa e se ajustar às restrições do contexto em que o modelo está sendo usado.

- **Stop sequences (sequências de parada)**: são tokens que indicam ao modelo que ele deve parar de gerar texto. Isso é útil para controlar quando e onde a saída deve terminar.

- **Top P**: controla a proporção cumulativa das probabilidades dos tokens a serem considerados durante a geração de texto. Isso permite que você controle a diversidade da saída, garantindo que o modelo escolha entre uma seleção mais restrita de tokens com probabilidades mais altas.

- **Frequency penalty (penalidade de frequência)**: controla a frequência com que o modelo repete palavras ou frases semelhantes. Valores mais altos desencorajam o modelo a repetir as mesmas palavras ou estruturas, tornando a saída mais diversificada.

- **Presence penalty (penalidade de presença)**: influencia a diversidade da saída, mas de maneira diferente do frequency penalty. Valores mais altos incentivam o modelo a explorar mais possibilidades e produzir respostas menos óbvias e mais criativas.

Lembre-se de que a combinação desses parâmetros pode afetar significativamente o resultado gerado pelo modelo. Tente sempre experimentar diferentes configurações para atingir o tipo de saída desejada em suas interações com o modelo de linguagem.

<p align="right"><a href="#top-readme">(back to top)</a></p>

## Playground

O Playground, assim como a API da OpenAI, permitem a construção de assistentes de IA. Um Assistente possui instruções e pode usar modelos, ferramentas e conhecimento para responder a consultas de usuários. Já as threads são responsáveis por garantir que em um fluxo de troca de mensagens com os assistentes, seja possível acessar o histórico da troca de mensagens.

Para utilizar um assistente no PlayGround precisamos nos atentar a suas configurações:

- **Name (nome)**: refere-se à ao nome do assistente que está sendo criado. Geralmente destacamos um nome que faça sentido para o assistente. Por exemplo: "Analisador de reviews".

- **id (identificador do assistente)**: Logo abaixo do nome do assistente, após ser salvo, será apresentado um identificador alfanumérico que pode ser informado para a API da OpenAI. Esta chave garante que o assistente criado possa ser utilizado nas aplicações desenvolvidas utilizando a API. Por exemplo, `asst_3sMzyMxmXzvw9H9P4z1fNnQG`.

- **Instructions (instruções)**: referem-se às configurações iniciais do assistente, bem como às diretrizes que serão informadas ao assistente. Neste campo podemos definir personas, regras de interpretação dos conteúdos informados e especificar formatos de saída de resposta.

- **Model (modelo)**: refere-se à arquitetura específica do modelo de linguagem que você deseja usar. No Playground da OpenAI, você pode escolher entre vários modelos, cada um com diferentes capacidades de processamento de instruções e tamanhos de tokens. Você pode verificar [todos os modelos disponíveis e suas especificações na documentação da OpenAI](https://platform.openai.com/docs/models/models).

- **Tools (ferramentas)**: nos permitem criar ferramentas personalizadas para criar novas funcionalidades para os assistentes. Como por exemplo, utilizar Functions ou criar respostas com base em arquivos**.

- **Code Interpreter (interpretador de código)**: o Code Interpreter permite a execução de código Python em um ambiente isolado, processando e gerando arquivos que incluem dados, variáveis e métodos invocados para gerar a resposta para o usuário. Ele é capaz de resolver problemas complexos de código e matemática, iterando sobre um algoritmo até obter sucesso na execução.

- **Retrieval (recuperação)**: amplia o conhecimento do Assistente com informações externas, como dados de produtos ou documentos fornecidos pelos usuários. Ele implementa uma busca vetorial para recuperar conteúdos relevantes e responder a consultas dos usuários.

- **Functions Calling (chamada de funções)**: permitem descrever funções aos Assistentes e obter retornos inteligentes das funções. O Assistente pausa a execução durante uma Run quando invoca funções, e os resultados da chamada da função podem ser fornecidos para continuar a execução..

- **Files (arquivos)**: Arquivos podem ser anexados a Assistentes ou Mensagens e são utilizados pelo Code Interpreter e pelo Retrieval. O tamanho máximo do arquivo é de 512 MB.

### Formatos de arquivos suportados:

- **Textuais**: .c, .cpp, .html, .java, .json, .md, .php, .py, .rb, .tex, .txt, .css, .js, .ts, .xml
- **Multimídia**: .jpeg, .jpg, .gif, .png
- **Documentos**: .csv, .docx, .pdf, .pptx, .xlsx
- **Outros**: .tar, .zip

<p align="right"><a href="#top-readme">(back to top)</a></p>

# 04. Batch e Controle de Erros

## Caminho de Arquivos em Python

Quando trabalhamos com manipulação de arquivos em Python, é fundamental colocarmos corretamente o caminho dos arquivos para acessar e manipular dados localizados em diferentes pastas ou diretórios. O caminho indica o trajeto até o arquivo, permitindo que o interpretador Python localize e interaja com ele.

Durante a aula, estamos utilizando o seguinte caminho:

```
.
└── dados
│   ├──avaliacoes-Camisetas de algodão orgânico.txt 
│   ├──(...)
│   └── lista_de_compras_100_clientes.csv
analisador_sentimentos.py
```

Em que acessamos os arquivos de avaliações dentro da pasta `dados`, enquanto nosso arquivo `analisador_sentimentos.py` se encontra no diretório base do nosso projeto. O código então ficou da seguinte maneira:

```python
prompt_usuario = carrega(f"./dados/avaliacoes-{produto}.txt")

(...)

salva(f"./dados/analise-{produto}.txt", texto_resposta)
```

Certifique-se de sempre observar o seu diretório ao trabalhar com arquivos em Python, de modo a garantir que os caminhos sejam interpretados corretamente.

<p align="right"><a href="#top-readme">(back to top)</a></p>

## Códigos de Erro

Durante a aula vimos que a OpenAI disponibiliza uma lista de códigos de erros tanto da API quanto do Python em sua documentação. É essencial ter conhecimento sobre esses erros ao trabalhar com APIs, por várias razões, entre elas:

- **Resolução de problemas**: ao compreender os diferentes tipos de erros que podem ocorrer, você terá mais repertório para identificar e resolver problemas quando eles ocorrerem, sendo mais eficaz na depuração de problemas e na implementação de soluções.

- **Eficiência no desenvolvimento**: saber como lidar com os diferentes erros pode acelerar o desenvolvimento de aplicativos e serviços que utilizam a API. Quando você encontra um erro, saber qual é a causa provável e como corrigi-lo economiza tempo e esforço.

- **Melhorar a qualidade do código**: ao lidar com diferentes tipos de erros de maneira apropriada, você pode escrever um código mais robusto e resiliente, fazendo a implementação de tratamento de erros adequada e incluindo a lógica de fallback quando necessário.

- **Cumprimento de limites e políticas**: entender os erros relacionados a limites de taxa, limites de uso e autenticação é fundamental para garantir que você esteja agindo de acordo com as políticas e diretrizes estabelecidas pela API e pela plataforma de serviço.

### Erros

Em geral, ter conhecimento sobre esses erros não apenas ajuda a garantir um funcionamento mais suave das suas integrações com a API, mas também **contribui para a criação de sistemas mais confiáveis e eficazes**.

A seguir apresentamos alguns erros frequentes de API e do Python, listando sua possível causa e a solução.

### Erros de API

Uma visão geral dos erros que podem ocorrer com a API.

- `401 - Invalid Authentication`
  - **Causa**: a autenticação fornecida é inválida.
  - **Solução**: verifique se a chave de API correta e a organização solicitante estão sendo usadas. Certifique-se de que a autenticação esteja configurada corretamente para a chamada da API.

- `401 - Incorrect API key provided`
  - **Causa**: a chave de API fornecida não está correta.
  - **Solução**: verifique se a chave de API usada está correta. Se houver problemas persistentes, você pode tentar limpar o cache do navegador ou gerar uma nova chave de API válida.

- `401 - You must be a member of an organization to use the API`
  - **Causa**: sua conta não faz parte de uma organização.
  - **Solução**: entre em contato com a equipe de suporte da OpenAI para te adicionar em uma nova organização. Outra alternativa é pedir a alguém da sua organização para te convidar para fazer parte dela.

- `429 - Rate limit reached for requests`
  - **Causa**: você está enviando solicitações com muita rapidez, excedendo o limite da taxa.
  - **Solução**: diminua a velocidade das suas solicitações para cumprir os limites de taxa. Consulte o [guia de limite de taxa fornecido pela OpenAI](https://platform.openai.com/docs/guides/rate-limits) (em inglês) para entender as diretrizes.

- `429 - You exceeded your current quota, please check your plan and billing details`
  - **Causa**: você atingiu o limite máximo de gastos mensais (limite rígido) definido para sua conta.
  - **Solução**: se você deseja aumentar esse limite, pode solicitar um aumento de quota à OpenAI. Verifique também [seus detalhes de plano e faturamento](https://platform.openai.com/settings/organization/limits).

- `500 - The server had an error while processing your request`
  - **Causa**: houve um problema nos servidores da OpenAI ao processar sua solicitação.
  - **Solução**: espere por um curto período e tente enviar a solicitação novamente. Se o problema persistir, entre em contato com a equipe de suporte da OpenAI e verifique se há informações adicionais na [página de status da OpenAI](https://status.openai.com/).

- `503 - The engine is currently overloaded, please try again later`
  - **Causa**: os servidores da OpenAI estão enfrentando um alto tráfego e estão sobrecarregados.
  - **Solução**: aguarde por um curto período e tente novamente mais tarde. Isso geralmente ocorre quando há um grande volume de solicitações sendo processadas simultaneamente.

### Erros do Python

Aqui está uma descrição de cada um dos tipos de erros da biblioteca Python da OpenAI:

- `APIError`
  - **Causa**: ocorreu um problema do lado da OpenAI.
  - **Solução**: espere por um curto período e tente enviar a solicitação novamente. Se o problema persistir, entre em contato com a equipe de suporte da OpenAI. Esse erro geralmente indica uma falha interna nos servidores da OpenAI.

- `Timeout`
  - **Causa**: a solicitação atingiu o tempo limite.
  - **Solução**: espere por um curto período e tente enviar a solicitação novamente. Se o problema persistir, entre em contato com a equipe de suporte da OpenAI. Isso pode ocorrer quando a solicitação leva muito tempo para ser processada.

- `RateLimitError`
  - **Causa**: você atingiu o limite de taxa atribuído.
  - **Solução**: diminua a velocidade das suas solicitações para cumprir os limites de taxa. Consulte o guia de limite de taxa fornecido pela OpenAI para entender as diretrizes.

- `APIConnectionError`
  - **Causa**: houve um problema ao se conectar aos serviços da OpenAI.
  - **Solução**: verifique suas configurações de rede, configuração de proxy, certificados SSL ou regras de firewall. Certifique-se de que sua conexão com a Internet esteja funcionando corretamente.

- `InvalidRequestError`
  - **Causa**: sua solicitação estava malformada ou faltava alguns parâmetros obrigatórios, como um token ou entrada.
  - **Solução**: o erro deve fornecer detalhes sobre o erro específico. Consulte a documentação do método de API específico que você está chamando e verifique se você está enviando parâmetros válidos e completos. Verifique também a codificação, formato ou tamanho dos dados da sua solicitação.

- `AuthenticationError`
  - **Causa**: sua chave de API ou token era inválida, expirou ou foi revogada.
  - **Solução**: verifique sua chave de API ou token e certifique-se de que ela esteja correta e ativa. Se necessário, gere uma nova chave de API a partir do painel da sua conta.

- `ServiceUnavailableError`
  - **Causa**: ocorreu um problema nos servidores da OpenAI.
  - **Solução**: espere por um curto período e tente enviar a solicitação novamente. Se o problema persistir, entre em contato com a equipe de suporte da OpenAI e verifique se há informações adicionais na página de status da OpenAI. 

Certifique-se de sempre verificar a [documentação de erros](https://platform.openai.com/docs/guides/error-codes/error-code) da OpenAI quando surgirem dúvidas sobre algum código informado.

<p align="right"><a href="#top-readme">(back to top)</a></p>