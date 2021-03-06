from flask import Blueprint
from flask import  jsonify, request
from src.business.cadastro_funcionario import CadastroFuncionario
from src.entities.funcionarios import Funcionarios
from src.exceptions.cpf_duplicated_error import CpfDuplicatedError


funcionario = Blueprint('funcionario',__name__)

cadastro_funcionario = CadastroFuncionario()

@funcionario.route("/funcionario", methods=['POST'])
def incluir_funcionario():
    dados = request.json

    funcionario = Funcionarios(
        dados['matricula'],
        dados['nome'], 
        dados['cpf'], 
        dados['admissao'], 
        dados['cargo'], 
        dados['comissao']
    )
    
    try:
        cadastro_funcionario.incluir(funcionario)
    except CpfDuplicatedError:
        return "cpf duplicado", 400 #encontrar um return adequado

    return "ok", 201

@funcionario.route("/funcionario/<matricula>", methods=['DELETE'])
def excluir_funcionario(matricula):
    cadastro_funcionario.excluir(matricula)

    return "deleted", 204

@funcionario.route("/funcionario/<matricula>", methods=['GET'])
def consultar_funcionario(matricula):
    funcionario = cadastro_funcionario.consultar(matricula)

    return jsonify(funcionario)
