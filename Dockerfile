# Use Microsoft’s official Playwright image (comes with Chromium, Firefox, WebKit, and GLIBC)
FROM mcr.microsoft.com/playwright/python:v1.43.0-jammy

# Set working directory inside the container
WORKDIR /app

# Copy all project files into the container
COPY . .

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Run your bot
CMD ["python", "fivesurveys_bot.py"]
