from src.TextClassification.entity import EvaluationConfig
import pandas as pd
import os
from sklearn.metrics import accuracy_score




class ModelEvaluation:
    def __init__(self, config: EvaluationConfig,Trainer,Pred) -> None:
        self.config = config
        self.Trainer = Trainer
        self.pred = Pred




    def EvaluatingModel(self):
        

        Metrix = [self.Trainer.evaluate()]
        df = pd.DataFrame(Metrix)
        df.to_csv(os.path.join(self.config.root_dir,self.config.Matrix_file))

        Score = accuracy_score(self.pred.label_ids, self.pred.predictions.argmax(axis=-1))
        df1 = pd.DataFrame([{"Score" : Score}])
        df1.to_csv(os.path.join(self.config.root_dir,self.config.Accuracy_file))




        print()
        print(f"Evaluation of model training {df.head()}")
        print()
        print("--------------------------")
        print()
        print(f"Evaluation of model training {df1.head()}")
        print()



