def posicaoNome(nomeBusca, nomes):
    posicao = 0
    tamanho = len(nomes)
    for nome in nomes:
        if(nome == nomeBusca):
            break
        else:
            posicao += 1
            if (posicao == tamanho):
                posicao = -1
    return posicao

alunos = ["joão", "maria", "josé"]
posicao = posicaoNome("helena", alunos)
print("Posição: ", posicao)
