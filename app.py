import os

from flask import Flask, redirect, render_template, request, session, url_for

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-secret-key")

QUICK_PROMPTS = [
    "What can you do?",
    "Tell me about Python",
    "Help me build a website",
    "Show advanced features",
]


def generate_reply(message: str) -> str:
    text = message.lower().strip()

    if not text:
        return "Please type a message so I can help."
    if any(word in text for word in ["hello", "hi", "hey"]):
        return "Hello! I'm your assistant. Ask me about Python, web apps, or chatbot ideas."
    if "python" in text:
        return "Python is great for automation, web apps, AI, and data work. Want a project idea?"
    if any(word in text for word in ["build", "website", "deploy"]):
        return "I can help you plan, build, and deploy a Flask app step by step."
    if "feature" in text or "advanced" in text:
        return "Advanced upgrades can include chat history, dark mode, AI API integration, and database storage."
    if "bye" in text or "goodbye" in text:
        return "Goodbye! Come back anytime."
    return "I'm still learning, but I can help with Flask, Python, UI ideas, and deployment."


@app.route("/")
def home():
    chat_history = session.get("chat_history", [])
    return render_template(
        "index.html",
        chat_history=chat_history,
        quick_prompts=QUICK_PROMPTS,
    )


@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.form.get("message", "").strip()
    bot_reply = generate_reply(user_message)

    chat_history = session.get("chat_history", [])
    chat_history.append({"role": "user", "message": user_message})
    chat_history.append({"role": "assistant", "message": bot_reply})
    session["chat_history"] = chat_history[-20:]

    return redirect(url_for("home"))


@app.route("/clear", methods=["POST"])
def clear_chat():
    session.pop("chat_history", None)
    return redirect(url_for("home"))


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    debug = os.environ.get("FLASK_DEBUG", "0") == "1"
    app.run(host="0.0.0.0", port=port, debug=debug)
