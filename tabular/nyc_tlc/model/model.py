"""Model."""
import pickle
from pathlib import Path

import numpy as np
import pandas as pd
from catboost import CatBoostClassifier, CatBoostRegressor

model_dir = Path(__file__).parent / "model_extras"
if model_dir.exists():
    cat_features = pickle.load(open(model_dir / "cat_features.pkl", "rb"))
    cont_features = pickle.load(open(model_dir / "cont_features.pkl", "rb"))
    model = CatBoostRegressor()
    model.load_model(str(model_dir / "model.catb"))
else:
    raise ValueError("Model files do not exist in required format.")


def preprocess_df(df: pd.DataFrame) -> pd.DataFrame:
    """Apply string preprocessing to categorical features."""
    cat_df = df[cat_features].astype(str)
    cont_df = df[cont_features]
    return pd.concat([cat_df, cont_df], axis=1)


def predict_df(df: pd.DataFrame) -> np.ndarray:
    """Predict."""
    df = preprocess_df(df)
    return model.predict(df)
