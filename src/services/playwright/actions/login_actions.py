from src.services.playwright.pages.login_page import LoginPage
from src.services.playwright.core.settings import EMAIL, PASSWORD

def do_login(page):
    login = LoginPage(page)
    login.input_email(EMAIL)
    login.input_password(PASSWORD)
    login.click_login()