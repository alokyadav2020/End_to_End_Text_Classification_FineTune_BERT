from src.TextClassification.constants import *
from src.TextClassification.logging import logger
from src.TextClassification.utils.common import read_yaml,create_directories
from src.TextClassification.entity import (DataIngestionConfig,
                                           DataValidationConfig,
                                           DataTransformationConfig,
                                           ModelTrainingConfig,
                                           TrainingArgumentConfig,
                                           EvaluationConfig
                                           )


class ConfigurationManager:
    def __init__(self, config_filepath = CONFIG_FILE_PATH, param_filepath = PARAMS_FILE_PATH):
        self.config = read_yaml(config_filepath)
        self.param = read_yaml(param_filepath)

        create_directories([self.config.artifacts_root])


    def return_data_ingestion_config(self)-> DataIngestionConfig:
        config = self.config.Data_Ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(

            root_dir=config.root_dir,
            local_file_path=config.local_file_path
        )

        return data_ingestion_config
    
    def get_data_valdation_config(self)-> DataValidationConfig:
        config = self.config.Data_Validaton

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(

            root_dir=config.root_dir,
            status_file=config.status_file,
            local_fiel_validation = config.local_fiel_validation
        )

        return data_validation_config
    

    def get_data_transfomation_config(self)->DataTransformationConfig:
        config= self.config.Data_Transformation

        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(

            root_dir=config.root_dir,
            local_data_file = config.local_data_file
        )

        return data_transformation_config
    

    def get_model_training_config(self)-> ModelTrainingConfig:
        config= self.config.Model_training

        create_directories([config.root_dir])

        model_trainig_config = ModelTrainingConfig(

            root_dir=config.root_dir,
            traning_data_file=config.traning_data_file,
            model_check_point= config.model_check_point,
            model_name= config.model_name
        )

        return model_trainig_config
    

    def get_trainingargument_config(self)-> TrainingArgumentConfig:
        param = self.param.TrainingArguments


        training_arument = TrainingArgumentConfig(

            num_train_epochs = param.num_train_epochs,
            learning_rate = param.learning_rate,
            per_device_train_batch_size = param.per_device_train_batch_size,
            per_device_eval_batch_size = param.per_device_eval_batch_size,
            weight_decay = param.weight_decay,
            evaluation_strategy = param.evaluation_strategy,
            disable_tqdm = param.disable_tqdm,
            logging_steps = param.logging_steps,
            log_level = param.log_level,
            optim = param.optim
        )

        return training_arument
    

    def get_evaluation_config(self)-> EvaluationConfig:
        config= self.config.Model_Evaluation

        create_directories([config.root_dir])

        evaluation_config = EvaluationConfig(

            root_dir= config.root_dir,
            Accuracy_file= config.Accuracy_file,
            Matrix_file= config.Matrix_file
           
        )

        return evaluation_config





