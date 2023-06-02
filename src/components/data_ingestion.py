import os
import sys
from src.exceptions import CustomException
from src.logger import logging
import pandas as pandas
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.component.data_transforamtion import DataTransforamtion


## initialize data ingestion configuration
'''
doesnt need constructor
dataclass is used when only a class variable needs to be created
inputs are train data patha and test data path
functionality is to collect data from various sources 
and move it to the target site either in batches or in real time
'''
@dataclass
class DataIngestionconfig:
    train_data_path:str = os.path.join('artifacts','train.csv')
    test_data_path:str = os.path.join('artifacts','test.csv')
    raw_data_path:str = os.path.join('artifacts','raw.csv')

## create a class for Data Ingestion
class DataIngestion:
    def __init__(self):
        self.ingestionconfig = DataIngestionconfig()
    def initiate_data_ingestion(self):
        logging.info('Data Ingestion methods Starts')
        try:
            df = pd.read_csv("https://raw.githubusercontent.com/krishnaik06/FSDSRegression/main/notebooks/data/gemstone.csv")
            logging.info('Raw Dataset read as pandas Dataframe')

            os.makedirs(os.path.dirname(self.ingestionconfig.raw_data_path),exist_ok=True)
            df.to_csv(self.ingestionconfig.raw_data_path,index=False)
            
            logging.info('Train test split')
            train_set,test_set = train_test_split(df,test_size=0.3)
            train_set.to_csv(self.ingestionconfig.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestionconfig.test_data_path,index=False,header=True)

            logging.info('Data Ingestion completed')

            return (self.ingestionconfig.train_data_path,self.ingestionconfig.test_data_path)
        except Exception as e:
            logging.info('Exception occurred at Data Ingestion stage')
            raise CustomException(e,sys)


## run data ingestion

if __name__=="__main__":
    obj = DataIngestion()
    train_data_path,test_data_path = obj.initiate_data_ingestion()
    data_transforamtion = DataTransforamtion()
    train_arr,test_arr,_ = data_transforamtion.initialize_data_transformation(train_data_path,test_data_path)

