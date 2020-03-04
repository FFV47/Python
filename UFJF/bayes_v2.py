

# definindo variáveis
import matplotlib.pyplot as plt
import scipy.stats as st
import numpy as np
N = 1000
# sorteando 1000 vezes uma moeda (valores 0 e 1) e calculando o mean
print("SORTEANDO E CALCULANDO VALOR MÉDIO")
data_coin_flips = np.random.randint(2, size=N)
print("VALOR MÉDIO:%f" % np.mean(data_coin_flips))
input("PRESS ENTER TO CONTINUE: ")

# fazendo o mesmo com a função binomial
PROB = 0.5
print("FAZENDO O MESMO COM A FUNÇÃO BINOMIAL")
bernoulli_flips = np.random.binomial(n=1, p=PROB, size=N)
print("VALOR MÉDIO:%f" % np.mean(bernoulli_flips))
input("PRESS ENTER TO CONTINUE: ")

# Essa é uma função simples mas Scipy tem muitas distribuições definidas
# repetindo com o pacote Scipy
print("PDF COM SCIPY")
print(st.bernoulli.pmf(1, PROB))
print(st.bernoulli.pmf(0, PROB))
input("PRESS ENTER TO CONTINUE: ")

# mas qual a probabilidade de ver os 1000 valores dos nossos dados??
# print(np.product(st.bernoulli.pmf(data_coin_flips, PROB)))
# mas qual a probabilidade de ver os 1000 valores dos nossos dados??

# print("%.4g" % np.product(st.bernoulli.pmf(data_coin_flips, PROB)))
# input("PRESS ENTER TO CONTINUE: ")

# Esse número por si śo não ajuda...precisamos de uma distribuição para o nosso
# problema...se PROB fosse diferente de 0.5? vamos fazer um vetor de valores...
print("DISTRIBUIÇÃO 1000 EVENTOS - USANDO UM VETOR DE VALORES")
# import seaborn as sns


PROBscan = np.linspace(0, 1, 100)

p_x = [np.product(st.bernoulli.pmf(data_coin_flips, p)) for p in PROBscan]
'''
plt.plot(PROBscan, p_x, "b")
plt.xlabel("PROB")
plt.ylabel("p_x")
#plt.xlim(0.4, 0.6)
plt.grid()
plt.figure(0)
plt.show(0)
#input("PRESS ENTER TO CONTINUE")
'''

# agora olhando para a distribuição a priori
print("DISTRIBUIÇÃO A PRIORI - NORMALIZAÇÃO")
fair_flips = benoulli_flips = np.random.binomial(n=1, p=PROB, size=N)
p_fair = np.array([np.product(st.bernoulli.pmf(fair_flips, p))
                   for p in PROBscan])
p_fair = p_fair / np.sum(p_fair)
plt.plot(PROBscan, p_fair, ":r")
# plt.plot(PROBscan, p_x, PROBscan, p_fair)
# plt.grid()
plt.figure(1)
plt.show()
# input("PRESS ENTER TO CONTINUE")

# essa distribuição acima seria o que esperamos dado que a moeda não é viciada.
# então essa distribuição representaria nosso conhecimento a priori.

# vamos agora considerar que nossa moeda no experimento É VICIADA

print("CONSIDERANDO MOEDA VICIADA")
PROBv = 0.8
unfair_flips = benoulli_flips = np.random.binomial(n=1, p=PROBv, size=N)
p_unfair = np.array([np.product(st.bernoulli.pmf(unfair_flips, p))
                     for p in PROBscan])
fig, axes = plt.subplots(2, 1, sharex=True)
axes[0].plot(PROBscan, p_unfair)
axes[0].set_title("Sampling Distribution")
axes[1].plot(PROBscan, p_fair)
axes[1].set_title("Prior Distribution")
plt.show()


# bem...temos uma situação....nosso conhecimento inicial apontava para uma
# distribuição e nosso experimento não está correspondendo...

# queremos saber P(p|X), ou seja, a probabilidade de nossos parâmetros
# (nesse caso apenas p) dado nossos dados

# Temos então que olhar a questão do conhecimento a posteriori....
# precisamos do Teorema de Bayes


print("POSTERIORI")

# RECOMEÇANDO EXPERIMENTO
n_pars = 100
n_sample = 100
true_p = 0.8
prior_p = 0.5
n_prior = 100

# PRIMEIRO SORTEIO...
pars = np.linspace(0, 1, n_pars)
sample = np.random.binomial(n=1, p=true_p, size=n_sample)
likelihood = np.array([np.product(st.bernoulli.pmf(sample, p)) for p in pars])
likelihood = likelihood/np.sum(likelihood)
prior_sample = np.random.binomial(n=1, p=prior_p, size=n_prior)
prior = np.array([np.product(st.bernoulli.pmf(prior_sample, p)) for p in pars])
prior = prior/np.sum(prior)
posterior = [prior[i]*likelihood[i] for i in range(prior.shape[0])]
posterior = posterior/np.sum(posterior)

fig, axes = plt.subplots(3, 1, sharex=True, figsize=(8, 8))
axes[0].plot(pars, likelihood)
axes[0].set_title("Sampling Distribution")
axes[1].plot(pars, prior)
axes[1].set_title("Prior Distribution")
axes[2].plot(pars, posterior)
axes[2].set_title("Posterior Distribution")
plt.show()


# SEGUNDO SORTEIO PRIOR = POSTERIOR
pars = np.linspace(0, 1, n_pars)
sample = np.random.binomial(n=1, p=true_p, size=n_sample)
likelihood = np.array([np.product(st.bernoulli.pmf(sample, p)) for p in pars])
likelihood = likelihood/np.sum(likelihood)
prior = posterior
posterior = [prior[i]*likelihood[i] for i in range(prior.shape[0])]
posterior = posterior/np.sum(posterior)

fig, axes = plt.subplots(3, 1, sharex=True, figsize=(8, 8))
axes[0].plot(pars, likelihood)
axes[0].set_title("Sampling Distribution")
axes[1].plot(pars, prior)
axes[1].set_title("Prior Distribution")
axes[2].plot(pars, posterior)
axes[2].set_title("Posterior Distribution")
plt.show()


# TERCEIRO SORTEIO
pars = np.linspace(0, 1, n_pars)
sample = np.random.binomial(n=1, p=true_p, size=n_sample)
likelihood = np.array([np.product(st.bernoulli.pmf(sample, p)) for p in pars])
likelihood = likelihood/np.sum(likelihood)
prior = posterior
posterior = [prior[i]*likelihood[i] for i in range(prior.shape[0])]
posterior = posterior/np.sum(posterior)

fig, axes = plt.subplots(3, 1, sharex=True, figsize=(8, 8))
axes[0].plot(pars, likelihood)
axes[0].set_title("Sampling Distribution")
axes[1].plot(pars, prior)
axes[1].set_title("Prior Distribution")
axes[2].plot(pars, posterior)
axes[2].set_title("Posterior Distribution")
plt.show()


#    return posterior

# example = bern_post()
#    print(example)


print("END")
# plt.show()
# plt.close()
