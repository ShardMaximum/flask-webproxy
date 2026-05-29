from flask import Flask, request, Response
import requests, json

#json.load

app = Flask(__name__)

@app.route('/<path:url>')
def proxy(url):
    if not url:
        return "Informe uma URL", 400

    try:
        resposta = requests.get(url)

        return Response(
            resposta.content,
            status=resposta.status_code,
            content_type=resposta.headers.get('Content-Type')
        )

    except requests.exceptions.RequestException as e:
        return f"Erro: {e}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)