import json
import os
from datetime import datetime

# Nome do arquivo JSON
FILENAME = 'motoristas.json'

class Motorista:
    def __init__(self, nome, cpf, genero, data_nascimento, celular, endereco, foto, email_verificado, celular_verificado):
        self.nome = nome
        self.cpf = cpf
        self.genero = genero
        self.data_nascimento = self._converter_data(data_nascimento)
        self.celular = celular
        self.endereco = endereco
        self.foto = foto
        self.email_verificado = email_verificado
        self.celular_verificado = celular_verificado

    def _converter_data(self, data_str):
        return datetime.strptime(data_str, '%d/%m/%Y').strftime('%Y-%m-%d')

    def to_dict(self):
        return {
            'nome': self.nome,
            'cpf': self.cpf,
            'genero': self.genero,
            'data_nascimento': self.data_nascimento,
            'celular': self.celular,
            'endereco': self.endereco,
            'foto': self.foto,
            'email_verificado': self.email_verificado,
            'celular_verificado': self.celular_verificado
        }

    @staticmethod
    def from_dict(d):
        return Motorista(
            d['nome'],
            d['cpf'],
            d['genero'],
            d['data_nascimento'],
            d['celular'],
            d['endereco'],
            d['foto'],
            d['email_verificado'],
            d['celular_verificado']
        )

# Função para carregar dados do arquivo JSON
def carregar_dados():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, 'r', encoding='utf-8') as file:
        return [Motorista.from_dict(item) for item in json.load(file)]

# Função para salvar dados no arquivo JSON
def salvar_dados(dados):
    with open(FILENAME, 'w', encoding='utf-8') as file:
        json.dump([motorista.to_dict() for motorista in dados], file, indent=4, ensure_ascii=False)

# Função para criar um novo motorista
def criar_motorista(nome, cpf, genero, data_nascimento, celular, endereco, foto, email_verificado, celular_verificado):
    dados = carregar_dados()
    novo_motorista = Motorista(nome, cpf, genero, data_nascimento, celular, endereco, foto, email_verificado, celular_verificado)
    dados.append(novo_motorista)
    salvar_dados(dados)
    print("Motorista criado com sucesso!")

# Função para ler todos os motoristas
def ler_motoristas():
    dados = carregar_dados()
    for motorista in dados:
        print(f"Nome: {motorista.nome}, CPF: {motorista.cpf}, Gênero: {motorista.genero}, Data de Nascimento: {motorista.data_nascimento}, Celular: {motorista.celular}, Endereço: {motorista.endereco}, Foto: {motorista.foto}, Email Verificado: {motorista.email_verificado}, Celular Verificado: {motorista.celular_verificado}")

# Função para atualizar um motorista pelo CPF
def atualizar_motorista(cpf, nome=None, genero=None, data_nascimento=None, celular=None, endereco=None, foto=None, email_verificado=None, celular_verificado=None):
    dados = carregar_dados()
    for motorista in dados:
        if motorista.cpf == cpf:
            if nome: motorista.nome = nome
            if genero: motorista.genero = genero
            if data_nascimento: motorista.data_nascimento = motorista._converter_data(data_nascimento)
            if celular: motorista.celular = celular
            if endereco: motorista.endereco = endereco
            if foto: motorista.foto = foto
            if email_verificado is not None: motorista.email_verificado = email_verificado
            if celular_verificado is not None: motorista.celular_verificado = celular_verificado
            salvar_dados(dados)
            print("Motorista atualizado com sucesso!")
            return
    print("Motorista não encontrado.")

# Função para deletar um motorista pelo CPF
def deletar_motorista(cpf):
    dados = carregar_dados()
    dados = [motorista for motorista in dados if motorista.cpf != cpf]
    salvar_dados(dados)
    print("Motorista deletado com sucesso!")

# Exemplos de uso das funções CRUD
if __name__ == '__main__':
    # Criando motoristas
    criar_motorista('Alice', '12345678901', 'Feminino', '01/01/1980', '11999999999', 'Rua A, 123', 'foto1.jpg', True, True)
    criar_motorista('Bob', '09876543210', 'Masculino', '02/02/1985', '11888888888', 'Rua B, 456', 'foto2.jpg', False, True)

    # Lendo motoristas
    print("Lista de motoristas:")
    ler_motoristas()

    # Atualizando um motorista
    atualizar_motorista('12345678901', nome='Alice Smith', email_verificado=False)

    # Lendo motoristas novamente para ver as alterações
    print("\nLista de motoristas atualizada:")
    ler_motoristas()

    # Deletando um motorista
    deletar_motorista('09876543210')

    # Lendo motoristas novamente para ver as alterações
    print("\nLista de motoristas após deleção:")
    ler_motoristas()
