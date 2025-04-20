import subprocess
import sys

# Lista de pacotes que você quer instalar
pacotes = ["numpy", "pandas", 'matplotlib', "scipy.stats","seaborn","statsmodels","plotly"] 

for pacote in pacotes:
    subprocess.check_call([sys.executable, "-m", "pip", "install", pacote])