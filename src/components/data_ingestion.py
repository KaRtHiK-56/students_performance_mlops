import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass  # this is used to define the class variable

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig

from src.components.model_trainer import ModelTrainerConfig
from src.components.model_trainer import ModelTrainer


@dataclass  # since we are using dataclass decorator, we are not defining the __init__ constructor here
class DataIngestionConfig:  # all inputs that are required are imported/loaded here
    train_data_path: str = os.path.join(
        "artifacts", "train.csv"
    )  # all the outputs are saved in artifacts path
    test_data_path: str = os.path.join("artifacts", "test.csv")
    raw_data_path: str = os.path.join("artifacts", "data.csv")


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        """_summary_

        Raises:
            CustomException: _description_

        Returns:
            _type_: _description_
        """
        logging.info("Entered the data ingestion method or component")
        try:
            df = pd.read_csv(
                r"C:\Users\User\Desktop\mlops\students_performance_mlops\notebook\data\stud.csv"
            )
            logging.info("Read the dataset as dataframe")

            os.makedirs(
                os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True
            )  # this  will create the artifact directory if it does not exist

            df.to_csv(
                self.ingestion_config.raw_data_path, index=False, header=True
            )  # converting the df and saving as .csv file

            logging.info("Train test split initiated")
            train_set, test_set = train_test_split(df, test_size=0.25, random_state=42)

            train_set.to_csv(
                self.ingestion_config.train_data_path, index=False, header=True
            )  # converting the df and saving as .csv file

            test_set.to_csv(
                self.ingestion_config.test_data_path, index=False, header=True
            )  # converting the df and saving as .csv file

            logging.info("Ingestion of the data is completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
            )
        except Exception as e:
            raise CustomException(e, sys)


if __name__ == "__main__":
    obj = DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()

    data_transformation = DataTransformation()
    train_arr, test_arr, _ = data_transformation.initiate_data_transformation(
        train_data, test_data
    )

    modeltrainer = ModelTrainer()
    print(modeltrainer.initiate_model_trainer(train_arr, test_arr))
