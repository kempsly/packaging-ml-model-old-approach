FROM python:3.10-slim-buster

RUN apt-get update && apt-get install -y \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

# Copy code to the container
COPY . /code

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade -r /code/src/requirements.txt

# Set execute permissions for scripts in the /code/src directory
RUN chmod +x /code/src/*.py

# Set execute permissions for files in the /code/src/loan_pred_model directory
RUN chmod +x -R /code/src/loan_pred_model

# Expose port
EXPOSE 8005

# Set the working directory
WORKDIR /code/src

# Add the code directory to PYTHONPATH
ENV PYTHONPATH "${PYTHONPATH};/code/src;/code/src/loan_pred_model"

# Install the package in editable mode and run it
CMD pip install -e . && python main.py
