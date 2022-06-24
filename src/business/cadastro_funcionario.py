from holerite.src.exceptions.funcionario_not_found_erro import FuncionarioNotFoundError
import mysql.connector
from holerite.src.entities.funcionarios import Funcionarios


class CadastroFuncionario():

    def incluir_funcionario(self, funcionario: Funcionarios) -> None:
        cnx = mysql.connector.connect(user='root', password='Decode27@',
                                      host='127.0.0.1',
                                      database='holerite_xpto')
        cursor = cnx.cursor()
        adiciona_funcionario = ("INSERT INTO funcionarios "
                            "(nome, cpf, admissao, cargo, comissao)"
                            " VALUES ( %(nome)s, %(cpf)s, %(admissao)s, %(cargo)s, %(comissao)s)")

        cursor.execute(adiciona_funcionario, {
            "nome": funcionario.nome,
            "cpf": funcionario.cpf,
            "admissao": funcionario.admissao,
            "cargo": funcionario.cargo,
            "comissao": funcionario.comissao,
        })

        cnx.commit()

        cursor.close()
        cnx.close()

    def excluir_funcionario(self,  matricula: str) -> None:
        cnx = mysql.connector.connect(user='root', password='Decode27@',
                                      host='127.0.0.1',
                                      database='holerite_xpto')
        cursor = cnx.cursor()

        self.consultar_funcionario()

        query = ("DELETE FROM funcionarios, WHERE matricula=%s")

        cursor.execute(query, [matricula])

        cnx.commit()

        cursor.close()
        cnx.close()

    def consultar_funcionario(self,  matricula: str) -> Funcionarios:
        cnx = mysql.connector.connect(user='root', password='Decode27@',
                                      host='127.0.0.1',
                                      database='holerite_xpto')
        cursor = cnx.cursor()

        query = ("SELECT matricula, nome, cpf, admissao, cargo, comissao FROM funcionarios WHERE matricula=%s")

        try:
            cursor.execute(query, [matricula])
            row = cursor.fetchone()

            if row != None:
                matricula, nome, cpf, admissao, cargo, comissao = row
                funcionario = Funcionarios(matricula, nome, cpf, admissao, cargo, comissao)

                cursor.close()
                cnx.close()
                return funcionario
        except:
            raise FuncionarioNotFoundError("Funcionario não encontrado.")

        cursor.close()
        cnx.close()

        return funcionario

    def alterar_nome_funcionario(self, matricula: str) -> None:
        cnx = mysql.connector.connect(user='root', password='Decode27@',
                                      host='127.0.0.1',
                                      database='holerite_xpto')
        cursor = cnx.cursor()

        query = ("SELECT matricula, nome, cpf, admissao, cargo, comissao FROM funcionarios WHERE matricula=%s")

        cursor.execute(query, [matricula])
        
        for (matricula, nome, cpf, admissao, cargo, comissao) in cursor:
            funcionario = Funcionarios(matricula, nome, cpf, admissao, cargo, comissao)
        else:
            raise FuncionarioNotFoundError("Funcionario não encontrado.")

    
        cursor.close()
        cnx.close()