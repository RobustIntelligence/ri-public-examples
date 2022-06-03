from transformers import pipeline

classifier = pipeline("text-classification", model='bhadresh-savani/roberta-base-emotion', return_all_scores=True)

# Order should not be changed, corresponds to HF emotion dataset numeric labels.
# See here: https://huggingface.co/datasets/emotion.
ordered_labels = [
    "sadness",
    "joy",
    "love",
    "anger",
    "fear",
    "surprise"
]

def predict_dict(x):
    pred = classifier(x["text"])[0]
    pred_dict = {y['label']: y['score'] for y in pred}
    pred_list = [pred_dict[label] for label in ordered_labels]
    output = {"probabilities": pred_list}
    return output

