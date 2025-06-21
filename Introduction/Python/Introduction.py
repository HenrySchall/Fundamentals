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
"bitsandbytes"]

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
from matplotlib.colors import LinearSegmentedColormap
from scipy.stats import skew 
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.tools.tools import add_constant

############################
### Análise Exploratória ###
############################

df = pd.read_csv("https://drive.google.com/uc?export=download&id=1wMapByTvMFt16zz9Bd2643eTHJXtEhnX")
df

df.describe()

df.dtypes

# Presença de Valores Nulos
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
# df['TV_Spend'] = df['TV_Spend'].fillna(df['TV_Spend'].mean())
# df['Radio_Spend'] = df['Radio_Spend'].fillna(df['Radio_Spend'].mean())
# df['Sales'] = df['Sales'].fillna(df['Sales'].mean())

# Substituindo pela Meridiana
# df['TV_Spend'] = df['TV_Spend'].fillna(df['TV_Spend'].median())
# df['Radio_Spend'] = df['Radio_Spend'].fillna(df['Radio_Spend'].median())
# df['Sales'] = df['Sales'].fillna(df['Sales'].median())

df.count()

# Tratando Outliers 