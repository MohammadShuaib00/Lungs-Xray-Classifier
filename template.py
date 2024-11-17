from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format="[%(asctime)s]: %(message)s")

project_name = "xray"

list_of_files = [
    ".github/workflows/.gitkeep",
    "lungsdata",
    "xray/__init__.py",
    "xray/cloud_storage/__init__.py",
    "xray/cloud_storage/s3_operations.py",
    "xray/components/__init__.py",
    "xray/components/data_ingestion.py",
    "xray/components/data_transformation.py",
    "xray/components/data_validation.py",
    "xray/components/model_trainer.py",
    "xray/components/model_evaluation.py",
    "xray/components/model_pusher.py",
    "xray/constant/__init__.py",
    "xray/constant/training_pipeline/__init__.py",
    "xray/logger/__init__.py",
    "xray/logger/logging.py",
    "xray/exception/__init__.py",
    "xray/exception/exception.py",
    "xray/pipeline/__init__.py",
    "xray/pipeline/training_pipeline.py",
    "xray/pipeline/prediction_pipeline.py",
    "xray/ml/__init__.py",
    "xray/ml/model/__init__.py",
    "xray/ml/model/estimator.py",
    "xray/ml/metric/__init__.py",
    "xray/ml/metric/get_metric_score.py",
    "xray/entity/__init__.py",
    "xray/entity/config_entity.py",
    "xray/entity/artifact_entity.py",
    "setup.py",
    "notebook/experiment.ipynb",
    "requirements.txt",
    "Dockerfile",
    "bentofile.yaml",
    "main.py",
]

for file_path in list_of_files:
    file = Path(file_path)
    if file.suffix:
        file.parent.mkdir(parents=True, exist_ok=True)
        file.touch(exist_ok=True)
        logging.info(f"Created file: {file}")
    else:
        file.mkdir(parents=True, exist_ok=True)
        logging.info(f"Created directory: {file}")
