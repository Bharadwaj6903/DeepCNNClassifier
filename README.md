## deep Classifier project

## workflow

1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config.
6. Update the components
7. Update the pipeline
8. Test run pipeline stage
9. run tox for testing your package
10. Update the dvc.yaml
11. run "dvc repro" for running all the stages in pipeline(dvc reproduction)

![img](https://raw.githubusercontent.com/c17hawke/FSDS_NOV_deepCNNClassifier/main/docs/images/Data%20Ingestion%402x%20(1).png)


mlflow server \
--backend-store-uri sqlite.///mlflow.db \
--default-artifact-root ./artifacts \
--host 0.0.0.0 -p 1234
backward slashes are used to make it a multi-line command
go to http://localhost:1234/


STEP 1: Set the env variable | Get it from dagshub -> remote tab -> mlflow tab

MLFLOW_TRACKING_URI=https://dagshub.com/Bharadwaj6903/DeepCNNClassifier.mlflow \
MLFLOW_TRACKING_USERNAME=Bharadwaj6903 \
MLFLOW_TRACKING_PASSWORD=cfe466dca2f6a4d1341cea293eaeb4c8be817904 \


export is used to set them as environment variables
write the below 3 commands in terminal
export MLFLOW_TRACKING_URI=https://dagshub.com/Bharadwaj6903/DeepCNNClassifier.mlflow 
export MLFLOW_TRACKING_USERNAME=Bharadwaj6903 
export MLFLOW_TRACKING_PASSWORD=cfe466dca2f6a4d1341cea293eaeb4c8be817904 

STEP 2: install mlflow

STEP 3: Set remote URI

STEP 4: Use context manager of mlflow to start run and then log metrics, params and model




