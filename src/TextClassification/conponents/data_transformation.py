import os
import pandas as pd 
from sklearn.model_selection import train_test_split
from datasets import DatasetDict,Dataset
from src.TextClassification.entity import DataTransformationConfig
from src.TextClassification.logging import logger
from pathlib import Path


class Datatransformation:
    def __init__(self, config: DataTransformationConfig) -> None:
        self.config = config


    def Data_Preprocessing(self, data_file: Path)-> pd.DataFrame:
        
        if os.path.exists(data_file):
            df = pd.read_csv(data_file)
            df['text']=df.text.str.replace('\n',' ')
            df['text']=df.text.str.replace('[','')
            df['text']=df.text.str.replace(']','')
            df=df.rename(columns={"generated":"label"})
            print(df.head())

            logger.info(f"Data loaded in DataFrame from {self.config.local_data_file}")

            return df
    

    def get_preprocessed_splited_data(self,df: pd.DataFrame):

        df_train, df_test = train_test_split(df, test_size=0.30, shuffle=True)
        df_val, df_test = train_test_split(df_test, test_size=0.50,shuffle=True)

        logger.info("Data splited in Train, Test, and Validation dataset")

        return df_train,df_test,df_val
    
    def data_save_to_local(self,df_train: pd.DataFrame, df_test: pd.DataFrame, df_val:pd.DataFrame):

        train_dataset = Dataset.from_pandas(df_train,preserve_index=False)
        test_dataset = Dataset.from_pandas(df_test,preserve_index=False)
        validation_dataset = Dataset.from_pandas(df_val,preserve_index=False)

        dataset_dict = DatasetDict({
            "train": train_dataset,
            "test": test_dataset,
            "validation": validation_dataset
        })

        dataset_dict.save_to_disk(self.config.root_dir)

        logger.info(f"Data saved in form of DataDictionary to disc {self.config.root_dir}")

        # Print information about the dataset
        print(dataset_dict)

        # return dataset_dict
    

    def Data_trasnformation(self):

        dataframe = self.Data_Preprocessing(self.config.local_data_file)
        print(dataframe.head())

        train,test,valdn =self.get_preprocessed_splited_data(dataframe)

        self.data_save_to_local(train,test,valdn)





    



