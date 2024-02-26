# Human Text Vs AI-Generated Text


### The project is all about how to classify text between human-generated text and AI-generated text.

### End-to-end Text Classification project, which is fine-tuned with the BERT-based (distilbert/distilbert-base-uncased) model with the dataset of human text and AI-generated text.



Model - distilbert/distilbert-base-uncased
Dataset -AI Vs Human Text from Kaggle, https://www.kaggle.com/datasets/shanegerami/ai-vs-human-text
Mongo Db
Flask
Deployed on AWS EC2 server

## Workflows

1. Update config.yaml
2. Update params.yaml
3. Update entity
4. Update the configuration manager in src config
5. update the conponents
6. update the pipeline
7. update the main.py
8. update the app.py

### The stages of the project are Data Ingestion, Data Validation, Data Transformation, Data Training, and Model evaluation.

1. Data Ingestion - Data can be downloaded from a server or database like MySQL or MongoDB. Here data is downloaded from Mongo.
2. Data Validation - To check data are available for further processing and training.
3. Data Transformation - Involves various tools and technology to process row data and make it suitable for training.
4. Model training - The tokenizer and model ( ‘distilbert/distilbert-base-uncased’) is used for model training.
5. Model Evaluation - After training model is evaluated by accuracy score from sklearn metrics.


After evaluation of model it deployed on AWS EC2 instance ubuntu server, Method of deployment is CI/CD deployment using github action and docker.

STEPS FOR DELPOYMENT -

1. Login to AWS console
2. Create IAM user for deployment
3. Create ECR repo to store/save docker image
4. Create EC2 machine (Ubuntu)
5. Open EC2 and Install docker in EC2 Machine:
6. Configure EC2 as self-hosted runner:
7. Setup github secrets:



