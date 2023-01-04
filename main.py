import os
import openai
import flask
from flask import Flask, render_template


# If you have the OpenAI API key as an environment variable, enable the below
# openai.api_key = os.getenv("OPENAI_API_KEY")

# If you have the OpenAI API key as a string, enable the below
openai.api_key = "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"

app = flask.Flask(__name__)

@app.route('/')
def my_html_page():
    return render_template('index.html')

@app.route("/api/send-message", methods=["POST"])
def send_message():
    # Get the message from the request data
    txtmessage = flask.request.form.get("message")

    # Generate a response from the OpenAI API
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=txtmessage,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
    )

    html = response.choices[0].text.replace("\n", "<br>")
    labels = ["Company Name:", "Address:", "Contact Person:", "Region:", "Phone Numbers:", "Email Address:", "Website:"]

    for label in labels:
        html = html.replace(label, "<b>" + label + "</b>")

    return flask.jsonify(html)

    # Return the response as JSON
    return flask.jsonify(response.choices[0].text)

if __name__ == "__main__":
    app.run()
