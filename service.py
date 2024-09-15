from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/data', methods=['GET'])
def exchange_crypto():
    lala_sample = {"lala": "bitcoin"}
    return jsonify(lala_sample)


@app.route('/test_api', methods=['GET'])
def test_api():
    data = {"test": "yoo yoo api"}
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8055)