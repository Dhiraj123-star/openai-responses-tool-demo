# 🤖 OpenAI Responses API Tool Calling Demo

A simple **AI-powered backend service** demonstrating **OpenAI Tool Calling using the Responses API** with a **FastAPI microservice architecture**.

This project showcases how an AI model can **autonomously decide to call external tools**, execute them locally, and return a refined response to the user.

The application exposes a REST API where users send natural language questions and the AI dynamically invokes tools when required.

---

# 🚀 Core Features

### 🧠 OpenAI Responses API

Uses the **latest OpenAI Responses API** to support structured **tool calling** and maintain conversation state using `previous_response_id`.

---

### 🔧 AI Tool Calling

The AI agent can dynamically call tools such as:

* 🌦 Weather information
* 🧮 Calculator
* 🕒 Time utility

The model decides **which tool to use automatically**.

---

### ⚡ FastAPI Microservice

A lightweight and scalable **REST API service** built with FastAPI.

Endpoints include:

```
GET  /health
POST /ask
```

---

### 🐳 Dockerized Deployment

The application can run in a **containerized environment** using:

* Docker
* Docker Compose

---

### 🔐 Secure Configuration

Sensitive credentials are stored in a `.env` file and loaded using environment variables.

```
OPENAI_API_KEY
```

---

### 🧩 Modular Architecture

The project follows a **clean separation of concerns**:

* API Layer
* AI orchestration layer
* Tool implementations
* Configuration management

This structure allows easy addition of **new AI tools**.

---

# 🧱 Project Structure

```
openai-responses-tool-demo
│
├── app
│   ├── main.py            # FastAPI application
│   ├── ai_service.py      # OpenAI tool-calling orchestration
│   ├── tools.py           # Tool implementations
│   ├── tool_registry.py   # Tool schemas for OpenAI
│   ├── schemas.py         # Request/response models
│   └── config.py          # OpenAI client configuration
│
├── Dockerfile
├── docker-compose.yml
│
├── requirements.txt
├── .env
└── README.md
```

---

# 🛠 Implemented Tools

## 🌦 Weather Tool

```
get_weather(city: str)
```

Example output:

```
The weather in Paris is 30°C and sunny.
```

---

## 🧮 Calculator Tool

```
calculate(expression: str)
```

Example:

```
Input: 345 * 22
Output: 7590
```

---

## 🕒 Time Tool

```
get_time(city: str)
```

Returns the current **UTC time** using a timezone-aware datetime object.

Example:

```
Current UTC time is 14:22:10
```

---

# 🧠 Tool Calling Execution Flow

The system follows a **two-step agent interaction pattern**.

---

### 1️⃣ User Request

User sends a question:

```
POST /ask
```

Example request:

```json
{
  "question": "What is the weather in Paris?"
}
```

---

### 2️⃣ AI Decision

The OpenAI model analyzes the query and decides whether to call a tool.

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

### 4️⃣ Tool Output Submission

The tool result is sent back to the model using:

```
previous_response_id
```

---

### 5️⃣ Final AI Response

The model combines reasoning with the tool output and returns the final answer.

Example:

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

API will start at:

```
http://localhost:8000
```

Swagger documentation:

```
http://localhost:8000/docs
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

---

# 🩺 Health Check

```
GET /health
```

Response:

```json
{
  "status": "healthy",
  "service": "openai-tool-api"
}
```

---

# 🎯 Learning Outcomes

This project demonstrates:

* Using **OpenAI Responses API**
* Implementing **AI Tool Calling**
* Designing **AI microservices with FastAPI**
* Creating **modular AI tool architectures**
* Building **containerized AI services**
* Implementing **agent-tool interaction workflows**

---

# 📌 Future Improvements

Possible enhancements:

* Streaming AI responses
* Parallel tool execution
* Observability and logging
* External API integrations
* Multi-agent orchestration
* Rate limiting and authentication

---

# 📜 License

MIT License

---
