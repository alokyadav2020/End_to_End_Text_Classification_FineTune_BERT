from dataclasses import dataclass
from pathlib import Path



@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    local_file_path: Path


@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    status_file: Path   
    local_fiel_validation: Path 

@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path    
    local_data_file: Path

@dataclass(frozen=True)
class ModelTrainingConfig:
    root_dir: str
    traning_data_file: Path   
    model_check_point: str 
    model_name: str
    tokenizer_name: str

@dataclass(frozen=True)
class TrainingArgumentConfig:
    num_train_epochs: float
    learning_rate: float
    per_device_train_batch_size: int
    per_device_eval_batch_size: int
    weight_decay: float
    evaluation_strategy: str
    disable_tqdm: bool
    logging_steps: float
    log_level: str
    optim: str

@dataclass(frozen=True)
class EvaluationConfig:
    root_dir: Path
    Accuracy_file: Path
    Matrix_file: Path

@dataclass(frozen=True)
class ModelPredictionConfig:
    model_name: Path
    tokenizer_name: Path
