from dataclasses import dataclass
import os
import sys


@dataclass
class DataIngestionArtifact:
    train_data_file_path: str
    test_data_file_path: str
