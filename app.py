from flask import Flask, render_template, request, jsonify
from but import main
import threading
import numpy as np
from openai_utils import initialize_openai, read_api_key


app = Flask(__name__)


api_key = read_api_key("openai_api_key.txt")
initialize_openai(api_key)

messages = []
context = []
message_summarys = []


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    message = request.get_json()['message']
    response = main(message, messages, message_summarys, context)
    return jsonify({'response': response})



if __name__ == '__main__':
    app.run(debug=True)
