from app.services.playwright.pages.login_page import LoginPage
from app.services.playwright.core.settings import EMAIL, PASSWORD

async def do_login(page):
    login = LoginPage(page)
    await login.input_email(EMAIL)
    await login.input_password(PASSWORD)
    await login.click_login()
