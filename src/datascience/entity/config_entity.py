from dataclasses import dataclass
from pathlib import Path
from src.datascience.constant import *
from src.datascience.utils.common import read_yaml, create_directories

# Update the params.yaml
@dataclass
class DataIngestionConfig:
    root_dir: Path
    source_dir: str
    local_data_file: Path
    unzip_dir: Path

@dataclass
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    unzip_data_dir: Path
    all_schema: dict