from app.services.playwright.pages.login_page import LoginPage
from app.services.playwright.core.settings import EMAIL, PASSWORD
from loguru import logger

async def do_login(page):
    login = LoginPage(page)
    try:
        logger.info("Starting login process")
        await login.input_email(EMAIL)
        await login.input_password(PASSWORD)
        await login.click_login()
        logger.success("Login completed successfully")
    except Exception:
        logger.exception("Error during login process")
        raise
