# Use a compatible Playwright image based on Ubuntu 20.04 (focal)
FROM mcr.microsoft.com/playwright/python:v1.32.0-focal

# Set working directory
WORKDIR /app

# Copy all project files
COPY . .

# Install dependencies
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Run your bot
CMD ["python", "fivesurveys_bot.py"]
