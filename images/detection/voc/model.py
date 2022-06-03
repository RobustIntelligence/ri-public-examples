"""Implements model API for RIME."""
from pathlib import Path
from typing import Dict
import torch
import sys

MODEL_FOLDER_PATH = Path(__file__).parent.absolute()
sys.path.append(str(MODEL_FOLDER_PATH))

NUM_CLASSES = 20
model = torch.hub.load(MODEL_FOLDER_PATH, 'yolov3_tiny', source="local")

def format_preds(box_info):
    """Reformat predictions to fit required format by RIME."""
    probs = [0] * NUM_CLASSES
    predicted_class_idx = int(box_info[5])
    probs[predicted_class_idx] = box_info[4].item()
    return {
        "x_min": box_info[0].item(),
        "x_max": box_info[2].item(),
        "y_min": box_info[1].item(),
        "y_max": box_info[3].item(),
        "probabilities": probs,
    }


def predict_dict(x) -> Dict:
    """Predicts on datapoint.
    
    The image to predict on is in x["__image__"].
    """
    with torch.no_grad():
        img = x["__image__"]
        result = model(img)
        preds = result.xyxyn[0]
        formatted_preds = []
        for box_idx in range(0, preds.shape[0]):
            box_info = preds[box_idx]
            formatted_pred = format_preds(box_info)
            formatted_preds.append(formatted_pred)
        return {
            "predicted_bounding_boxes": formatted_preds
        }
