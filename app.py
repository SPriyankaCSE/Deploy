from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    text = data.get('text')
    # Dummy model logic
    prediction = "Positive" if "good" in text.lower() else "Negative"
    return jsonify({"text": text, "prediction": prediction})

if __name__ == '__main__':
    app.run()