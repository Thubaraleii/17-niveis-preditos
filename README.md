# Fossil Occurrence Prediction - LSL

This project includes Python and Java code to predict the presence (I) or absence (F) of key fossil types 
in the Lontras Shale Lagerstätte (LSL), based on stratigraphic and geochemical data.

## Files

- `fossil_prediction.py`: Main Python script using scikit-learn and Random Forest classifier.
- `FossilPrediction.java`: Java version using Weka's RandomForest.
- `dados_17_niveis.xlsx` or `dados_17_niveis.arff`: Input data containing fossil, stratigraphic and geochemical indicators.

## Requirements

- Python 3.x with pandas, scikit-learn
- Java 11+ with Weka library installed

## Instructions

1. Place your dataset file (`dados_17_niveis.xlsx` or `.arff`) in the working directory.
2. Run the Python script to train and evaluate models for each fossil category.
3. Alternatively, compile and run the Java version using:
   ```
   javac -cp .:weka.jar FossilPrediction.java
   java -cp .:weka.jar FossilPrediction
   ```

## Authors

Generated for academic purposes by AI with reference to the LSL fossil dataset.
# Tafonomia Subníveis - Distribuição Proporcional por Ponderadores

Este repositório contém os scripts e arquivos necessários para aplicar distribuição proporcional de fósseis por subnível,
respeitando o total por nível e um conjunto de ponderadores específicos.

## Estrutura

- `ponderamento_tafonomia.py` – Script principal que realiza o preenchimento proporcional de subníveis.
- `Nova_Coluna_Tafonomia_Completa.xlsx` – Resultado final da distribuição.
- `README.md` – Este arquivo.

## Como usar

1. Prepare um dicionário com os totais por nível (por coluna/ano).
2. Liste os valores já conhecidos por subnível.
3. O script calculará o valor proporcional restante para os subníveis ausentes com base nos ponderadores.

## Exemplo

Para o nível 7 com total de 82 fósseis:
- Apenas `7C` conhecido com 82
- Restante distribuído como zero para os outros, já que não há fósseis restantes

Níveis incompletos com totais não atingidos são preenchidos com base na proporção de pesos (ponderadores) de cada subnível.

