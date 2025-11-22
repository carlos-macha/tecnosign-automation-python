from playwright.async_api import async_playwright
from loguru import logger
from app.services.playwright.core.settings import BASE_URL

async def start_browser():
    try:
        logger.info(f"Starting Playwright and opening browser at {BASE_URL}")
        p = await async_playwright().start()
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto(BASE_URL)
        logger.success("Browser started and base URL opened successfully")
        return p, browser, context, page

    except Exception:
        logger.exception("Error while starting browser or opening base URL")

        try:
            await p.stop()
        except:
            pass
        raise
