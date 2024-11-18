from xray.logger.logging import logging
from xray.exception.exception import XrayException
from xray.components.data_ingestion import DataIngestion
from xray.entity.config_entity import DataIngestionConfig, TrainingPipelineConfig
from xray.constant import training_pipeline
import os
import sys


class TrainingPipeline:
    def __init__(self):
        try:
            logging.info("Initializing TrainingPipeline")
            self.training_pipeline_config = TrainingPipelineConfig()
            logging.info("TrainingPipelineConfig initialized successfully")
        except Exception as e:
            logging.error(f"Error initializing TrainingPipelineConfig: {str(e)}")
            raise XrayException(
                f"Error initializing TrainingPipelineConfig: {str(e)}", sys
            )

    def started_data_ingestion(self):
        try:
            logging.info("Starting data ingestion process")
            data_file_path = training_pipeline.UNZIP_DATA_FILE_PATH
            data_ingestion_config = DataIngestionConfig(self.training_pipeline_config)
            data_ingestion = DataIngestion(data_ingestion_config, data_file_path)
            logging.info("DataIngestion instance created, initiating data ingestion")
            data_ingestion.initiate_data_ingestion()  # Ensure data ingestion is initiated
            logging.info("Data ingestion process completed successfully")
        except Exception as e:
            logging.error(f"Error in data ingestion: {str(e)}")
            raise XrayException(f"Error in data ingestion: {str(e)}", sys)

    def run_pipeline(self):
        try:
            logging.info("Starting the training pipeline")
            self.started_data_ingestion()  # Call the data ingestion method on the current instance
            logging.info("Training pipeline completed successfully")
        except Exception as e:
            logging.error(f"Error running the pipeline: {str(e)}")
            raise XrayException(f"Error running pipeline: {str(e)}", sys)
