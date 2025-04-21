/*
Fossil Prediction Model - Java (Weka)
Requer as bibliotecas do Weka para funcionar.
*/

import weka.core.Instances;
import weka.core.converters.ConverterUtils.DataSource;
import weka.classifiers.trees.RandomForest;
import weka.classifiers.Evaluation;
import java.util.Random;

public class FossilPrediction {
    public static void main(String[] args) throws Exception {
        DataSource source = new DataSource("dados_17_niveis.arff");
        Instances data = source.getDataSet();
        data.setClassIndex(data.numAttributes() - 1); // Assumindo o target como última coluna

        RandomForest rf = new RandomForest();
        rf.buildClassifier(data);

        Evaluation eval = new Evaluation(data);
        eval.crossValidateModel(rf, data, 10, new Random(1));

        System.out.println(eval.toSummaryString());
    }
}
