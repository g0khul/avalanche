from flask import Flask, request, jsonify
from flask_cors import CORS  # import CORS

app = Flask(__name__)
CORS(app, origins=["http://localhost:5173", "http://127.0.0.1:5000"])  # allow only your frontend origin

# Simple in-memory store for demo
posts = {}

@app.route('/post', methods=['POST'])
def create_post():
    print("hi---------")
    request_data = request.get_json()

    # Parse text fields from form
    chain_name = request_data.get('chain_name')
    chain_id = request_data.get('chain_id')
    token_name = request_data.get('token_name')
    token_symbol = request_data.get('token_symbol')
    initial_supply = request_data.get('initial_token_supply')
    decimal_precision = request_data.get('token_decimal_precision')
    block_time = request_data.get('block_time')
    gas_limit = request_data.get('gas_limit_per_block')
    validators = request_data.get('validators')
    network_type = request_data.get('network_type')
    predeployed_contracts = request_data.get('contract_files')
    contract_names = request_data.get('contract_names')
    constructor_args = request_data.get('constructor_args')
    special_transaction_fees = request_data.get('special_transaction_fees')

    # Access files
    files = request.files.getlist('uploadContracts')

    print("files : ", files)

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
      "total_nodes": 4,
      "active_nodes": 4,
      "inactive_nodes": 0,
      "node_data": [
        {
          "node_id": "Node 1",
          "stake_amount": "100",
          "stake_start_time": "1754809359",
          "stake_end_time": "1755673359",
          "reward_address": "0x981A16164D8514B2CB3730Ea72C8D1268E75c7eA",
        },
        {
          "node_id": "Node 2",
          "stake_amount": "100",
          "stake_start_time": "1754809359",
          "stake_end_time": "1755673359",
          "reward_address": "0x04fe1A220C592C40ae931Bae08731d50380cE14f",
        },
        {
          "node_id": "Node 3",
          "stake_amount": "100",
          "stake_start_time": "1754809359",
          "stake_end_time": "1755673359",
          "reward_address": "0x0f892c20F1cbd837a7043754036A340BbC9F3Be6",
        },
        {
          "node_id": "Node 4",
          "stake_amount": "100",
          "stake_start_time": "1754809359",
          "stake_end_time": "1755673359",
          "reward_address": "0xFF4C51466BF8bF05eD36A984dCAD7600E3F958a3",
        },
      ],
    }), 201




if __name__ == '__main__':
    app.run(debug=True)
