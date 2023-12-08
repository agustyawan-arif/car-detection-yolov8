from ultralytics import YOLO
import wandb
import os

class YOLOTrainer:
    def __init__(self, config_file):
        self.config = self.load_config(config_file)
        wandb.login(key=self.config['wandb']['key'])
        self.model = YOLO(self.config['model']['weights'])

    def train_model(self):
        self.model.train(data=os.path.join(self.config['paths']['data'], "yolo.yaml"), **self.config['train_config'])

if __name__ == "__main__":
    trainer = YOLOTrainer("config.conf")
    trainer.train_model()
