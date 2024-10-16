<div name="top-readme" align=center>
  <h1>Python e GPT</h1>
</div>

CURSO ALURA | Python e GPT: crie seu chatbot com IA

---

# 📌 Table of Contents

- [01. Playground e a API da OpenAI](#01-playground-e-a-api-da-openai)
  - [Parâmetros do Palyground](#parâmetros-do-palyground)
  - [Playground](#playground)

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