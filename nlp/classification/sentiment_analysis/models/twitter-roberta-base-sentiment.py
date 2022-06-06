"""Wrapped model for the RoBERTa-based twitter sentiment analysis model."""
from typing import Dict, List

import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer

_hf_tag = "cardiffnlp/twitter-roberta-base-sentiment"
_tokenizer = AutoTokenizer.from_pretrained(_hf_tag)
_model = AutoModelForSequenceClassification.from_pretrained(_hf_tag)


def predict_dict(x: dict) -> Dict[str, list]:
    with torch.no_grad():
        input_ids = _tokenizer(x["text"], max_length=512, truncation=True)["input_ids"]
        tensor = torch.tensor([input_ids], dtype=torch.int32)
        preds = _model(tensor)
        logits = preds.logits[0]
        probs: List[float] = torch.softmax(logits, dim=-1).tolist()
    return {"probabilities": probs}
