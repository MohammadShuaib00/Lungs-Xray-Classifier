import os
import sys
from datetime import datetime
from xray.constant import training_pipeline
from xray.logger.logging import logging
from xray.exception.exception import XrayException

print(f"Artifact dir pipeline: {training_pipeline.ARTIFACT_DIR}")


class TrainingPipelineConfig:
    def __init__(self, timestamp=datetime.now()):
        try:
            logging.info("Initializing TrainingPipelineConfig")
            timestamp = timestamp.strftime("%m_%d_%Y_%H_%M_%S")
            self.artifact_name = training_pipeline.ARTIFACT_DIR
            self.artifact_dir = os.path.join(self.artifact_name, timestamp)
            logging.info(
                f"TrainingPipelineConfig initialized with artifact dir: {self.artifact_dir}"
            )
        except Exception as e:
            logging.error(f"Error initializing TrainingPipelineConfig: {str(e)}")
            raise XrayException(
                f"Error initializing TrainingPipelineConfig: {str(e)}", sys
            )


class DataIngestionConfig:
    def __init__(self, training_pipeline_config: TrainingPipelineConfig):
        try:
            logging.info("Initializing DataIngestionConfig")
            self.training_pipeline_config = training_pipeline_config
            self.data_ingestion_dir = os.path.join(
                self.training_pipeline_config.artifact_dir,
                training_pipeline.DATA_INGESTION_DIR,
            )
            self.ingested_data = os.path.join(
                self.data_ingestion_dir, training_pipeline.DATA_INGESTED_fOLDER
            )
            self.source_url = training_pipeline.UNZIP_DATA_FILE_PATH
            logging.info(
                f"DataIngestionConfig initialized with directory: {self.data_ingestion_dir}"
            )
        except Exception as e:
            logging.error(f"Error initializing DataIngestionConfig: {str(e)}")
            raise XrayException(
                f"Error initializing DataIngestionConfig: {str(e)}", sys
            )
