# AI Powered Chatbot

## Description

AI Powered Chatbot is a web-based application developed using Python and Flask.

## Features

* User-friendly interface
* Instant responses
* Web-based chatbot
* Built using Flask framework
* Modern responsive chat layout
* Conversation history in session
* Quick prompt chips for faster input
* Render-ready deployment setup

## Technologies Used

* Python
* Flask
* HTML
* CSS

## Possible Advanced Upgrades

* Connect a real AI model or API
* Store chat history in SQLite or PostgreSQL
* Add markdown rendering for richer replies
* Add user login and separate chat sessions
* Add voice input and text-to-speech
* Add dark/light theme toggle

## Run Locally

```bash
pip install -r requirements.txt
python app.py
```

## Deploy on Render

1. Push this project to GitHub.
2. Go to Render and create a new `Web Service`.
3. Connect your GitHub repository.
4. Use these settings:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
5. Deploy the app.

## Author

Harshda Shinde
