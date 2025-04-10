# -*- coding: utf-8 -*-
"""codigo-eduardo-inteligencia-comp-fuzzy.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ch78vA_oZ877g4ZKzcj_k9wL-5Uk_ptd
"""

!pip install scikit-fuzzy

import matplotlib.pyplot as plt
import skfuzzy as fuzz
import numpy as np

x_superficie = np.arange(0,6,1)
x_sujeira = np.arange(0,6,1)
x_succao = np.arange(0,11,1)

x_superficie, x_sujeira, x_succao

"""# Superfície"""

y_superficie_dificil = fuzz.trimf(x_superficie,[2.5, 5, 5])
y_superficie_moderada = fuzz.trimf(x_superficie,[0, 2.5, 5])
y_superficie_facil = fuzz.trimf(x_superficie,[0, 0, 2.5])

y_superficie_facil, y_superficie_moderada,y_superficie_dificil

x_superficie, y_superficie_facil

plt.plot(x_superficie,y_superficie_facil, 'bo', label='grafico da superficie fácil')
plt.plot(x_superficie,y_superficie_facil)
plt.legend();

x_superficie, y_superficie_moderada

plt.plot(x_superficie,y_superficie_moderada, 'bo', label='grafico da superficie moderada')
plt.plot(x_superficie,y_superficie_moderada)
plt.legend();

x_superficie, y_superficie_dificil

plt.plot(x_superficie, y_superficie_dificil, 'bo', label='grafico da superficie difícil')
plt.plot(x_superficie, y_superficie_dificil)
plt.legend();

fig, ax8 = plt.subplots(figsize = (8, 5))
ax8.plot(x_superficie, y_superficie_dificil,  'r', label='difícil')
ax8.plot(x_superficie, y_superficie_moderada,  'g', label='moderada')
ax8.plot(x_superficie, y_superficie_facil,  'b', label='fácil')


ax8.set_title('Intercecção Superfície')
ax8.legend();

"""# Sujeira"""

y_sujeira_pesada = fuzz.trimf(x_superficie,[2.5, 5, 5])
y_sujeira_moderada = fuzz.trimf(x_superficie,[0, 2.5, 5])
y_sujeira_leve = fuzz.trimf(x_superficie,[0, 0, 2.5])

y_sujeira_leve,y_sujeira_moderada,y_sujeira_pesada

plt.plot(x_sujeira,y_sujeira_leve, 'bo', label='leve')
plt.plot(x_sujeira,y_sujeira_leve)
plt.legend();

x_sujeira, y_sujeira_moderada

plt.plot(x_sujeira,y_sujeira_moderada, 'bo', label='moderada')
plt.plot(x_sujeira,y_sujeira_moderada)
plt.legend();

x_sujeira, y_sujeira_pesada

plt.plot(x_sujeira,y_sujeira_pesada, 'bo', label='pesada')
plt.plot(x_sujeira,y_sujeira_pesada)
plt.legend();

fig, ax9 = plt.subplots(figsize = (8, 5))
ax9.plot(x_sujeira, y_sujeira_leve,  'b', label='leve')
ax9.plot(x_sujeira, y_sujeira_moderada,  'g', label='moderada')
ax9.plot(x_sujeira, y_sujeira_pesada,  'r', label='pesada')
ax9.set_title('Sujeira')
ax9.legend();

"""# Sucção"""

y_succao_baixa = fuzz.trimf(x_succao, [0,0,5])
y_succao_media = fuzz.trimf(x_succao, [0,5,10])
y_succao_alta = fuzz.trimf(x_succao, [5,10,10])

y_succao_baixa, y_succao_media, y_succao_alta

x_succao, y_succao_baixa

plt.plot(x_succao,y_succao_baixa, 'bo', label='baixa')
plt.plot(x_succao,y_succao_baixa)
plt.legend();

x_succao, y_succao_media

plt.plot(x_succao,y_succao_media, 'bo', label='media')
plt.plot(x_succao,y_succao_media)
plt.legend();

x_succao, y_succao_alta

plt.plot(x_succao,y_succao_alta, 'bo', label='alta')
plt.plot(x_succao,y_succao_alta)
plt.legend();

fig, axS = plt.subplots(figsize = (8, 5))
axS.plot(x_succao, y_succao_alta,  'r', label='alta')
axS.plot(x_succao, y_succao_media,  'g', label='media')
axS.plot(x_succao, y_succao_baixa,  'b', label='baixa')


axS.set_title('Sucção')
axS.legend();

superficie_nivel_dificil = fuzz.interp_membership(x_superficie, y_superficie_dificil, 4.0)
superficie_nivel_moderada = fuzz.interp_membership(x_superficie, y_superficie_moderada, 4.0)
superficie_nivel_facil = fuzz.interp_membership(x_superficie, y_superficie_facil, 4.0)

