from flask import Flask, request, Response, render_template
import requests, json

app = Flask(__name__)

with open("blocked.json", "r") as blockfile:
    blocklist = json.load(blockfile)

with open("words.json", "r") as wordsfile:
    filter = json.load(wordsfile)

@app.route('/<path:url>')
def proxy(url):
    if not url:
        return "Informe uma URL", 400

    try:
        resposta = requests.get(url)

        if url in blocklist["blocked"]:
            return render_template("./blocked.html")

        return Response(
            resposta.content,
            status=resposta.status_code,
            content_type=resposta.headers.get('Content-Type')
        )

    except requests.exceptions.RequestException as e:
        return f"Erro: {e}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)