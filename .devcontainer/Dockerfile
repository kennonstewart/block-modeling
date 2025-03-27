# .devcontainer/Dockerfile
FROM python:3.11-slim

# Set up a working directory
WORKDIR /workspace

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Optional: install extra tools
RUN apt-get update && apt-get install -y git vim

# Default command
CMD ["bash"]
