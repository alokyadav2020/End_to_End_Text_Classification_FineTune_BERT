from src.TextClassification.config.configuration import ConfigurationManager
from src.TextClassification.conponents.model_training import ModelTraining





class ModelTrainingPieline:
    def __init__(self) -> None:
        pass

    def main(self):
        config_file= ConfigurationManager()
        model_config= config_file.get_model_training_config()
        Arg_config = config_file.get_trainingargument_config()

        Training= ModelTraining(model_config, Arg_config)
        Trainer = Training.Training_Model()
        return Trainer