class LoginPage:

    def __init__(self, page):
        self.page = page
        self.frame = page.frame_locator("iframe").first

    def input_email(self, email):
        self.page.get_by_placeholder("Email").fill(email)

    def input_password(self, password):
        self.page.get_by_placeholder("Senha").fill(password)

    def click_login(self):
        self.page.get_by_role("button", name="ENTRAR").click()
