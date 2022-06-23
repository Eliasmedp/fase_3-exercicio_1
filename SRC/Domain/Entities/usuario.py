from datetime import date
import uuid
from SRC.Domain.Enums.opcaoGeneroEnum import Genero
from SRC.Domain.Config.config_atributos import IDADE_MINIMA, TAMANHO_MAX_NOME
from SRC.Domain.Validators.data_validator import DataValidator
from SRC.Domain.Validators.string_validator import ValidaString
from transfero_validators.validators import CPFValidator, EmailValidator, CelularValidator, SenhaValidator
from calendar import isleap

class Usuario:
    def __init__(self, nome : str, email : str, senha : str, celular1 : str, data_nasc : date, cpf : str, genero : Genero, celular2 : str = None, id : uuid = None) -> None:
        if not id:
            id = uuid.uuid1()

        self.id : str = id
        self.nome : str = nome
        self.email : str = email
        self.senha : str = senha
        self.celular1 : str = celular1
        self.celular2 : str = celular2
        self.data_nasc : date = data_nasc
        self.cpf : str = cpf
        self.genero : Genero = genero

    def valida_nome(self):
        ValidaString.valida_string(self.nome, 'Nome do Usuário', tamanho_maximo=TAMANHO_MAX_NOME)
        self.nome = self.nome.strip()
        self.nome = self.nome.replace('  ', ' ')
    

    def valida_idade(self):
        if not isinstance(self.data_nasc, date):
            raise Exception('Data precisa ser do tipo date.')
        
        data_atual = date.today()
        idade_usuario = (data_atual.year - self.data_nasc.year - ((data_atual.day, data_atual.month) < (self.data_nasc.day, self.data_nasc.month)))

        if idade_usuario < IDADE_MINIMA:
            raise Exception (f"Idade mínima aceita: {IDADE_MINIMA} anos.")
    
    def valida(self):
        self.valida_nome()
        self.valida_idade()
        CPFValidator.valida(self.cpf)
        EmailValidator.valida(self.email)
        CelularValidator.valida(self.celular1)
        SenhaValidator.valida(self.senha)

        if (self.celular2 != 0):
            CelularValidator.valida(self.celular2)
        
        if not self.genero in Genero:
            raise Exception ('Gênero inválido.')
