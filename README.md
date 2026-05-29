# Webproxy com Flask

Trabalho da disciplina de Sistemas para Internet 2.
Feito por Vitor Rocha

## Como usar

- Clone o repositório com `git clone https://github.com/ShardMaximum/flask-webproxy` ou baixe os arquivos da forma que preferir
- Crie um ambiente virtual do Python: `python -m venv .venv`
- Ative o ambiente virtual. O script necessário depende do shell que está usando
- Instale as dependências (Flask e request) com `pip install flask request`
- Adicione os sites que deseja bloquear dentro do array `"blocked"` em `blocked.json`
- Adicione as palavras a serem filtradas em `words.json`, com o formato `"palavra recebida": "palavra alterada"`
- Execute o arquivo wp.py para iniciar o servidor
- Acesse as páginas na web através do proxy usando `localhost:8080/url.do.site`

## Sobre o desenvolvimento

- Testado no Python 3.11.5
- ChatGPT foi usado para desenvolver a parte de requests. O prompt usado está disponível em `ai_prompts.pdf` e apenas partes do código gerado foram usadas.
- Haverão muitos erros na exibição das páginas...
