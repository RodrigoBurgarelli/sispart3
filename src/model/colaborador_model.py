from src.model import db # essa linha traz a instância SQLAlchemy para este arquivo
from sqlalchemy.schema import Column # Traz o recurso que transforma atributos em colunas
from sqlalchemy.types import String, DECIMAL, Integer #Traz o recurso que identifica os tipos de dados para as colunas

class Colaborador(db.Model): # db.Model serve para mapear essa classe
    
    # ----------------------Atributos------------------------
    id = Column(Integer, primary_key=True, autoincrement=True) # igual ir no banco de ados e estipuar id INT AUTO_INCREMENT PRIMARYKEY
    
    nome = Column(String(255)) #igual a ir no banco de dados e estipular VARCHAR(255)
    email = Column(String(150))
    senha = Column(String(255))
    cargo = Column(String(100))
    salario = Column(DECIMAL(10,2))
    
    # -------------------------------------- nesse bloco tudo que está dentro vai criar as colunas na tabela banco de dados---------------
    
    # ----------- Construtor --------------
    
    def __init__(self, nome, email, senha, cargo, salario):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.cargo = cargo
        self.salario = salario
    # -------------------- nesse bloco irá criar o que está dentro das linhas
    
    def to_dict(self) -> dict:
        return {
            'email': self.email,
            'senha': self.senha,
        }