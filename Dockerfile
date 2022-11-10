FROM python:3.10

# Set the working directory
WORKDIR /app

# Install dependencies
COPY ./requirements.txt /app
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy the scripts to the folder
COPY . /app

# Start the server
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]