superficie_n_facil,superficie_n_moderada,superficie_n_dificil

sujeira_nivel_pesada = fuzz.interp_membership(x_sujeira, y_sujeira_pesada, 3.0)
sujeira_nivel_moderado = fuzz.interp_membership(x_sujeira, y_sujeira_moderada, 3.0)
sujeira_nivel_leve = fuzz.interp_membership(x_sujeira, y_sujeira_leve, 3.0)

sujeira_nivel_leve,sujeira_nivel_moderado,sujeira_nivel_pesada

"""# Regras

# Regra 1 : Se a superfície for fácil e a sujeira for leve então a sucção será baixa
"""

superficie_nivel_facil,sujeira_nivel_leve

regranumero1 = np.fmax(superficie_nivel_facil, sujeira_nivel_leve)
aciona_succao_baixa = np.fmin(regranumero1, y_succao_baixa)

regranumero1,aciona_succao_baixa

"""# Regra 2 : Se a superfície for moderada e a sujeira for leve então a sucção será média"""

superficie_nivel_moderada, sujeira_nivel_leve

regranumero2 = np.fmax(superficie_nivel_moderada, sujeira_nivel_leve)
aciona_succao_media = np.fmin(regranumero2, y_succao_media)

regranumero2, aciona_succao_media

superficie_nivel_dificil, sujeira_nivel_pesada

regranumero3 = np.fmax(superficie_nivel_dificil, sujeira_nivel_pesada)
aciona_succao_alta = np.fmin(regranumero3, y_succao_alta)

regranumero3, aciona_succao_alta

"""Regra 4:  Se a superfície for moderada então a sucção será média

# 1ª maneira
"""

regranumero4 = np.fmax(superficie_nivel_moderada, sujeira_nivel_moderado)
aciona_succao_media = np.fmin(regranumero4, y_succao_media)

regranumero4 , aciona_succao_media

"""# 2ª maneira"""

regranumero4 = aciona_succao_media

regranumero4

"""# Gráfico com as interesecções"""

x_succao0 = np.zeros_like(x_succao)
x_succao0

fig,ax8 = plt.subplots(figsize=(8,3))
ax8.fill_between(x_succao, x_succao0, aciona_succao_alta,facecolor='r', alpha=0.7)
ax8.plot(x_succao,y_succao_alta,'r',linewidth=0.5,linestyle='--'),
ax8.fill_between(x_succao, x_succao0, aciona_succao_media,facecolor='g', alpha=0.7)
ax8.plot(x_succao, y_succao_media,'g',linewidth=0.5,linestyle='--'),
ax8.fill_between(x_succao, x_succao0, aciona_succao_baixa,facecolor='b', alpha=0.7)
ax8.plot(x_succao,y_succao_baixa,'b',linewidth=0.5,linestyle='--')


ax8.set_title('Saída das atividades interligadas');

"""# Defuzzificação

1.   centroid(centroid)

2.   bisector(bisector)

3.   mean of maximum(mom)

4.   min of maximum(som

5.   max of maximum(lom)






"""

controle = np.fmax(aciona_succao_baixa, np.fmax(aciona_succao_media,aciona_succao_alta))

controle

aciona_succao_baixa

aciona_succao_media

a_succao_alta

np.fmax(aciona_succao_media, aciona_succao_alta)

succao = fuzz.defuzz(x_succao,controle,'centroid')
succao2 = fuzz.defuzz(x_succao,controle,'bisector')
succao3 = fuzz.defuzz(x_succao,controle,'mom')
succao4 = fuzz.defuzz(x_succao,controle,'som')
succao5 = fuzz.defuzz(x_succao,controle,'lom')
print("Resultado com o método centroid:", succao)
print("Resultado com o método bisector:", succao2)
print("Resultado com o método mom:", succao3)
print("Resultado com o método som:", succao4)
print("Resultado com o método lom:", succao5)

succao_ativacao = fuzz.interp_membership(x_succao,controle, succao)

succao_ativacao

fig,ax8 = plt.subplots(figsize=(8,3))

ax8.plot(x_succao,y_succao_alta,'r',linewidth=0.5,linestyle='--'),
ax8.plot(x_succao, y_succao_media,'g',linewidth=0.5,linestyle='--'),
ax8.plot(x_succao,y_succao_baixa,'b',linewidth=0.5,linestyle='--')


ax8.fill_between(x_succao, x_succao0, controle ,facecolor='#FFFF00', alpha=0.7)
ax8.set_title('Resultado após a defuzzificação')
ax8.plot([succao,succao], [0, succao_ativacao],'pink', linewidth = 1.5, alpha=0.9)

print("(Poder de Sucção) - Resultado: (LINHA)  ", succao)