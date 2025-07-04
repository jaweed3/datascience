import pandas as pd
import os
from src.datascience import logger
from sklearn.linear_model import ElasticNet
from src.datascience.entity.config_entity import ModelTrainerConfig
import mlflow
from urllib.parse import urlparse
import joblib

os.environ["MLFLOW_TRACKING_URI"] = "https://dagshub.com/jaweed3/datascience.mlflow"
os.environ["MLFLOW_TRACKING_USERNAME"] = "jaweed3"
os.environ["MLFLOW_TRACKING_PASSWORD"] = "0933f50842e73c4bd68fffd52850326b068782d5"

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config
    
    def train(self):
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)

        train_x = train_data.drop([self.config.target_column], axis=1)
        test_x = test_data.drop([self.config.target_column], axis=1)
        train_y = train_data[[self.config.target_column]]
        test_y = test_data[[self.config.target_column]]

        lr = ElasticNet(alpha=self.config.alpha, l1_ratio=self.config.l1_ratio, random_state=42)
        lr.fit(train_x, train_y)

        joblib.dump(lr, os.path.join(self.config.root_dir, self.config.model_name))