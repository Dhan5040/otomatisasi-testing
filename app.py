# file: app.py
from flask import Flask, jsonify
import logging
logging.basicConfig(filename="logs/app.log", level=logging.INFO)
app = Flask(__name__)

@app.route('/ping')
def ping():
    app.logger.info("Request masuk ke /ping")
    return jsonify({"message": "pong"})

def tambah(a, b):
    return a + b

# Tambahkan ini:
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
