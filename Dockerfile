# ---------- Builder Stage ----------
FROM python:3.12-slim AS builder

WORKDIR /install

RUN apt-get update && apt-get install -y build-essential

COPY requirements.txt .

RUN pip install --prefix=/install/deps --no-cache-dir -r requirements.txt


# ---------- Final Stage ----------
FROM python:3.12-slim

RUN useradd -m appuser

WORKDIR /app

# Copy installed dependencies
COPY --from=builder /install/deps /usr/local

# Copy application code
COPY app ./app

# Set ownership
RUN chown -R appuser:appuser /app

USER appuser

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
