from src.TextClassification.config.configuration import ConfigurationManager
from transformers import AutoTokenizer
from transformers import pipeline


class PredictionPipeline:
    def __init__(self):
        self.config = ConfigurationManager().get_prediction_config()


    
    def predict(self,text):
        # tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_name)
        

        pipe = pipeline("text-classification", model=self.config.model_name)

        print("Text :")
        print(text)

        output = pipe(text)[0]["label"]
        output_score = pipe(text)[0]["score"]
        print("\nModel label:")
        print(output)
        print("\nModel Score:")
        print(output_score)

        return output,output_score