# -- Stage 1: Builder ---
FROM python:3.12-slim AS builder

WORKDIR /install

# Install build dependencies
RUN apt-get update && apt-get install -y build-essential

# Copy requirements
COPY requirements.txt .

# Install dependencies into temporary directory
RUN pip install --prefix=/install/deps --no-cache-dir -r requirements.txt

# ----- Stage 2: Runtime -----
FROM python:3.12-slim 

# Create non-root user
RUN useradd -m appuser

WORKDIR /app

# Copy install dependencies from builder
COPY --from=builder /install/deps /usr/local

# Copy project files
COPY app ./app
COPY .env .

# Change ownership
RUN chown -R appuser:appuser /app

# Switch to non-root user
USER appuser

# Expose FastAPI port
EXPOSE 8000

# Run FastAPI
CMD ["uvicorn","app.main:app","--host","0.0.0.0","--port","8000","--workers","2"]
