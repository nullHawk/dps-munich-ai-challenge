import joblib
import pandas as pd

# Load the SARIMA model and training data
try:
    model = joblib.load('data/sarima.pkl')
    print("Model loaded successfully.")
except Exception as e:
    print(f"Error loading model: {e}")
    model = None  # Set model to None if loading fails

try:
    df_train = pd.read_csv('data/df_train.csv', index_col='MONAT', parse_dates=True)
    print("Training data loaded successfully.")
except Exception as e:
    print(f"Error loading training data: {e}")
    df_train = None  # Set df_train to None if loading fails



def predict(year: int, month: int):
    """Predict the value for a given year and month."""
    global model, df_train
    try:
        target_date = pd.Timestamp(year=year, month=month, day=1)
        last_known_date = df_train.index[-1]
        steps_to_forecast = (target_date.year - last_known_date.year) * 12 + target_date.month - last_known_date.month

        if steps_to_forecast > 0:
            prediction = model.get_forecast(steps=steps_to_forecast).predicted_mean.iloc[-1]
        else:
            prediction = df_train.loc[target_date.strftime('%Y-%m-%d')]['WERT'] if target_date in df_train.index else "Unknown date"
    except Exception as e:
        print(f"Error during prediction: {e}")
        prediction = str(e)

    return {"prediction": prediction}
