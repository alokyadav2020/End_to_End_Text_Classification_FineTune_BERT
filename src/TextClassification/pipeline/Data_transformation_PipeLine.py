from src.TextClassification.config.configuration import ConfigurationManager
from src.TextClassification.conponents.data_transformation import Datatransformation





class DataValidationPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config_file= ConfigurationManager()
        data_transform_config= config_file.get_data_transfomation_config()
        Data_Transform= Datatransformation(data_transform_config)
        Data_Transform.Data_trasnformation()