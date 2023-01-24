from acesso_cep import BuscaEndereco
from datas_br import DatasBR
from TelefonesBR import telefoneBr
from cpf_cnpj import Documento, DocCpf, DocCNPJ

insira_telefone = input("insira o seu telefone")
objeto_telefone = telefoneBr(insira_telefone)
telefone_formatado = objeto_telefone.format_numero()

insira_CPF = input("Insira seu CPF")
objeto_CPF = Documento.cria_documento(insira_CPF)

insira_cep = input("Insira o seu cep")
objeto_cep = BuscaEndereco(insira_cep)
logradouro, bairro, cidade, uf = objeto_cep.acessa_via_cep()

cadastra_ano = DatasBR()
formata_data = cadastra_ano.mes_cadastro()
print(logradouro, bairro, cidade, uf)
print(telefone_formatado)
print(f'cadastrado em {formata_data}')
print(objeto_CPF)
