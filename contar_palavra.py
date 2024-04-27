def contar_palavras_unicas(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        palavras = arquivo.read().split()
        palavras_unicas = set(palavras)
        return len(palavras_unicas)
print(contar_palavras_unicas('texto.txt'))
