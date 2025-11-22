from app.services.playwright.actions.financial_report_actions import open_financial_report_page
from app.services.playwright.core.browser import start_browser
from app.services.playwright.actions.login_actions import do_login
from loguru import logger
from fastapi import HTTPException

class CustomerService:

    @staticmethod
    async def get_customer(identification_code: str):
        p, browser, context, page = await start_browser()

        try:
            logger.info(f"Starting customer search ID={identification_code}")

            await do_login(page)
            data = await open_financial_report_page(page, identification_code)

            if not data:
                logger.warning(f"No data found for the customer ID={identification_code}")
                raise HTTPException(
                    status_code=404,
                    detail="Customer data not found."
                )

            await page.wait_for_timeout(500)

            logger.success(f"Data found for the client ID={identification_code}")
            return data

        except Exception as e:
            logger.exception(f"Error when searching for customer ID={identification_code}")
            raise HTTPException(
                status_code=500,
                detail="Internal error while retrieving customer data."
            )

        finally:
            await browser.close()
            await p.stop()
            logger.info("Browser closed successfully.")
