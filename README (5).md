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

