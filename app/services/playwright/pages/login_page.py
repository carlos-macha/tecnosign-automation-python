from playwright.async_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    async def input_email(self, email: str):
        await self.page.get_by_placeholder("Email").fill(email)

    async def input_password(self, password: str):
        await self.page.get_by_placeholder("Senha").fill(password)

    async def click_login(self):
        await self.page.get_by_role("button", name="ENTRAR").click()
