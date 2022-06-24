from flask import Flask, jsonify, request
from business.cadastro_funcionario import CadastroFuncionario
from entities.funcionarios import Funcionarios

app = Flask(__name__)

cadastro_funcionario = CadastroFuncionario()

@app.route("/funcionario", methods=['POST'])
def incluir_funcionario():
    dados = request.json

    funcionario = Funcionarios(
        dados['nome'], 
        dados['cpf'], 
        dados['admissao'], 
        dados['cargo'], 
        dados['comissao']
    )

    cadastro_funcionario.incluir(funcionario)

    return "ok", 201

@app.route("/funcionario/<matricula>", methods=['DELETE'])
def excluir_funcionario(matricula):
    cadastro_funcionario.excluir(matricula)

    return "deleted", 204

@app.route("/funcionario/<matricula>", methods=['GET'])
def consultar_funcionario(matricula):
    funcionario = cadastro_funcionario.consultar(matricula)

    return jsonify(funcionario)
