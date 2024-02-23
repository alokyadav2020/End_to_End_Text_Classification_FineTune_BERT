from src.TextClassification.config.configuration import ConfigurationManager
from src.TextClassification.conponents.model_evaluation import ModelEvaluation





class ModelEvaluationPieline:
    def __init__(self) -> None:
        pass

    def main(self,Trainer,pred):
        config_file= ConfigurationManager()
        Eval_config= config_file.get_evaluation_config()
       

        Model_Matrix= ModelEvaluation(Eval_config, Trainer,pred)
        Model_Matrix.EvaluatingModel()