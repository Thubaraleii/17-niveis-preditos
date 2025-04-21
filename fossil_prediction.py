# Fossil Prediction Model - Python
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Carregar os dados
df = pd.read_excel("dados_17_niveis.xlsx")

# Selecionar as colunas úteis
features = ["DISTÂNCIA", "ESPESSURA", "MOA", "TOC", "TS", "Fe2O3", "U/Th", "Al2O3", "TiO2"]
fossil_targets = ["PEIXES_I", "PEIXES_F", "BRAQUIOPODES_I", "BRAQUIOPODES_F", "ESPONJAS_I", "ESPONJAS_F"]

# Gerar modelos para cada tipo de fóssil
for target in fossil_targets:
    data = df.dropna(subset=[target])
    X = data[features]
    y = data[target]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    print(f"Resultados para {target}:")
    print(classification_report(y_test, model.predict(X_test)))
