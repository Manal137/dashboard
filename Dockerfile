# FROM python:3.12-slim

# WORKDIR /app

# # Install system dependencies
# RUN apt-get update && apt-get install -y \
#     gcc \
#     python3-dev \
#     curl \
#     && rm -rf /var/lib/apt/lists/*

# # Copy requirements first for better caching
# COPY requirements.txt .
# RUN pip install -r requirements.txt 



# COPY . /app/
# # Set environment variables
# ENV PYTHONPATH=/app:/app/bladerunner
# ENV FLASK_APP=app.py
# ENV FLASK_ENV=development
# ENV PYTHONUNBUFFERED=1

# # Expose port
# EXPOSE 8050

# # Add healthcheck
# HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
#     CMD curl -f http://localhost:8050/health || exit 1

# # Run the application
# CMD ["python", "app.py"]

FROM python:3.12-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV FLASK_ENV=production
ENV PYTHONPATH=/app:/app/bladerunner

# Expose port
EXPOSE 8050

# Health check endpoint
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:8050/health || exit 1

# Run the application
CMD ["python", "app.py"]
