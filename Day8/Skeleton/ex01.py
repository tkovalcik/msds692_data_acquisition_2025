from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
# Step 1. Create a browser
# Can use chromium/firefox/webkit
    browser = p.chromium.launch(headless=False)

# Step 2. Create a new BrowserContext
    context = browser.new_context()
    page = context.new_page()
    # time.sleep(1)

# Step 3. Open a page
    page.goto("https://reddit.com")
    # time.sleep(1)

    # page.wait_for_selector("summary")
    # page.wait_for_selector("#grecaptcha-badge")
    page.wait_for_selector("main")
    page.query_selector_all("a")

    for anchor in page.query_selector_all("a"):
        # print(anchor.inner_html())
        print(anchor.get_attribute("href"))

    # time.sleep(2)

    # print(page.title())

    browser.close()
