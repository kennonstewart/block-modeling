# .devcontainer/Dockerfile
FROM python:3.11-slim

# Set up a working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
COPY pyproject.toml .
COPY src/ src/
COPY tests/ tests/

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install -e .

# Optional: install extra tools
RUN apt-get update && apt-get install -y git vim

# Default command
CMD ["bash"]
