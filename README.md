# 🤖 OpenAI Responses API Tool Calling Demo

A simple **AI-powered backend service** demonstrating **OpenAI Tool Calling using the Responses API** with a **FastAPI microservice architecture**.

This project shows how an AI model can **autonomously decide to call external tools**, execute them locally, and return a refined response to the user.

The application exposes a REST API where users send natural language questions and the AI dynamically invokes tools when required.

---

# 🚀 Core Features

### 🧠 OpenAI Responses API

Uses the **latest Responses API** to enable structured tool calling and maintain conversation context.

### 🔧 Tool Calling Workflow

The AI can automatically trigger external tools such as:

* Weather information tool

### ⚡ FastAPI Backend

Provides a clean and scalable REST API service.

### 🐳 Dockerized Deployment

The service can run inside a container using **Docker and Docker Compose**.

### 🔐 Secure Configuration

Uses environment variables (`.env`) to securely manage API keys.

### 🧩 Modular Architecture

Separates:

* API layer
* AI orchestration
* Tool logic
* Configuration

---

# 🧱 Project Structure

```
openai-responses-tool-demo
│
├── app
│   ├── main.py          # FastAPI application entrypoint
│   ├── ai_service.py    # OpenAI Responses API orchestration
│   ├── tools.py         # External tool implementations
│   └── config.py        # OpenAI client configuration
│
├── Dockerfile           # Production Docker image
├── docker-compose.yml   # Container orchestration
│
├── requirements.txt
├── .env
└── README.md
```

---

# 🛠 Implemented Tool

## Weather Tool

```
get_weather(city: str)
```

Returns weather information for a given city.

Example:

Input

```
Paris
```

Output

```
The weather in Paris is 30°C and sunny.
```

---

# 🧠 Tool Calling Execution Flow

The system follows a **two-step agentic interaction pattern** with the OpenAI API.

### 1️⃣ User Request

A user sends a question to the API:

```
POST /ask
```

Example:

```json
{
  "question": "What is the weather in Paris?"
}
```

---

### 2️⃣ Model Tool Decision

The OpenAI model determines that the request requires external data and returns a **tool call request**.

Example:

```
get_weather(city="Paris")
```

---

### 3️⃣ Local Tool Execution

The backend executes the corresponding Python function:

```
tools.get_weather()
```

---

### 4️⃣ Tool Result Submission

The result is sent back to the OpenAI API using:

```
previous_response_id
```

---

### 5️⃣ Final AI Response

The model combines reasoning with the tool output and returns a final answer.

Example response:

```json
{
  "answer": "The weather in Paris is 30°C and sunny."
}
```

---

# ⚙️ Setup & Installation

## 1️⃣ Clone Repository

```
git clone https://github.com/dhiraj123-star/openai-responses-tool-demo.git
cd openai-responses-tool-demo
```

---

## 2️⃣ Create Environment File

Create a `.env` file:

```
OPENAI_API_KEY=your_api_key_here
```

---

## 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

## 4️⃣ Run the API

```
uvicorn app.main:app --reload
```

---

# 🐳 Run with Docker

### Build container

```
docker compose build
```

### Start service

```
docker compose up
```

API will be available at:

```
http://localhost:8000
```

Swagger UI:

```
http://localhost:8000/docs
```

---

# 🎯 Learning Outcomes

This project demonstrates:

* Using **OpenAI Responses API**
* Implementing **LLM Tool Calling**
* Designing **AI microservices with FastAPI**
* Managing **agent-tool interaction loops**
* Containerizing AI services with **Docker**

---

# 📌 Future Improvements

Planned enhancements:

* Add **health check endpoint**
* Add **multiple tools (calculator, time, etc.)**
* Implement **dynamic tool routing**
* Support **multi-agent orchestration**
* Add **observability and logging**

---

# 📜 License

MIT License

---
