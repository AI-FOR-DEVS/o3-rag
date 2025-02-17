from flask import Flask, request, jsonify,Response, render_template
from app import chat

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

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