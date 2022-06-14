# Robust Intelligence Public Examples

This repository tracks sample datasets and models. Due to size constraints, the actual data and model files are stored externally.

To pull the data and model(s) for a specific example, run the `download_files.py` script like so:
```bash
python download_files.py --project-dir tabular/nyc_tlc # downloads the NYC TLC example
```

## Tabular

### 1. Income (`tabular/income/`)
Based on the [Adult Census Income](https://www.kaggle.com/datasets/uciml/adult-census-income) dataset, this directory contains a basic Catboost binary classification model, reference set, and evaluation set.

### 2. Fraud (`tabular/fraud/`)
This is a proprietary fraud detection dataset created by Robust Intelligence. This directory contains a basic Catboost binary classification model, reference set, and evaluation set.

### 3. NYC TLC (`tabular/nyc_tlc/`)
This is based on public NYC Taxi and Limousine Commission data (https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page). This directory contains a basic Catboost regression model, reference set, evaluation set and test set (representing production data).

## Natural Language Processing

### Classification

#### 1. Arxiv (`nlp/classification/arxiv/`)
TODO

#### 2. Twitter Sentiment Analysis (`nlp/classification/sentiment_analysis/`)
TODO
