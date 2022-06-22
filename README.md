# Robust Intelligence Public Examples

This repository tracks sample datasets and models. Due to size constraints, the actual data and model files are stored externally.

This repository can be installed as a pip package (e.g. `pip install -e git+https://github.com/RobustIntelligence/ri-public-examples.git`). 
To pull the data and model(s) for a specific example, run the following module script as follows from within the top-level directory:
```python
from ri_public_examples.download_files import download_files
download_files('tabular/nyc_tlc', 'nyc_tlc')
```
This will download the NYC TLC datasets/models/configs.

## Tabular

### 1. Income (`tabular/income/`)
Based on the [Adult Census Income](https://www.kaggle.com/datasets/uciml/adult-census-income) dataset, this directory contains a basic Catboost binary classification model, reference set, and evaluation set.

### 2. Fraud (`tabular/fraud/`)
This is a proprietary fraud detection dataset created by Robust Intelligence. This directory contains a basic Catboost binary classification model, reference set, and evaluation set.

### 3. NYC TLC (`tabular/nyc_tlc/`)
This is based on public NYC Taxi and Limousine Commission data (https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page). This directory contains a basic Catboost regression model, reference set, evaluation set and test set (representing production data).

## Natural Language Processing

### Classification

#### 1. ArXiv (`nlp/classification/arxiv/`)
This is based on the [public ArXiv dataset](https://www.kaggle.com/datasets/Cornell-University/arxiv?select=arxiv-metadata-oai-snapshot.json).
This directory contains an NLP topic classification model, reference set, evaluation set, and test sets representing production data.

#### 2. Twitter Sentiment Analysis (`nlp/classification/sentiment_analysis/`)
This is based on the [CARER Emotion Recognition dataset](https://github.com/dair-ai/emotion_dataset).
This directory contains a RoBERTA-based model trained on tweets and used for sentiment analysis. It also contains the reference set and test sets.

## Computer Vision

### Classification

#### 1. Animals with Attributes 2 (`images/classification/awa2`)
This is based on the [Animals with Attributes dataset](https://cvml.ist.ac.at/AwA2/).
This directory contains an image classification model, a reference and evaluation set for stress testing, as well as a test set representing production data.
