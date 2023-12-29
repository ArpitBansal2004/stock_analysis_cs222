from flask import Flask, render_template, jsonify
from modeltrain import predict_and_save_stock_graph

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict/<stock_code>')
def predict(stock_code):
    try:
        print(f"Received request for stock code: {stock_code}")
        image_path = predict_and_save_stock_graph(stock_code)  # This might throw an exception for invalid stock code
        return jsonify({"chartPath": image_path})
    except Exception as e:
        print(f"Error during prediction for {stock_code}: {e}")
        return jsonify({"error": "Failed to generate chart for the given stock symbol."}), 400

if __name__ == '__main__':
    app.run(debug=True)
