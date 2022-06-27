from src.exceptions.cpf_duplicated_error import CpfDuplicatedError
from src.exceptions.funcionario_not_found_erro import FuncionarioNotFoundError
import mysql.connector
from src.entities.funcionarios import Funcionarios


class CadastroFuncionario():

    def incluir(self, funcionario: Funcionarios) -> None:
        cnx = mysql.connector.connect(user='root', password='Decode27@',
                                      host='127.0.0.1',
                                      database='holerite_xpto')
        cursor = cnx.cursor()

        query_cpf =  ("SELECT cpf FROM funcionarios")
        cursor.execute(query_cpf)
        list_cpfs = [elemento[0] for elemento in cursor.fetchall()]

        # compreensão de lista - list comprehension
        # lista_cpf = []
        # for elemento in cursor.fetchall():
        #     lista_cpf.append(elemento[0])

        if funcionario.cpf in list_cpfs:
            raise CpfDuplicatedError("Funcionário já existente, tente de novo.")
        else:
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

    def excluir(self,  matricula: str) -> None:
        cnx = mysql.connector.connect(user='root', password='Decode27@',
                                      host='127.0.0.1',
                                      database='holerite_xpto')
        cursor = cnx.cursor()

        self.consultar()

        query = ("DELETE FROM funcionarios WHERE matricula=%s")

        cursor.execute(query, [matricula])

        cnx.commit()

        cursor.close()
        cnx.close()

    def consultar(self,  matricula: str) -> Funcionarios:
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

    def alterar(self, matricula: str) -> None:
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


# funcionario = Funcionarios(5464, "nome", "12345678", "2020-01-03", "cargo", "sim")
# print(funcionario.nome)

# cadastro_funcionario = CadastroFuncionario()
# cadastro_funcionario.incluir(funcionario)

