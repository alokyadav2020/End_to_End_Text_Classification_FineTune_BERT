import os
import pandas as pd
from src.TextClassification.config.configuration import ModelTrainingConfig, TrainingArgumentConfig
from transformers import AutoTokenizer
import torch
from transformers import AutoModelForSequenceClassification,TrainingArguments,Trainer,EvalPrediction
import evaluate
import numpy as np
from datasets import load_from_disk, DatasetDict
from sklearn.metrics import accuracy_score

class ModelTraining:
    def __init__(self, config: ModelTrainingConfig, param: TrainingArgumentConfig) -> None:
        self.config = config
        self.param = param
        self.tokenizer = AutoTokenizer.from_pretrained(self.config.model_check_point)

        


    def tokenize_function(self,batch):  
        # tokenizer = AutoTokenizer.from_pretrained(self.config.model_check_point)
        return self.tokenizer(batch["text"], padding=True, truncation=True)
    
    
    def load_model(self):
    #   device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        num_labels = 2
        model = (AutoModelForSequenceClassification.from_pretrained(self.config.model_check_point, num_labels=num_labels))

        return model


    def training_arguments(self):

        training_arg = TrainingArguments(

            output_dir= self.config.model_name,
            num_train_epochs= self.param.num_train_epochs,
            learning_rate= self.param.learning_rate,
            per_device_train_batch_size= self.param.per_device_train_batch_size,
            per_device_eval_batch_size= self.param.per_device_eval_batch_size,
            weight_decay= self.param.weight_decay,
            evaluation_strategy= self.param.evaluation_strategy,
            disable_tqdm= self.param.disable_tqdm,
            logging_steps= self.param.logging_steps,
            log_level= self.param.log_level,
            optim= self.param.optim
        )

        return training_arg
    
    

    # def compute_metrics(elv):
        
    #     x, y = elv
    #     preds = np.argmax(x, -1)
    #     metric = evaluate.load("accuracy")
    #     return metric.compute(predictions=preds, references=y)
    

    def compute_metrics(eval_pred):
        predictions, labels = eval_pred
        predictions = np.argmax(predictions, axis=1)
        accuracy = evaluate.load("accuracy")
        return accuracy.compute(predictions=predictions, references=labels)
        

    def Training_Model(self):

        torch.cuda.empty_cache()

        dataset_dict = load_from_disk(self.config.traning_data_file)
        tiny_data = DatasetDict()
        tiny_data['train'] = dataset_dict['train'].shuffle(seed=1).select(range(20))
        tiny_data['validation'] = dataset_dict['validation'].shuffle(seed=1).select(range(10))
        tiny_data['test'] = dataset_dict['test'].shuffle(seed=1).select(range(10))


        print(tiny_data)

        data_encoded = tiny_data.map(self.tokenize_function, batched=True, batch_size=None)


        model = self.load_model()

        training_arg = self.training_arguments()


        trainer = Trainer(

            model= model,
            args= training_arg,
            # compute_metrics=  self.compute_metrics,
            train_dataset= data_encoded['train'],
            eval_dataset= data_encoded["validation"],
            tokenizer= self.tokenizer
        )

        trainer.train()
       
        trainer.save_model(self.config.model_name)

        pred= trainer.predict(data_encoded['test'])

        
        


        return trainer,pred

        # Evaluate = trainer.evaluate()

       

        # pred= trainer.predict(data_encoded['test'])

        # pred
        

        # Score = accuracy_score(pred.label_ids, pred.predictions.argmax(axis=-1))
        # print(f"Scor is : {Score}")

        # df = pd.DataFrame([{"Score" : Score}])
        # df.to_csv(self.config.root_dir)


