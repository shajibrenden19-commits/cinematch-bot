from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from openai import OpenAI
import os

app = Flask(__name__)

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

@app.route("/", methods=["POST"])
def bot():
    user_msg = request.form.get("Body")

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are CineMatch AI. Recommend movies clearly and briefly."},
            {"role": "user", "content": user_msg}
        ]
    )

    ai_reply = response.choices[0].message.content

    resp = MessagingResponse()
    resp.message(ai_reply)

    return str(resp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
