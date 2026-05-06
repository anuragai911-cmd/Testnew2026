# 🚀 AI Audit Engineering: The Beginner's Guide
*A step-by-step guide for the future IT Audit AI Engineer*

Welcome! You've successfully built a professional UI. Now, let's learn how to make it "Live" by connecting it to a real AI brain (OpenAI).

---

## 1. Core Concepts (The Basics)

In the software world, we use a **Three-Tier Architecture**:

1.  **THE FRONTEND (`ai_tester_pro.html`):**
    *   This is the "Face" of your app.
    *   It's what you see in the browser.
    *   Think of it like the **steering wheel and dashboard** of a car.

2.  **THE BACKEND (`app.py`):**
    *   This is the "Engine".
    *   It runs on your computer (not in the browser).
    *   It's where we keep the secrets (like your API Key) hidden.

3.  **THE API (OpenAI):**
    *   This is the "External Brain".
    *   Our Backend asks it questions, and it sends back smart answers.

---

## 2. Setting Up Your Machine (First Time Only)

To run this, you need **Python** installed.

### Step A: Install the "Connectors"
Open your terminal (Command Prompt or Terminal) and type this:
```bash
pip install flask flask-cors openai
```
*Wait for it to finish. This installs the tools needed for Python to talk to the web and the AI.*

### Step B: Get your Secret Key
1. Go to [platform.openai.com](https://platform.openai.com) and create an account.
2. Create an **API Key**.
3. **COPY IT** and paste it into `app.py` where it says `YOUR_OPENAI_API_KEY_HERE`.

---

## 3. How to Start the App (The Workflow)

Always follow this order:

1.  **START THE BRAIN:**
    *   Run `python app.py` in your terminal.
    *   You should see: `Running on http://127.0.0.1:5000`.
    *   *Keep this window open!*

2.  **OPEN THE FACE:**
    *   Open `ai_tester_pro.html` in your browser.

3.  **AUDIT:**
    *   Fill in your attributes, upload a file, and click **"Execute Real AI Audit"**.

---

## 4. How the "Magic" Happens

1. You click the button in your **Browser**.
2. The browser sends a `POST` request (like a digital letter) to your **Python Server**.
3. Python takes that letter, adds your **Secret Key**, and sends it to **OpenAI**.
4. OpenAI reads the attributes and evidence, thinks about it, and sends a **JSON** response back.
5. Python sends that JSON back to your **Browser**.
6. The Browser updates the **Chart and findings** instantly!

---

## 5. Pro Tips for your 15-year-old self:
- **DEBUGGING:** If it doesn't work, check the black terminal window where `app.py` is running. It will tell you the error in plain English.
- **COST:** Using the API costs a few pennies per use. Monitor your usage on the OpenAI website.
- **MODELS:** I used `gpt-4o`. It's currently the smartest model for understanding images and audit logic.
