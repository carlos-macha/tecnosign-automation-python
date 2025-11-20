from playwright.async_api import async_playwright
from app.services.playwright.core.settings import BASE_URL

async def start_browser():
    p = await async_playwright().start()
    browser = await p.chromium.launch(headless=False)
    context = await browser.new_context()
    page = await context.new_page()
    await page.goto(BASE_URL)  # <-- abre a URL base aqui
    return p, browser, context, page