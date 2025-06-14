from flask import Flask, request, jsonify
from model import SimpleTextGenerator

app = Flask(__name__)

corpus = """
Artificial intelligence is changing the world. It powers voice assistants, automates tasks, and helps make decisions.
Machine learning and deep learning are important techniques in AI.
"""
generator = SimpleTextGenerator(corpus)

@app.route('/')
def index():
    return 'Simple Generative AI is running!'

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    start_word = data.get('start', 'Artificial')
    length = int(data.get('length', 10))
    result = generator.generate(start_word, length)
    return jsonify({'generated_text': result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
