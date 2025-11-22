from app.services.playwright.pages.financial_report_page import FinancialReportPage
from loguru import logger

async def open_financial_report_page(page, identification_code: str):
    menu = FinancialReportPage(page)

    try:
        logger.info(f"Opening financial report for customer ID: {identification_code}")

        await menu.click_group("Relatorios")
        await menu.click_item("Financeiro")
        await menu.reload_page()
        await menu.click_group("Relatorios")
        await menu.click_item("Financeiro")

        await menu.identification_input(identification_code)
        await menu.click_check_button()

        await menu.click_add_button()
        await menu.sale_details()
        data = await menu.customer_data()

        logger.success(f"Financial report retrieved successfully for customer ID: {identification_code}")
        return data

    except Exception:
        logger.exception(f"Error while opening financial report for customer ID: {identification_code}")
        raise
