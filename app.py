from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form['message']

    if "hello" in user_message.lower():
        bot_reply = "Hello! How can I help you?"
    elif "python" in user_message.lower():
        bot_reply = "Python is a powerful programming language."
    elif "bye" in user_message.lower():
        bot_reply = "Goodbye!"
    else:
        bot_reply = "Sorry, I don't understand."

    return render_template(
        'chat.html',
        user_message=user_message,
        bot_reply=bot_reply
    )

if __name__ == '__main__':
    app.run(debug=True)
