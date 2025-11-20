from app.services.playwright.pages.financial_report_page import FinancialReportPage

async def open_financial_report_page(page):
    menu = FinancialReportPage(page)
    await menu.click_group("Relatorios")
    await menu.click_item("Financeiro")