# Use the official Playwright base image with Python 3.10
FROM mcr.microsoft.com/playwright/python:v1.43.1-jammy

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container
COPY . .

# Install Python dependencies and Playwright browsers
RUN pip install --upgrade pip \
    && pip install -r requirements.txt \
    && playwright install --with-deps

# Run the bot script
CMD ["python", "fivesurveys_bot.py"]
