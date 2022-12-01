from flask import jsonify, request, Flask
import joblib
import pandas as pd


app = Flask(__name__)
model = joblib.load('fbprophet.pkl')

@app.route("/predict", methods=["POST"])
def predict_gold():
    """
    Given the date, predict the gold price for next date
    """
    date_given = request.form["date"]
    df = pd.DataFrame()
    df['ds'] = [pd.to_datetime(date_given)]
    pred = model.predict(df)
    return jsonify(
            {
                "given_date": date_given,
                "price": float(pred['yhat'])
            }
        )
if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)
