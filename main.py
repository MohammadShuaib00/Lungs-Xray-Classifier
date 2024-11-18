from xray.logger.logging import logging
from xray.pipeline.training_pipeline import TrainingPipeline

if __name__ == "__main__":
    try:
        logging.info("Starting the training pipeline execution")

        # Instantiate the TrainingPipeline class
        pipeline = TrainingPipeline()

        # Call run_pipeline to execute the data ingestion and other pipeline steps
        pipeline.run_pipeline()

        logging.info("Training pipeline execution finished")
    except Exception as e:
        logging.error(f"Error in main execution: {str(e)}")
        raise
