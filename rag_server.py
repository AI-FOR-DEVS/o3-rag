from flask import Flask, request, jsonify
from app import chat

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat_endpoint():
    data = request.json
    query = data['query']
    response = chat(query)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True, port=8080)