def notas(*n, sit=False):
    """Função para analisar notas e situações de varios alunos

    Args:
        n: uma ou mais notas do aluno
        sit (bool, optional): Mostra a situaçao do aluno. Defaults to False.

    Returns:
        [dict]: Retorna um dicionario com varias informações sobre o aluno
    """
    dados = dict()
    dados["total"] = len(n)
    dados["maior"] = max(n)
    dados["menor"] = min(n)
    dados["media"] = sum(n) / len(n)
    if sit is False:
        return dados
    else:
        if dados["media"] > 7:
            dados["situaçao"] = "BOA"
        elif 5 <= dados["media"] <= 7:
            dados["situaçao"] = "RAZOAVEL"
        else:
            dados["situaçao"] = "RUIM"
        return dados


print("-" * 60)
resp = notas(4.12, 6.12, 8.67, 3.45, 9, 8, 10, 10, 0, 0, 0, 0, sit=True)
print(resp)
help(notas)
print()
