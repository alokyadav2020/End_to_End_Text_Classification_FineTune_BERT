import os
from pathlib import Path
from src.TextClassification.logging import logger
from src.TextClassification.entity import DataValidationConfig
from src.TextClassification.utils.common import WriteFile





class DataValidation:
    def __init__(self, Vconfig: DataValidationConfig) -> None:
        self.Validation_config = Vconfig


    def Validation_Data(self):


        if os.path.exists(self.Validation_config.local_fiel_validation):
            WriteFile(self.Validation_config.status_file,"True")
                
            logger.info(f"Data file is available for data processing in {self.Validation_config.local_fiel_validation}")

        else:
            WriteFile(self.Validation_config.status_file,"False")    
            logger.info(f"Data file is not available for data processing in {self.Validation_config.local_fiel_validation}")