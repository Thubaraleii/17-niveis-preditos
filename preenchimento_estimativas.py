
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Subníveis
subniveis = [
    "1A", "1B", "1C", "1D", "2A", "2B", "3A", "4A", "4B", "5A", "5B", "5C",
    "6A", "6B", "7A", "7B", "7C", "7D", "7E"
]

# Dados com valores reais e ausentes (np.nan)
dados = {
    "OPAL": [np.nan, np.nan, 2, 1, 0, 1, 0, 1, 2, 4, 3, 4, 2, 1, 3, 7, 3, 10, 4],
    "MOA": [np.nan, np.nan, 71, 72, 79, 89, 84, 89, 75, 62, 74, 78, 71, 64, 70, 54, 62, 27, 29],
    "TOC": [12.97, 12.41, 7.42, 5.73, 7.69, 8.79, 13.05, 12.01, np.nan, 11.7, 12.11, 11.93, 11.93, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
    "TN": [0.54, 0.52, 0.26, 0.18, 0.29, 0.32, 0.54, 0.43, np.nan, 0.44, 0.46, 0.43, 0.43, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
    "Fe2O3": [4.94, 5.52, 5.25, 5.78, 6.89, 5.99, 7.41, 5.23, np.nan, 6.41, 6.66, 7.06, 7.06, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
    "U/Th": [1.48, 1.51, 1.17, 1.11, 1.28, 1.35, 1.66, 1.81, np.nan, 1.82, 1.98, 2.06, 2.06, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]
}

df = pd.DataFrame(dados, index=subniveis)

# Função para preencher valores ausentes usando regressão linear com índice
def preencher_com_regressao(col):
    y = df[col].values
    x = np.arange(len(y)).reshape(-1, 1)
    mask = ~np.isnan(y)
    model = LinearRegression().fit(x[mask], y[mask])
    y_pred = model.predict(x)
    preenchido = y.copy()
    for i in range(len(y)):
        if np.isnan(preenchido[i]):
            preenchido[i] = round(y_pred[i], 2)
    return preenchido, y != preenchido

# Preencher e marcar os novos valores
novos_valores = {}
destaques = {}
for col in df.columns:
    preenchido, destaque = preencher_com_regressao(col)
    novos_valores[col] = preenchido
    destaques[col] = destaque

df_preenchido = pd.DataFrame(novos_valores, index=subniveis)
df_destaque = pd.DataFrame(destaques, index=subniveis)

# Marcar os valores novos com "*"
df_formatado = df_preenchido.astype(str)
for col in df.columns:
    df_formatado[col] = df_formatado[col].where(~df_destaque[col], df_formatado[col] + " *")

# Salvar como Excel
df_formatado.to_excel("planilha_completa_estimativas.xlsx", sheet_name="Estimativas", index_label="Subnível")
