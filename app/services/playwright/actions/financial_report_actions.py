from app.services.playwright.pages.financial_report_page import FinancialReportPage
from app.api.schema.customer_schema import Customer

async def open_financial_report_page(page, identification_code: str):
    customer = Customer()
    menu = FinancialReportPage(page)

    await menu.click_group("Relatorios")
    await menu.click_item("Financeiro")
    await menu.reload_page()
    await menu.click_group("Relatorios")
    await menu.click_item("Financeiro")

    await menu.identification_input(identification_code)
    await menu.click_check_button()

    await menu.click_add_button()
    await menu.sale_details()
    data = await menu.customer_data(customer)

    return data