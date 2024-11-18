# import os
# import sys
# from xray.logger.logging import logging
# from xray.exception.exception import XrayException
# from xray.utils.common import unzip_data
# from xray.entity.config_entity import DataIngestionConfig, TrainingPipelineConfig
# from xray.entity.artifact_entity import DataIngestionArtifact


# class DataIngestion:
#     def __init__(self, data_ingestion_config: DataIngestionConfig, data_file_path: str):
#         try:
#             logging.info("Initializing DataIngestion with config and data file path")
#             self.data_ingestion_config = data_ingestion_config
#             self.data_file_path = data_file_path
#             logging.info(
#                 f"DataIngestion initialized: {self.data_ingestion_config} | {self.data_file_path}"
#             )
#         except Exception as e:
#             logging.error(f"Error initializing DataIngestion: {str(e)}")
#             raise XrayException(f"Error initializing DataIngestion: {str(e)}", sys)

#     def initiate_data_ingestion(self):
#         try:
#             logging.info(
#                 f"Creating data ingestion directory at {self.data_ingestion_config.data_ingestion_dir}"
#             )
#             os.makedirs(self.data_ingestion_config.data_ingestion_dir, exist_ok=True)

#             logging.info(
#                 f"Unzipping data from {self.data_file_path} to ingestion folder"
#             )
#             unzip_data(self.data_file_path, self.data_ingestion_config.ingested_data)
#             data_ingestion_artifact = DataIngestionArtifact(
#                 train_data_file_path="artifact/11_18_2024_14_29_17/data_ingestion/ingested\data/train"
#                 test_data_file_path="artifact/11_18_2024_14_29_17/data_ingestion/ingested\data/train"
#             )
#             logging.info("Data unzipped successfully and stored in ingestion folder")

#         except Exception as e:
#             logging.error(f"Error in initiating data ingestion: {str(e)}")
#             raise XrayException(f"Error in data ingestion: {str(e)}", sys)


import os
import sys
from xray.logger.logging import logging
from xray.exception.exception import XrayException
from xray.utils.common import unzip_data  # Assuming this handles the actual unzipping
from xray.entity.config_entity import DataIngestionConfig, TrainingPipelineConfig
from xray.entity.artifact_entity import DataIngestionArtifact


class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig, data_file_path: str):
        try:
            logging.info("Initializing DataIngestion with config and data file path")
            self.data_ingestion_config = data_ingestion_config
            self.data_file_path = data_file_path
            logging.info(
                f"DataIngestion initialized: {self.data_ingestion_config} | {self.data_file_path}"
            )
        except Exception as e:
            raise XrayException(e, sys)

    def initiate_data_ingestion(self):
        try:
            # Ensure the main directory exists
            logging.info(
                f"Creating data ingestion directory at {self.data_ingestion_config.data_ingestion_dir}"
            )
            os.makedirs(self.data_ingestion_config.data_ingestion_dir, exist_ok=True)

            # Extract the zip file into the ingestion directory
            logging.info(
                f"Unzipping data from {self.data_file_path} to the ingestion folder"
            )
            unzip_data(
                self.data_file_path, self.data_ingestion_config.data_ingestion_dir
            )

            logging.info(
                "Data unzipped successfully and stored in the ingestion folder"
            )

            # Define paths for train and test folders
            train_data_dir = os.path.join(
                self.data_ingestion_config.data_ingestion_dir, "train"
            )
            test_data_dir = os.path.join(
                self.data_ingestion_config.data_ingestion_dir, "test"
            )

            # Verify the expected structure exists
            if not os.path.isdir(train_data_dir) or not os.path.isdir(test_data_dir):
                logging.info("Extracted data does not contain the expected train/test folders")

            # Create the DataIngestionArtifact
            data_ingestion_artifact = DataIngestionArtifact(
                train_data_file_path=train_data_dir, test_data_file_path=test_data_dir
            )

            logging.info(
                f"Data ingestion artifact created successfully: {data_ingestion_artifact}"
            )
            return data_ingestion_artifact

        except Exception as e:
            raise XrayException(e, sys)
