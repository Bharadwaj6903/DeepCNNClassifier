import os
from deepClassifier.entity import PrepareCallbacksConfig
import tensorflow as tf
import time
from pathlib import Path

class PrepareCallback:
    def __init__(self, config: PrepareCallbacksConfig):
        self.config = config

    @property
    def _create_tb_callbacks(self):
        timestamp = time.strftime("%Y-%m-%d-%H-%M-%S")
        tb_running_log_dir ="artifacts/prepare_callbacks/tensorboard_log_dir"+f"tb_logs_at_{timestamp}"
    
        return tf.keras.callbacks.TensorBoard(log_dir=Path(tb_running_log_dir))

    @property #A property can be accessed without () brackets
    def _create_ckpt_callbacks(self):
        return tf.keras.callbacks.ModelCheckpoint(
            filepath= "artifacts/prepare_callbacks/checkpoint_dir/model.h5",
            save_best_only=True   #saves only best weights
    
        )

    def get_tb_ckpt_callbacks(self):  
        return [
            self._create_tb_callbacks,  #A property can be accessed without () brackets
            self._create_ckpt_callbacks
        ]
