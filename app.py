from flask import Flask, request, jsonify
from flask_cors import CORS  # import CORS

app = Flask(__name__)
CORS(app, origins=["http://localhost:5173"])  # allow only your frontend origin

# Simple in-memory store for demo
posts = {}

@app.route('/post', methods=['POST'])
def create_post():
    # Parse text fields from form
    chain_name = request.form.get('chainName')
    chain_id = request.form.get('chainId')
    token_name = request.form.get('tokenName')
    token_symbol = request.form.get('tokenSymbol')
    initial_supply = request.form.get('initialSupply')
    decimal_precision = request.form.get('decimalPrecision')
    block_time = request.form.get('blockTime')
    gas_limit = request.form.get('gasLimit')
    validator_count = request.form.get('validatorCount')
    predeployed_contracts = request.form.get('predeployedContracts')

    # For validators, you might want to accept JSON string inside form data
    validators_json = request.form.get('validators')
    if validators_json:
        import json
        try:
            validators = json.loads(validators_json)
        except Exception as e:
            return jsonify({"error": "Invalid validators JSON"}), 400
    else:
        validators = []

    # Access files
    files = request.files.getlist('uploadContracts')  # multiple files

    # Debug print (remove later)
    print(f"Received chainName={chain_name}, validators={validators}")
    print(f"Files count: {len(files)}")

    # You can save files if you want
    saved_files = []
    for file in files:
        if file.filename == '':
            continue
        # Save file somewhere (demo, saving in /tmp)
        filepath = f"/tmp/{file.filename}"
        file.save(filepath)
        saved_files.append(file.filename)

    # Now respond
    return jsonify({
        "message": "Post received",
        "chainName": chain_name,
        "validatorsCount": len(validators),
        "filesSaved": saved_files
    }), 201




if __name__ == '__main__':
    app.run(debug=True)
