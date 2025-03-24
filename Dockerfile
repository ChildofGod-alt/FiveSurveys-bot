
# Use the official Python 3.10 base image
FROM mcr.microsoft.com/playwright/python:v1.43.1-jammy

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container
COPY . .

# Install dependencies
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Run the bot script
CMD ["python", "fivesurveys_bot.py"]
