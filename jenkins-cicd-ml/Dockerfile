FROM python:3.10-slim-buster

RUN apt-get update && apt-get install -y \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

# Copy code to the container
COPY . /code

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade -r /code/src/requirements.txt

# Expose port
EXPOSE 8005

# Set the working directory
WORKDIR /code/src

# Add the code directory to PYTHONPATH
ENV PYTHONPATH "${PYTHONPATH};/code/src"

# Install the package in editable mode and run it
CMD pip install -e . && python main.py
