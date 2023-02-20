from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/donate', methods=['POST'])
def donate():
    data = request.json
    
    if 'amount' not in data:
        return jsonify({'error': 'Missing amount parameter'}), 400
    
    # Here you can add your code to process the donation and store it in your database or payment gateway
    
    return jsonify({'message': 'Donation processed successfully'}), 200

if __name__ == '__main__':
    app.run()