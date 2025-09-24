########################
### Install Packages ###
########################

import subprocess
import sys

def install_packages(pacotes):
    for pacote in pacotes:
        subprocess.check_call([sys.executable, "-m", "pip", "install", pacote])

# List of packages
packages_list = ["numpy", "pandas", "matplotlib", "scipy", "seaborn","statsmodels", "plotly", "gurobipy",
"yfinance", "scikit-learn", "panel", "datashader", "param", "colorcet", "transformers","einops","accelerate", 
"bitsandbytes", "openpyxl"]

install_packages(packages_list)

#####################
### Load Packages ###
#####################

import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import plotly.express as px
import tensorflow as tf
import tensorflow_probability as tfp
import arviz as az
import IPython
from matplotlib.colors import LinearSegmentedColormap
from scipy.stats import skew 
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.tools.tools import add_constant

######################################
### Análise Exploratória dos Dados ###
######################################

df = pd.read_csv("https:/drive.google.com/uc?export=download&id=1Xa631th1GeU4OVmGW33UckDWJgj5E8VL")
df 

df.describe()

df.dtypes

#################################
### Presença de Valores Nulos ###
#################################

# - Eliminando Valores
# - Substituir pela Média
# - Substituir pela Mediana (Caso os dados não sejam assimétricos)

df.isnull().sum()

df.count()

# Eliminando Valores Nulos
# df = df.dropna(subset=['TV_Spend'])
# df = df.dropna(subset=['Radio_Spend'])
# df = df.dropna(subset=['Sales']) 

# Substituindo pela Média
df['TV_Spend'] = df['TV_Spend'].fillna(df['TV_Spend'].mean())
df['Radio_Spend'] = df['Radio_Spend'].fillna(df['Radio_Spend'].mean())
df['Sales'] = df['Sales'].fillna(df['Sales'].mean())

# Substituindo pela Meridiana
# df['TV_Spend'] = df['TV_Spend'].fillna(df['TV_Spend'].median())
# df['Radio_Spend'] = df['Radio_Spend'].fillna(df['Radio_Spend'].median())
# df['Sales'] = df['Sales'].fillna(df['Sales'].median())

df.count()

#########################
### Tratando Outliers ###
#########################

plt.hist(x = df['Sales'])
plt.show()

plt.hist(x = df['TV_Spend'])
plt.show()

plt.hist(x = df['Radio_Spend'])
plt.show()

plt.hist(x = df['Digital_Spend'])
plt.show()

plt.hist(x = df['OOH_Spend'])
plt.show()

plt.hist(x = df['Competitor_Price'])
plt.show()

plt.hist(x = df['Promo_Flag'])
plt.show()

plt.hist(x = df['Region'])
plt.show()

df[df["Sales"] >= 10000]
df[df["TV_Spend"] >= 20000]

media = df['Sales'].mean()
print(f"Média: {media}")
# 3543.527771633722

media = df['TV_Spend'].mean()
print(f"Média: {media}")
# 5139.619781506285

# Substituir os valores pela média da coluna 'Sales'
df.loc[35, 'Sales'] = 3543.527771633722
df.loc[216, 'Sales'] = 3543.527771633722
df.loc[473, 'Sales'] = 3543.527771633722
df.loc[515, 'Sales'] = 3543.527771633722
df.loc[877, 'Sales'] = 3543.527771633722

# Substituir os valores pela média da coluna 'TV_Spend'
df.loc[177, 'TV_Spend'] = 5139.619781506285
df.loc[386, 'TV_Spend'] = 5139.619781506285
df.loc[768, 'TV_Spend'] = 5139.619781506285

# Verificando
df.iloc[35]
df.iloc[177]

plt.hist(x = df['Sales'])
plt.show()

plt.hist(x = df['TV_Spend'])
plt.show()

### Logaritmizar
# Deve-se logaritmizar, quando:
# - Dados estão em ordem de magnitude diferente (escala muito grande)
# - Distribuição assimétrica à direita. Exemplo: Faturamento, preços, população, PIB
# - Relações são multiplicativas e não aditivas, ou seja, o efeito de uma variável cresce proporcionalmente, não de forma linear. Exemplo: elasticidade → interpretar "um aumento percentual em X gera um aumento percentual em Y

# Técnicas
# 1) Análise de Skewness (assimetria)
#   • Entre -0.5 e +0.5 = Distribuição aproximadamente simétrica (Não precisa logaritimizar)
#   • Entre ±0.5 e ±1 = Assimetria moderada (Avaliar log, opcional)
#   • Maior que +1 ou menor que -1 = Forte assimetria (Recomenda-se logaritmizar)

# 2) Teste Estátisticos: Shapiro-Wilk, Kolmogorov-Smirnov, Anderson-Darling, Teste de normalidade conjunta.

# Não se deve Logaritmizar, quando:
# - Dados possuem valores zero ou negativos (logaritmo não existe para isso).
# - Relação entre variáveis é naturalmente linear.
# - Interpretação percentual não faz sentido para aquele contexto.

df['Sales'].skew() # Simetrica
df['TV_Spend'].skew() # Simetrica
df['Radio_Spend'].skew() # Simetrica
df['OOH_Spend'].skew() # Simetrica
df['Competitor_Price'].skew() # Simetrica

####################################
### Alteração de Inconsistências ###
####################################

df[df["Promo_Flag"] == "yes"]
df['Promo_Flag'] = df['Promo_Flag'].replace({'yes': 1})

df.head(10)

df[df["Region"] == "nort"]
df['Region'] = df['Region'].replace({'nort': "North"})

df[df["Region"] == "southh"]
df[df["Region"] == "southh"]

df[df["Region"] == "southh"]
df.count()

#########################
### Análise dos Dados ###
#########################

# Multicolinearidade
corr = df.corr(numeric_only=True)
plt.style.use('dark_background')
plt.figure(figsize=(12, 10))

sns.heatmap(
    corr,
    annot=True,
    fmt=".2f",
    cmap="seismic",
    linewidths=1.0,
    linecolor='gray',
    cbar=True,
    square=True,
    annot_kws={"color": "white"},
    mask=corr.isnull()
)

plt.show()

plt.title('Matriz de Correlação')
plt.show()

# Dispersão
grafico = px.scatter_matrix(df, dimensions=['Sales', 'TV_Spend', 'Radio_Spend', 'Digital_Spend', 'OOH_Spend', 'Competitor_Price'], color = 'Sales')
grafico.update_layout(
    width=1200,
    height=900,
    plot_bgcolor='black',
    paper_bgcolor='black',
    font_color='white')
grafico.show()

# Exportar Excel
df.to_excel("marketing_dataset_tratado.xlsx", index=False, engine='openpyxl')

# Exportar CSV
df.to_csv("marketing_dataset_tratado.csv", index=False, encoding="utf-8")

# Exportar Excel/CSV Juypter Notebook
# from google.colab import files
# df.to_excel('tratamento.xlsx', index=False)
# files.download('tratamento.xlsx')


import pandas as pd
df = pd.read_csv("https://drive.google.com/uc?export=download&id=1fKv2Lp8gonKTbgeakjy9h0eI1BOyouBU")
print(df.head())
