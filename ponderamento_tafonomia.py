import pandas as pd

# Ponderadores por subnível
ponderadores = {
    "7E": 29, "7D": 27, "7C": 62, "7B": 54, "7A": 70,
    "6B": 64, "6A": 71,
    "5C": 78, "5B": 74, "5A": 62,
    "4B": 75, "4A": 89,
    "3A": 84,
    "2B": 89, "2A": 79,
    "1D": 72, "1C": 71, "1B": 74, "1A": 73
}

# Organização dos subníveis por nível
levels = {
    "7": ["7E", "7D", "7C", "7B", "7A"],
    "6": ["6B", "6A"],
    "5": ["5C", "5B", "5A"],
    "4": ["4B", "4A"],
    "3": ["3A"],
    "2": ["2B", "2A"],
    "1": ["1D", "1C", "1B", "1A"]
}

# Totais por nível (ano ou coluna-alvo)
totais = {
    "7": 82,
    "6": 30,
    "5": 84,
    "4": 200,
    "3": 57,
    "2": 64,
    "1": 26
}

# Valores já conhecidos para subníveis
valores_conhecidos = {
    "5C": 30.62, "5B": 29.05, "5A": 24.34,
    "4B": 91.46, "4A": 108.54,
    "3A": 57,
    "2B": 44, "2A": 20,
    "1D": 20, "1C": 6, "1B": 0, "1A": 0
}

# Inicializa DataFrame
subniveis = list(ponderadores.keys())
df = pd.DataFrame(index=subniveis, columns=["NovaColuna"]).fillna(0)

# Preencher valores existentes
for sub, val in valores_conhecidos.items():
    df.at[sub, "NovaColuna"] = val

# Preencher proporcionalmente os ausentes
for nivel, subs in levels.items():
    total = totais[nivel]
    existentes = df.loc[subs, "NovaColuna"].astype(float)
    soma_existente = existentes.sum()
    restante = total - soma_existente

    if restante > 0:
        pesos = {s: ponderadores[s] for s in subs}
        soma_pesos = sum(pesos.values())
        for sub in subs:
            if df.at[sub, "NovaColuna"] == 0:
                proporcao = pesos[sub] / soma_pesos
                df.at[sub, "NovaColuna"] = round(restante * proporcao, 2)

# Exporta resultado
df.reset_index(inplace=True)
df.rename(columns={"index": "Subnível"}, inplace=True)
df.to_excel("Nova_Coluna_Tafonomia_Completa.xlsx", index=False)
print("Distribuição completa salva em: Nova_Coluna_Tafonomia_Completa.xlsx")
