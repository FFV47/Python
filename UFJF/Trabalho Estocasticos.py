import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st

plt.close("all")

"""DISTRIBUIÇÃO A PRIORI, DADO IDEAL, VALOR ESPERADO"""

N = 1500
divx = 100
dado_1 = np.array([1, 2, 3, 4, 5, 6])
dado_2 = dado_1
eixoX = np.linspace(start=0, stop=1, num=divx)

dado_ideal = np.array(
    [dado_1[np.random.randint(6)] + dado_2[np.random.randint(6)] for i in range(0, N)]
)
DensiProb = [np.prod(st.bernoulli.pmf(dado_ideal == 7, i)) for i in eixoX]
DensiProb = DensiProb / np.sum(DensiProb)

plt.figure("PRIORI")
plt.plot(eixoX, DensiProb, antialiased=True, color="b")
plt.title("Distribuição a Priori")
plt.xlabel("Probabilidade")
plt.show()

"""DISTRIBUIÇÃO COM DADO VICIADO, O NUMERO 1 FOI SUBSTITUIDO POR 6"""

dado_1 = np.array([6, 2, 3, 4, 5, 6])
dado_2 = dado_1
dado_viciado = np.array(
    [dado_1[np.random.randint(6)] + dado_2[np.random.randint(6)] for i in range(0, N)]
)
DensiProb = [np.prod(st.bernoulli.pmf(dado_viciado == 7, i)) for i in eixoX]
DensiProb = DensiProb / np.sum(DensiProb)

plt.figure("POSTERIORI")
plt.plot(eixoX, DensiProb, antialiased=True, color="m")
plt.title("Distribuição a Posteriori")
plt.xlabel("Probabilidade")
plt.show()

"""UTILIZANDO O TEOREMA DE BAYES, OBSERVAREMOS O AJUSTE DO CONHECIMENTO A PRIORI DEVIDO AO LANÇAMENTO DO DADO VICIADO CONDICIONADO AO DADO IDEAL"""

"""PRIMEIRO SORTEIO"""

dado_1 = np.array([1, 2, 3, 4, 5, 6])
dado_2 = dado_1
dado_ideal = np.array(
    [dado_1[np.random.randint(6)] + dado_2[np.random.randint(6)] for i in range(0, N)]
)
priori = [np.prod(st.bernoulli.pmf(dado_ideal == 7, i)) for i in eixoX]
priori = priori / np.sum(priori)
dado_1 = np.array([6, 2, 3, 4, 5, 6])
dado_2 = dado_1
dado_viciado = np.array(
    [dado_1[np.random.randint(6)] + dado_2[np.random.randint(6)] for i in range(0, N)]
)
dado_real = [np.prod(st.bernoulli.pmf(dado_viciado == 7, i)) for i in eixoX]
dado_real = dado_real / np.sum(dado_real)
posteriori = [priori[i] * dado_real[i] for i in range(priori.shape[0])]
posteriori = posteriori / np.sum(posteriori)

fig, axes = plt.subplots(3, 1, num="PRIMEIRO SORTEIO", figsize=(10, 10))
axes[0].plot(eixoX, priori, "b")
axes[0].set_title("Distribuição a Priori")
axes[1].plot(eixoX, dado_real, "r")
axes[1].set_title("Distribuição Dado Viciado")
axes[2].plot(eixoX, posteriori, "g")
axes[2].set_title("Distribuição a Posteriori")
plt.show()

"""SEGUNDO SORTEIO"""

priori = posteriori
dado_viciado = np.array(
    [dado_1[np.random.randint(6)] + dado_2[np.random.randint(6)] for i in range(0, N)]
)
dado_real = [np.prod(st.bernoulli.pmf(dado_viciado == 7, i)) for i in eixoX]
dado_real = dado_real / np.sum(dado_real)
posteriori = [priori[i] * dado_real[i] for i in range(priori.shape[0])]
posteriori = posteriori / np.sum(posteriori)

fig, axes = plt.subplots(3, 1, num="SEGUNDO SORTEIO", figsize=(10, 10))
axes[0].plot(eixoX, priori, "b")
axes[0].set_title("Distribuição a Priori")
axes[1].plot(eixoX, dado_real, "r")
axes[1].set_title("Distribuição Dado Viciado")
axes[2].plot(eixoX, posteriori, "g")
axes[2].set_title("Distribuição a Posteriori")
plt.show()

"""TERCEIRO SORTEIO"""

priori = posteriori
dado_viciado = np.array(
    [dado_1[np.random.randint(6)] + dado_2[np.random.randint(6)] for i in range(0, N)]
)
dado_real = [np.prod(st.bernoulli.pmf(dado_viciado == 7, i)) for i in eixoX]
dado_real = dado_real / np.sum(dado_real)
posteriori = [priori[i] * dado_real[i] for i in range(priori.shape[0])]
posteriori = posteriori / np.sum(posteriori)

fig, axes = plt.subplots(3, 1, num="TERCEIRO SORTEIO", figsize=(10, 10))
axes[0].plot(eixoX, priori, "b")
axes[0].set_title("Distribuição a Priori")
axes[1].plot(eixoX, dado_real, "r")
axes[1].set_title("Distribuição Dado Viciado")
axes[2].plot(eixoX, posteriori, "g")
axes[2].set_title("Distribuição Posteriori")
plt.show()
