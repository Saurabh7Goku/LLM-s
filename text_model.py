from flask import Flask, render_template, request
import openai

app = Flask(__name__)
openai.api_key = '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'
model_name = 'text-davinci-003'
questions = []  # List to store the asked questions
answers = []  # List to store the generated answers

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    prompt = request.form['prompt']
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=500,
        n=1,
        stop=None,
        temperature=0.7,
        top_p=None,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    reply = response.choices[0].text.strip()
    questions.append(prompt)
    answers.append(reply)
    return reply

if __name__ == '__main__':
    app.run(debug=True)

