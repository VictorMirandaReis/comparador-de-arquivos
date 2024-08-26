def ler_arquivo(arquivo):
    with open(arquivo, 'r') as arquivo:
        return [linha.strip() for linha in arquivo.readlines()]

def escrever_arquivo(arquivo, linha):
    with open(arquivo, 'w') as arquivo:
        for linha in linha:
            arquivo.write(f"{linha}\n")

arquivo_a_ = ler_arquivo('arquivo_a_.txt')
arquivo_b_ = ler_arquivo('arquivo_b_.txt')

linhas = []

tamanho_linhas_a = len(arquivo_a_)
tamanho_linhas_b = len(arquivo_b_)
tamanho_linhas = max(tamanho_linhas_a, tamanho_linhas_b)

for linha in range(tamanho_linhas):
    linha_a = arquivo_a_[linha] if linha < tamanho_linhas_a else None
    linha_b = arquivo_b_[linha] if linha < tamanho_linhas_b else None

    if linha_a and linha_b:
        if linha_a == linha_b:
            linhas.append(linha_a)
        else:
            linhas.append(f"+ {linha_a}")
            linhas.append(f"- {linha_b}")
    elif linha_a:
        linhas.append(f"+ {linha_a}")
    elif linha_b:
        linhas.append(f"- {linha_b}")
    else:
        break

escrever_arquivo('arquivo_c_.txt', linhas)

print("O arquivo 'arquivo_c_.txt' foi criado com sucesso.")
