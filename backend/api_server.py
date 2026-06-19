# backend/api_server.py
# The JSON Bridge for Hamnet-SA-V1 (Runs on Codespace)

from flask import Flask, request, jsonify
from flask_cors import CORS
from ugroove_encoder import UgrooveTernary

app = Flask(__name__)
CORS(app)  # Allows your browser to talk to this server

# Initialize the U-groove engine
processor = UgrooveTernary()

@app.route('/ping', methods=['GET'])
def ping():
    """Health check for the JSON bridge."""
    return jsonify({"status": "Ham Snuffer JSON Bridge is alive!"})

@app.route('/process', methods=['POST'])
def process():
    """Receives raw text, processes U-groove, returns JSON."""
    try:
        data = request.get_json()
        raw_input = data.get('input', '')
        
        if not raw_input:
            return jsonify({"error": "No input provided"}), 400
        
        # Convert text to bytes (simulating a sniffed packet)
        raw_bytes = raw_input.encode('utf-8')
        
        # Run the U-groove engine (using the class we just fixed)
        result = processor.process_packet(raw_bytes)
        
        # Return JSON response
        return jsonify({
            "success": True,
            "binary": result["binary_preview"],
            "ternary": result["ternary"],
            "original_size": result["original_size"],
            "compressed_size": result["compressed_size"],
            "ratio": result["ratio"]
        })
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    print("🚀 Ham Snuffer JSON Bridge is running on http://localhost:5000")
    print("📡 Send POST requests to /process with JSON body: {'input': 'your text'}")
    app.run(host='0.0.0.0', port=5000, debug=False)
