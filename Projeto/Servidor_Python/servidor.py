from flask import Flask, request, send_file, jsonify
from gerar_doc import criar_doc
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['POST'])
def index():
    dados = request.get_json()
    if 'texto' in dados:
        Texto = dados['texto']
        criar_doc(Texto)
        response = send_file('Documentacao.docx')
        return response
    else:
        return jsonify({'error': 'JSON inválido: a tag "texto" é necessária.'}), 400

if __name__ == '__main__':
    app.run()