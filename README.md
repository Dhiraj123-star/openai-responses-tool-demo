# 🤖 OpenAI Responses API Tool Calling Demo

This is a technical overview and guide for the **Response-Flow** project, a Python-based implementation of the OpenAI Responses API. This project demonstrates how an AI agent can autonomously decide to use external tools, execute them locally, and deliver a refined answer to the user.

---

### 🚀 Core Features

* **Native State Management:** Utilizes the 2026 Responses API `previous_response_id` to maintain context without manually managing message arrays.
* **Agentic Logic:** Features an LLM that identifies when a query requires data it doesn't possess (like real-time weather).
* **Secure Configuration:** Uses environment-based API key management to prevent credential leaking.
* **Modular Design:** Separates the LLM orchestration from the actual tool logic for easy scaling.

---

### 🧱 Project Structure

**Folder: response-flow/**

* **main.py:** The entry point. It contains the "Response Loop" that handles the handshake between the user, the OpenAI model, and the local tools.
* **tools.py:** A dedicated library of Python functions. For this demo, it contains the `get_weather` function.
* **registry.py:** Contains the JSON schemas that describe your tools to the OpenAI model so it knows how to call them.
* **.env:** A private file for your `OPENAI_API_KEY`.
* **requirements.txt:** Lists the necessary libraries: `openai` and `python-dotenv`.

---

### 🛠 Implementation: The Weather Tool

The primary tool used in this demo is a weather fetcher.

**Function Signature:** `get_weather(location: str)`
**Example Input:** `"Paris"`
**Example Output:** `"22°C, Partly Cloudy"`

---

### 🧠 The Two-Step Execution Flow

The Responses API operates on a "Action-Submission" loop:

1. **The Trigger:** The user asks, "Do I need an umbrella in London?" The application sends this to the Responses API.
2. **The Requirement:** The model returns a status of `requires_action`. It specifically asks for the `get_weather` tool with the argument `{"location": "London"}`.
3. **The Local Execution:** Your Python code sees this request, runs the `get_weather` function in `tools.py`, and gets the real-time data.
4. **The Submission:** The code uses `client.responses.submit_tool_outputs` to send that data back.
5. **The Final Response:** The model receives the weather data, realizes it's raining, and tells the user: "Yes, you should take an umbrella; it's currently raining in London."

---

### ⚙️ Setup and Installation

1. **Clone & Enter:** Pull the repository and move into the project directory.
2. **Environment:** Create a `.env` file and paste your `OPENAI_API_KEY`.
3. **Dependencies:** Run `pip install -r requirements.txt`.
4. **Launch:** Run `python main.py` to start the interactive console.

---

### 🎯 Learning Outcomes

By exploring this project, you will master:

* Transitioning from "Chat" models to "Response" agents.
* Defining **Strict Mode** JSON schemas for tool calling to ensure the AI never sends malformed arguments.
* Handling the server-side state of the Responses API.

---

