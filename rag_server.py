from flask import Flask, request, jsonify
from app import chat
from flask import Response

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat_endpoint():
    data = request.json
    query = data['query']

    def stream_with_context(query):
        for chunk in chat(query):
            yield chunk

    return Response(stream_with_context(query), mimetype='text/event-stream')

if __name__ == '__main__':
    app.run(debug=True, port=8080)