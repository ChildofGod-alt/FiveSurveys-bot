# Use official Playwright + Python base image
FROM mcr.microsoft.com/playwright/python:v1.43.1-jammy

# Set working directory
WORKDIR /app

# Copy contents
COPY . .

# Install Python dependencies and Playwright browser binaries
RUN pip install --upgrade pip \
    && pip install -r requirements.txt \
    && playwright install --with-deps

# Run the bot
CMD ["python", "fivesurveys_bot.py"]
