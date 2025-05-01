from flask import Flask, request, jsonify

app = Flask(__name__)

# Serve a simple chat UI at "/"
@app.route('/', methods=['GET'])
def home():
    return """
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Custom ChatBot</title>
    <style>
      body { font-family: Arial, sans-serif; margin: 2em; }
      #chat { max-width: 600px; margin: auto; }
      #messages { list-style: none; padding: 0; }
      #messages li { margin-bottom: 1em; }
      input { width: 80%; padding: 0.5em; }
      button { padding: 0.5em 1em; }
    </style>
  </head>
  <body>
    <div id="chat">
      <h1>Chat with Bot</h1>
      <ul id="messages"></ul>
      <input id="input" placeholder="Type a message..." autofocus />
      <button onclick="sendMessage()">Send</button>
    </div>
    <script>
      async function sendMessage() {
        const inputEl = document.getElementById('input');
        const msg = inputEl.value;
        if (!msg) return;
        inputEl.value = '';
        const res = await fetch('/chat', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ message: msg })
        });
        const data = await res.json();
        const li = document.createElement('li');
        li.innerHTML = '<strong>You:</strong> ' + msg + '<br/><strong>Bot:</strong> ' + data.response;
        document.getElementById('messages').appendChild(li);
        window.scrollTo(0, document.body.scrollHeight);
      }
    </script>
  </body>
</html>
"""

@app.route('/chat', methods=['POST'])
def chat():
    user_msg = request.json.get('message', '')
    return jsonify({'response': __import__('chatbot').get_response(user_msg)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
