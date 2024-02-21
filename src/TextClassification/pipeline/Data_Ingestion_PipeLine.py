from src.TextClassification.config.configuration import ConfigurationManager
from src.TextClassification.conponents.data_ingestion import DataIngestion





class DataIngestionPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config_file= ConfigurationManager()
        data_Ingestion_config= config_file.return_data_ingestion_config()
        Data_Ingestion= DataIngestion(data_Ingestion_config)
        Data_Ingestion.Download_Data()