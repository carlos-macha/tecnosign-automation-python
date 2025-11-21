from app.api.schema.customer_schema import Customer
from app.services.playwright.actions.financial_report_actions import open_financial_report_page
from app.services.playwright.core.browser import start_browser
from app.services.playwright.actions.login_actions import do_login

class CustomerService:

    @staticmethod
    async def get_customer(identification_code: str):
        p, browser, context, page = await start_browser()

        try:
            await do_login(page)
            data = await open_financial_report_page(page, identification_code)

            await page.wait_for_timeout(500)

            return data

        finally:
            await browser.close()
            await p.stop()
