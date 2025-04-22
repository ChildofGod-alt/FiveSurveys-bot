
from playwright.sync_api import sync_playwright
import time
import random

# === Configuration ===
EMAIL = "precieux2911@gmail.com"
SURVEYS_TO_COMPLETE = random.randint(10, 15)  # Random daily target
ANSWER_WAIT_RANGE = (1.5, 4.5)  # Delay range between answers to simulate human behavior


# === Function to simulate random wait time ===
def human_delay():
    delay = random.uniform(*ANSWER_WAIT_RANGE)
    time.sleep(delay)


# === Main Bot Logic ===
def run_bot():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        print("Navigating to Five Surveys...")
        page.goto("https://www.fivesurveys.com/en-gb")

        human_delay()

        # Click login/signup
        page.click("text=Log in / Sign up")

        human_delay()

        # Fill in email and submit
        page.fill("input[type='email']", EMAIL)
        page.click("text=Continue")

        print("Logging in...")

        # Wait for login to complete (simulate a wait or confirm login success)
        page.wait_for_timeout(5000)

        # Start clicking and completing surveys
        surveys_done = 0
        while surveys_done < SURVEYS_TO_COMPLETE:
            print(f"Survey round: {surveys_done+1}")

            # Find and click the first available survey
            surveys = page.query_selector_all("div:has-text('min')")  # Simple selector by duration
            if not surveys:
                print("No surveys available.")
                break

            survey = surveys[0]
            survey.click()

            try:
                page.wait_for_timeout(3000)

                # Check for common trap question
                if page.is_visible("text=A boy had 4 marbles"):
                    page.click("text=3")

                # Example region question
                if page.is_visible("text=Which region do you live?"):
                    page.click("text=London")

                # Click continue
                page.click("button:has-text('→')")

                page.wait_for_timeout(5000)
                print("Answered initial questions.")

                # Wait and finish survey (simulate)
                page.wait_for_timeout(10000)

                surveys_done += 1

                # Return to home screen
                page.goto("https://www.fivesurveys.com/en-gb")

            except Exception as e:
                print("Survey error:", e)

            human_delay()

        print("Finished session.")
        browser.close()

run_bot()
