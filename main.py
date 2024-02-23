
from src.TextClassification.logging import logger
from src.TextClassification.pipeline.Data_Ingestion_PipeLine import DataIngestionPipeline
from src.TextClassification.pipeline.Data_Validation_PipeLine import DataValidationPipeline
from src.TextClassification.pipeline.Data_transformation_PipeLine import DataValidationPipeline
from src.TextClassification.pipeline.Model_training_PipeLine import ModelTrainingPieline
from src.TextClassification.pipeline.Model_evaluation_PipeLine import ModelEvaluationPieline



STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Data Validation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_validation = DataValidationPipeline()
   data_validation.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e



STAGE_NAME = "Data Transformation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_transform = DataValidationPipeline()
   data_transform.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Model Training stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   Model_Training = ModelTrainingPieline()
   Trainer,pred = Model_Training.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Model Evaluation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   Model_Training = ModelEvaluationPieline()
   Model_Training.main(Trainer,pred)
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

