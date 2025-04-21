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
