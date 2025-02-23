import csv
from datetime import datetime

# Função para criar o arquivo CSV
def criar_csv():
    # Dados para o arquivo CSV
    registros = [
        ["João", "01/15/1990", "2025-02-23", "10:30"],
        ["Maria", "03/22/1985", "2025-02-23", "11:45"],
        ["Pedro", "07/04/1993", "2025-02-23", "14:00"],
        ["Ana", "12/30/1980", "2025-02-23", "09:15"],
        ["Carlos", "06/18/1992", "2025-02-23", "16:50"]
    ]

    # Escreve os registros no arquivo CSV
    with open('cadastros.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Nome", "Data de Nascimento", "Dia de Cadastro", "Hora de Cadastro"])  # Cabeçalho
        writer.writerows(registros)

# Função para ler o arquivo CSV e imprimir o registro solicitado
def ler_csv():
    # Lê o arquivo CSV
    with open('cadastros.csv', mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Ignora o cabeçalho

        # Solicita o número do registro ao usuário
        n = int(input("Digite o número do registro que deseja visualizar (1-5): "))

        # Imprime o registro solicitado
        for i, row in enumerate(reader, 1):
            if i == n:
                nome, data_nascimento, dia_cadastro, hora_cadastro = row
                # Formata a data no padrão brasileiro
                data_nascimento = datetime.strptime(data_nascimento, "%m/%d/%Y").strftime("%d/%m/%Y")
                dia_cadastro = datetime.strptime(dia_cadastro, "%Y-%m-%d").strftime("%d/%m/%Y")
                print(f"{nome} - Nascimento: {data_nascimento} - Cadastro: {dia_cadastro} {hora_cadastro}")
                break

# Cria o arquivo CSV
criar_csv()

# Lê e imprime o registro solicitado
ler_csv()
