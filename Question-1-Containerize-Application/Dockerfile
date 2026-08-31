# 1. Base image layer: Minimal Python runtime
FROM python:3.11-slim

# 2. Set working directory
WORKDIR /app

# 3. Environment settings to optimize Python in container
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# 4. Copy dependency specification first for layer caching
COPY requirements.txt .

# 5. Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copy the rest of the application source code
COPY app.py .

# 7. Expose the port the app listens on
EXPOSE 5000

# 8. Define default command to execute
CMD ["python", "app.py"]
