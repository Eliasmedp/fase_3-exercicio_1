import sys
sys.path.append('c:\\repositorio\\fase3\\exercicio1\\src\domain')

import uuid
from datetime import date
from enums.genero_enum import GeneroEnum
from config.config_atributos import *
from validators.string_obrigatorio_validador import StringObrigatorioValidador

class Usuario():
    def __init__(self, nome: str, email: str, senha: str, celular1: str, data_de_nascimento: date, cpf: str, genero: GeneroEnum, celular2: str = None, id: uuid=None) -> None:
        if not id:
            id = uuid.uuid4()

        self.id: str = uuid.uuid4()
        self.nome: str = nome
        self.email: str = email
        self.senha: str = senha
        self.celular: str = celular1
        self.celular2: str = celular2
        self.data_de_nascimento: date = data_de_nascimento
        self.cpf: str = cpf
        self.genero: GeneroEnum = genero

    def valida_cpf(self):
        StringObrigatorioValidador.validate(self.cpf, "CPF do Usuário", tamanho_exato=TAM_CPF)
        # depois verifica se o cpf tem digito verificador valido

  
    def valida_email(self):
        StringObrigatorioValidador().validate(self.email, "Email do Usuário", tamanho_maximo=TAM_MAX_EMAIL)
        if ("@" not in self.email):
            raise Exception("Campo e-mail deve ser válido. Deve possuir um @")

    def valida_data_de_nasc(self):
        if (type(self.data_de_nascimento) != date):
            raise Exception("Data deve ser DD/MM/AAAA")

    def valida_senha(self):
        StringObrigatorioValidador().validate(self.senha, "Senha do Usuário", tamanho_maximo=TAM_MAX_SENHA)

    def valida_nome(self):
        StringObrigatorioValidador().validate(self.nome, "Nome do Usuário", tamanho_maximo=TAM_MAX_NOME)
        self.nome = self.nome.strip()
        self.nome = self.nome.replace("  ", " ")

    def valida(self):
        self.valida_cpf()
        self.valida_nome()
        self.valida_email()
        self.valida_data_de_nasc()
        self.valida_senha()
        StringObrigatorioValidador().validate(self.celular, "Celular do Usuário", tamanho_exato=TAM_CELULAR)

        if (self.celular2 != None):
            StringObrigatorioValidador().validate(self.celular2, tamanho_exato=TAM_CELULAR)

        if not self.genero in (GeneroEnum):
            raise Exception("Gênero inválido")



""" usuario = Usuario(cpf="00000000000", nome="patricia  dos  anjos", email="None", senha="None", celular1="99999999999", data_de_nascimento=None, genero=None, celular2=None)
usuario.valida_nome()
print (usuario.nome) """