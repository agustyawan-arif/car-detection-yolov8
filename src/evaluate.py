import os
import glob
import numpy as np
import matplotlib.pyplot as plt
from ultralytics import YOLO
import argparse

class YOLOEvaluate:
    def __init__(self, config_file, yolo_model):
        self.config = self.load_config(config_file)
        self.model = YOLO(yolo_model)

    def predict(self):
        results = self.model.predict(source=os.path.join(self.config['paths']['data'], "testing_images"), save=True)

    def visualize_predictions(self, testing_paths):
        predictions = glob.glob(testing_paths, '*'))
        rows, columns = 4, 4
        total_images = rows * columns
        num_images = min(total_images, len(predictions))
        random_indices = np.random.choice(len(predictions), num_images, replace=False)
        fig, axes = plt.subplots(rows, columns, figsize=(12, 12))
        for i, ax in enumerate(axes.flat):
            if i < num_images:
                idx = random_indices[i]
                image_path = predictions[idx]
                image = Image.open(image_path)
                ax.imshow(image)
                ax.axis('off')  
            else:
                ax.axis('off')
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--yolo_model", default="yolov8m.pt")
    parser.add_argument("--testing_paths", default="runs/detect/predict")
    args = parser.parse_args()
    model = args.yolo_model
    testing_paths = args.testing_paths

    evaluate = YOLOEvaluate("config.conf", model)
    evaluate.predict()
    evaluate.visualize_predictions(testing_paths)
