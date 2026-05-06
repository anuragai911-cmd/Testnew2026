# ---------------------------------------------------------
# STEP 1: THE "BRAIN" (BACKEND SERVER)
# ---------------------------------------------------------
# This is a Python file that stays on YOUR computer.
# It acts as a "Middleman".
#
# Why a middleman? Because your API Key is like a credit card.
# If you put it in the HTML file, anyone on the internet can steal it.
# This file keeps it hidden and safe.

from flask import Flask, request, jsonify
from flask_cors import CORS # This allows our website to talk to this server
import openai
import os

# 1. SETUP: Create the app
app = Flask(__name__)
CORS(app) # Enable communication from our website

# 2. THE SECRET KEY:
# In a real app, we use "Environment Variables".
# For now, we will assume you have it in a variable.
# NEVER share this key with anyone!
openai.api_key = "YOUR_OPENAI_API_KEY_HERE"

@app.route('/test-control', methods=['POST'])
def test_control():
    """
    This is an "Endpoint". It's like a specific mailbox for our website.
    The website sends data here, and we process it.
    """
    try:
        # Get the data sent from our website
        data = request.json
        description = data.get('description')
        attributes = data.get('attributes')
        evidence_text = data.get('evidence_text')

        # 3. TALKING TO THE AI (OpenAI)
        # We send a specific request to the AI model
        response = openai.chat.completions.create(
            model="gpt-4o", # The "smart" model
            messages=[
                {"role": "system", "content": "You are a Senior IT Auditor. Analyze evidence against control attributes and return a score (0-10), status (Pass/Fail), and improvements in JSON format."},
                {"role": "user", "content": f"Control: {description}\nAttributes: {attributes}\nEvidence: {evidence_text}"}
            ],
            response_format={ "type": "json_object" } # We want the AI to reply in a way our code can understand easily
        )

        # 4. SENDING IT BACK:
        # We take the AI's answer and send it back to the website.
        result = response.choices[0].message.content
        return result

    except Exception as e:
        print(f"Error occurred: {e}")
        return jsonify({"error": "Something went wrong with the AI connection"}), 500

# 5. START: Run the server
if __name__ == '__main__':
    print("--- Audit AI Backend is Starting! ---")
    print("Running on http://127.0.0.1:5000")
    app.run(debug=True, port=5000)
