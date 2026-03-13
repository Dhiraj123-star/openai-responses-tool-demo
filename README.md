# 🤖 OpenAI Responses API Tool Calling Demo

A lightweight **AI-powered backend service** demonstrating **OpenAI Tool Calling using the OpenAI Responses API** within a **FastAPI microservice architecture**.

This project showcases how an AI model can **autonomously decide to call external tools**, execute them locally, and generate a refined response for the user.

The application exposes a REST API where users submit natural language queries and the AI **dynamically selects and invokes tools when necessary**.

---

# 🚀 Core Features

## 🧠 OpenAI Responses API

Uses the **OpenAI Responses API** to support:

* Structured **tool calling**
* Iterative **agent workflows**
* Conversation state management using:

```
previous_response_id
```

This enables a **multi-step interaction loop** between the AI model and backend tools.

---

## 🔧 Dynamic AI Tool Calling

The AI agent can dynamically invoke tools based on user queries.

Currently implemented tools include:

* 🌦 Weather lookup
* 🧮 Calculator
* 🕒 Time utility

The model determines **which tool to call automatically** without any hardcoded routing logic.

---

## ⚡ FastAPI Microservice

The application exposes a **REST API built with FastAPI**, providing a lightweight and scalable backend service.

Available endpoints:

```
GET  /health
POST /ask
```

---

## 🐳 Containerized Deployment

The service is fully containerized using:

* Docker
* Docker Compose

This ensures **consistent environments for local development and deployment**.

---

## 🔐 Secure Configuration

Sensitive credentials such as the OpenAI API key are **not stored inside the Docker image**.

Instead they are injected at **runtime using environment variables**.

Example `.env` file:

```
OPENAI_API_KEY=your_api_key_here
```

Docker Compose loads the environment variables automatically.

---

## ⚙️ CI/CD Pipeline (GitHub Actions)

The project includes a **simple CI/CD pipeline using GitHub Actions**.

The pipeline automatically:

1️⃣ Builds the Docker image
2️⃣ Logs in to DockerHub
3️⃣ Pushes the image to DockerHub

DockerHub repository:

```
dhiraj918106/openai-responses-tool-demo
```

The pipeline runs automatically on every push to the **main branch**.

---

# 🧩 Modular Architecture

The project follows a **clean modular architecture** that separates responsibilities across components.

| Layer                | Responsibility                      |
| -------------------- | ----------------------------------- |
| API Layer            | FastAPI routes                      |
| AI Service Layer     | OpenAI orchestration                |
| Tool Registry        | Tool schemas exposed to OpenAI      |
| Tool Implementations | Local tool execution                |
| Configuration        | OpenAI client and environment setup |

This architecture allows **new tools to be added easily without modifying the AI orchestration logic**.

---

# 🧱 Project Structure

```
openai-responses-tool-demo
│
├── app
│   ├── main.py            # FastAPI application entrypoint
│   ├── ai_service.py      # OpenAI agent orchestration
│   ├── tools.py           # Tool implementations
│   ├── tool_registry.py   # Tool schemas exposed to OpenAI
│   ├── schemas.py         # API request/response models
│   └── config.py          # OpenAI client configuration
│
├── Dockerfile
├── docker-compose.yml
│
├── requirements.txt
├── .env
│
├── .github
│   └── workflows
│       └── docker-build.yml   # GitHub Actions CI/CD pipeline
│
└── README.md
```

---

# 🛠 Implemented Tools

## 🌦 Weather Tool

```
get_weather(city: str)
```

Returns simulated weather information.

Example:

```
The weather in Paris is 30°C and sunny.
```

---

## 🧮 Calculator Tool

```
calculate(expression: str)
```

Evaluates mathematical expressions.

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

The system follows an **AI agent execution loop**.

---

## 1️⃣ User Request

A user sends a question to the API:

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

## 2️⃣ AI Decision

The OpenAI model analyzes the question and determines whether a tool should be used.

Example tool call:

```
get_weather(city="Paris")
```

---

## 3️⃣ Local Tool Execution

The backend executes the corresponding Python function:

```
tools.get_weather()
```

---

## 4️⃣ Tool Output Submission

The tool result is returned to the model using:

```
previous_response_id
```

This allows the model to continue the reasoning process.

---

## 5️⃣ Final AI Response

The model generates the final response incorporating the tool output.

Example response:

```json
{
  "answer": "The weather in Paris is 30°C and sunny."
}
```

---

# ⚙️ Setup & Installation

## 1️⃣ Clone the Repository

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

The API will start at:

```
http://localhost:8000
```

Swagger UI:

```
http://localhost:8000/docs
```

---

# 🐳 Run with Docker

### Build the container

```
docker compose build
```

---

### Start the service

```
docker compose up
```

The API will run at:

```
http://localhost:8000
```

---

# 🩺 Health Check Endpoint

```
GET /health
```

Example response:

```json
{
  "status": "healthy",
  "service": "openai-tool-api"
}
```

---

# 🎯 Learning Outcomes

This project demonstrates:

* Using the **OpenAI Responses API**
* Implementing **AI Tool Calling**
* Designing **AI-powered FastAPI microservices**
* Creating **modular AI tool architectures**
* Building **containerized backend services**
* Implementing **CI/CD pipelines with GitHub Actions**

---

# 📜 License

MIT License

---
