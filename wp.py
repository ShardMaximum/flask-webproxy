from flask import Flask, request, Response, render_template
from datetime import datetime               #Usado só pro log
import requests, json

app = Flask(__name__)

#Carregar os arquivos JSON
with open("blocked.json", "r") as blockfile:
    blocklist = json.load(blockfile)

with open("words.json", "r") as wordsfile:
    filtro = json.load(wordsfile)

@app.route('/<path:url>')                   #path é um str que aceita barras
def proxy(url):
    if not url:
        return "Informe uma URL", 400

    try:
        resposta = requests.get(url)
        acao = "Permitido"

        res_txt = str(resposta.content)     #resposta.content tem o tipo bytes. quando converte acaba vindo uns caracteres estranhos junto

        if url in blocklist["blocked"]:
            acao = "Bloqueado"
        else:
            for (word, changeword) in filtro.items():   #Confere cada palavra do filtro
                if word in res_txt.lower():             #.lower() devia deixar case insensitive
                    res_txt = res_txt.replace(word, changeword)
                    acao = "Filtrado"                   #Mudança no ação para registrar no log que foi filtrado

        with open("log.txt","a") as log:    #Registro no log. Se o arquivo não existe, simplesmente cria um novo automaticamente
            acesso = str(datetime.now()) + " - " + url + " - " + acao + "\n"
            log.write(acesso)

        if acao == "Bloqueado":
            return render_template("./blocked.html")    #Se recebeu um acesso a um site bloqueado, simplesmente renderiza uma página pronta

        return Response(
            res_txt,
            status=resposta.status_code,
            content_type=resposta.headers.get('Content-Type')
        )

    except requests.exceptions.RequestException as e:
        return f"Erro: {e}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)