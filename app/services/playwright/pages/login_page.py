from playwright.async_api import Page
from loguru import logger

class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    async def input_email(self, email: str):
        try:
            logger.info(f"Filling email field with: {email}")
            await self.page.get_by_placeholder("Email").fill(email)
            logger.success("Email field filled successfully")
        except Exception:
            logger.exception("Error while filling email field")
            raise

    async def input_password(self, password: str):
        try:
            logger.info("Filling password field")
            await self.page.get_by_placeholder("Senha").fill(password)
            logger.success("Password field filled successfully")
        except Exception:
            logger.exception("Error while filling password field")
            raise

    async def click_login(self):
        try:
            logger.info("Clicking 'ENTRAR' button")
            await self.page.get_by_role("button", name="ENTRAR").click()
            logger.success("'ENTRAR' button clicked successfully")
        except Exception:
            logger.exception("Error while clicking 'ENTRAR' button")
            raise
