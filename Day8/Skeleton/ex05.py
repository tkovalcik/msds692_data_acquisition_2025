import asyncio
from playwright.async_api import async_playwright


async def scrape_page(url, p):
    browser = await p.chromium.launch(headless=False)
    page = await browser.new_page()
    await page.goto(url)
    title = await page.title()
    await browser.close()
    return title

async def main():
    async with async_playwright() as p:
        results = await asyncio.gather(scrape_page("https://reddit.com", p),
                             scrape_page("https://linkedin.com", p))
        print(results)

asyncio.run(main())