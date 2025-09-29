from playwright.sync_api import sync_playwright
import time


with sync_playwright() as p:
    # Launching a Browser
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://reddit.com")

    # Click the login button and enter id and password.
    page.locator("#login-button").click()
    time.sleep(2)

    page.locator("#login-username").click()
    time.sleep(2)

    page.keyboard.type("email@gmail.com")
    time.sleep(1)

    page.keyboard.press("Tab")
    time.sleep(1)

    page.keyboard.type("password")
    time.sleep(1)
