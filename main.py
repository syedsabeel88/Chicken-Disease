from cnnClassifier import logger
from cnnClassifier.pipeline.Stage_01_Data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>Stage :{STAGE_NAME} started<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>Stage :{STAGE_NAME} completed<<<<\n\nx")
except Exception as e:
    logger.exception(e)
    raise e



