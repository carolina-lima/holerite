class Funcionarios():

    def __init__(self, matricula: str, nome: str, cpf: str, admissao: None, cargo: str, comissao: bool):
        self.__matricula = matricula
        self.__nome = nome
        self.__cpf = cpf
        self.__admissao = admissao
        self.__cargo = cargo
        self.__comissao = comissao

    @property
    def matricula(self) -> str:
        return self.__matricula

    @property
    def nome(self) -> str:
        return self.__nome
    
    @property
    def cpf(self) -> str:
        return self.__cpf
    
    @property
    def admissao(self) -> str:
        return self.__admissao

    @property
    def cargo(self) -> str:
        return self.__cargo
    
    @property
    def comissao(self) -> str:
        return self.__comissao