import pandas as pd

# Pesos por subnível (baseado em variáveis de referência)
ponderadores = {
    "7E": 29, "7D": 27, "7C": 62, "7B": 54, "7A": 70,
    "6B": 64, "6A": 71,
    "5C": 78, "5B": 74, "5A": 62,
    "4B": 75, "4A": 89,
    "3A": 84,
    "2B": 89, "2A": 79,
    "1D": 72, "1C": 71, "1B": 74, "1A": 73
}

# Subníveis organizados por nível
levels = {
    "7": ["7E", "7D", "7C", "7B", "7A"],
    "6": ["6B", "6A"],
    "5": ["5C", "5B", "5A"],
    "4": ["4B", "4A"],
    "3": ["3A"],
    "2": ["2B", "2A"],
    "1": ["1D", "1C", "1B", "1A"]
}

# Totais reais por nível extraídos da tabela
totais_nivel = {
    "2010": {"7": 82, "6": 30, "5": 84, "4": 200, "3": 57, "2": 108, "1": 26},
    "2011": {"7": 71, "6": 100, "5": 270, "4": 241, "3": 113, "2": 136, "1": 264},
    "2016": {"7": 0, "6": 57, "5": 81, "4": 68, "3": 22, "2": 81, "1": 84}
}

# Valores já preenchidos por subnível
valores_conhecidos = {
    "2010": {
        "7C": 82, "6B": 30, "5B": 84, "4B": 200, "3A": 57, "2B": 64, "2A": 44, "1C": 6, "1B": 0, "1A": 0
    },
    "2011": {
        "7C": 71, "6B": 100, "5B": 270, "4B": 241, "3A": 113, "2B": 52, "2A": 84, "1D": 20, "1C": 45, "1B": 119, "1A": 80
    },
    "2016": {
        "6B": 57, "5B": 81, "4B": 68, "3A": 22, "2B": 50, "2A": 31, "1D": 21, "1C": 13, "1B": 44, "1A": 6
    }
}

# Inicializar DataFrame com subníveis
subniveis = list(ponderadores.keys())
anos = ["2010", "2011", "2016"]
df_resultado = pd.DataFrame(index=subniveis, columns=anos).fillna(0)

# Preencher valores conhecidos
for ano in anos:
    for sub, val in valores_conhecidos[ano].items():
        df_resultado.at[sub, ano] = val

# Preencher os ausentes com base em ponderação e totais por nível
for ano in anos:
    for nivel, subs in levels.items():
        total_nivel = totais_nivel[ano][nivel]
        pesos = {sub: ponderadores[sub] for sub in subs}
        soma_pesos = sum(pesos.values())

        valores_existentes = df_resultado.loc[subs, ano]
        soma_existentes = valores_existentes.astype(float).sum()
        restante = total_nivel - soma_existentes

        if restante > 0:
            for sub in subs:
                if df_resultado.at[sub, ano] == 0:
                    proporcao = pesos[sub] / soma_pesos
                    df_resultado.at[sub, ano] = round(restante * proporcao, 2)

# Exportar
df_resultado.reset_index(inplace=True)
df_resultado.rename(columns={"index": "Subnível"}, inplace=True)
df_resultado.to_excel("Tafonomia_Subniveis_Com_Ponderacao.xlsx", index=False)

print("Arquivo salvo: Tafonomia_Subniveis_Com_Ponderacao.xlsx")
