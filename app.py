from src import *
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)



@cross_origin
@app.route('/conta/criarConta',methods=['POST'])
def rota_criar_conta():
    pass


@cross_origin
@app.route('/conta/logarConta',methods=['POST'])
def rota_logar_conta():
    pass


@cross_origin
@app.route('/conta/alterarConta',methods=['PUT'])
def rota_alterar_conta():
    pass


@cross_origin
@app.route('/conta/excluirConta',methods=['DELETE'])
def rota_excluir_conta():
    pass