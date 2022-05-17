from catboost import CatBoostClassifier
from pathlib import Path
mod = CatBoostClassifier()
mod.load_model(Path(__file__).parent/ "fraud_model.catb")
cat_cols = ['category', 'card_type', 'card_company', 'city', 'browser_version', 'country']

def predict_df(df):
    for col in cat_cols:
        df[col] = df[col].astype(object)
    return mod.predict_proba(df.fillna(0))[:,1]