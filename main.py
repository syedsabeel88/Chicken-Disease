from cnnClassifier import logger
from cnnClassifier.pipeline.Stage_01_Data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.Stage_02_Prepare_base_model import PrepareBaseModelTrainingPipeline
from cnnClassifier.pipeline.Stage_03_Training import TrainingPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>Stage :{STAGE_NAME} started<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>Stage :{STAGE_NAME} completed<<<<\n\nx")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Prepare Base Model"

try:
    logger.info(f">>>>Stage :{STAGE_NAME} started<<<<")
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>Stage :{STAGE_NAME} completed<<<<\n\nx")
except Exception as e:
    logger.exception(e)
    raise e
        

STAGE_NAME = "Training"

try:
    logger.info(f">>>>Stage :{STAGE_NAME} started<<<<")
    obj = TrainingPipeline()
    obj.main()
    logger.info(f">>>>Stage :{STAGE_NAME} completed<<<<\n\nx")        
except Exception as e:
    logger.exception(e)
    raise e