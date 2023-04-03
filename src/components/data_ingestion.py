import os
import sys 
from src.logger import logging
from src.exception import CustomException
import pandas as pd 
from sklearn.model_selection import train_test_split
from dataclasses import dataclass 


@dataclass
class dataingestionconfig:
    train_dat_path:str=os.path.join("artifacts","train.csv")
    test_dat_path:str=os.path.join("artifacts","test.csv")
    raw_dat_path:str=os.path.join("artifacts","data.csv")

class dataingestion:
    def __init__(self):
        self.ingestion_config=dataingestionconfig()
    def initiate_data_ingestion(self):
        logging.info("entered the data ingestion method")
        try:
            data=pd.read_csv("notebook\std.csv")
            logging.info("read data")

            os.makedirs(os.path.dirname(self.ingestion_config.train_dat_path),exist_ok=True)
            data.to_csv(self.ingestion_config.raw_dat_path,index=False,header=True)
            logging.info("split data initated")
            train_set,test_set=train_test_split(data,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_dat_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_dat_path,index=False,header=True) 
            logging.info("ingestion of data completed")
            return(
                self.ingestion_config.train_dat_path,
                self.ingestion_config.test_dat_path
            )
        except Exception as e:
            raise CustomException(e,sys) 

if __name__=="__main__":
    obj=dataingestion()
    obj.initiate_data_ingestion()








