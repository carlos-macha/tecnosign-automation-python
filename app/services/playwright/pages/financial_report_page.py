from playwright.async_api import Page
from loguru import logger
from app.api.schema.customer_schema import Customer

class FinancialReportPage:
    def __init__(self, page: Page):
        self.page = page

    async def reload_page(self):
        try:
            logger.info("Reloading the page")
            await self.page.reload()
            logger.success("Page reloaded successfully")
        except Exception:
            logger.exception("Error while reloading the page")
            raise

    async def click_group(self, group_name: str):
        try:
            logger.info(f"Clicking on group: {group_name}")
            await self.page.locator("div.v-list-item-title", has_text=group_name).click()
            logger.success(f"Group '{group_name}' clicked successfully")
        except Exception:
            logger.exception(f"Error while clicking on group: {group_name}")
            raise

    async def click_item(self, item_name: str):
        try:
            logger.info(f"Clicking on item: {item_name}")
            item = self.page.locator("div.v-list-item-title", has_text=item_name)
            await item.wait_for(state="visible")
            await item.click()
            logger.success(f"Item '{item_name}' clicked successfully")
        except Exception:
            logger.exception(f"Error while clicking on item: {item_name}")
            raise

    async def identification_input(self, identification_code: str):
        try:
            logger.info(f"Filling identification field with: {identification_code}")
            input_field = self.page.locator("div:has-text('CNPJ/CPF/Nome/Razão') input").first
            await input_field.wait_for(state="visible")
            await input_field.fill(identification_code)
            logger.success(f"Identification field filled with: {identification_code}")
        except Exception:
            logger.exception(f"Error while filling identification field: {identification_code}")
            raise

    async def click_check_button(self):
        try:
            logger.info("Clicking 'Check' button")
            await self.page.locator("span:has-text('Consultar') >> ..").click()
            logger.success("'Check' button clicked successfully")
        except Exception:
            logger.exception("Error while clicking 'Check' button")
            raise

    async def click_add_button(self):
        try:
            logger.info("Clicking 'Add' button")
            await self.page.locator(
                "i.fas.fa-plus-square.v-icon.notranslate.v-theme--light.v-icon--size-default.v-icon--clickable.cor-sistema--text"
            ).nth(-1).click()
            logger.success("'Add' button clicked successfully")
        except Exception:
            logger.exception("Error while clicking 'Add' button")
            raise

    async def sale_details(self):
        try:
            logger.info("Opening sale details")
            card = self.page.locator("div.v-row:has-text('Detalhes da Venda')")
            await card.locator("i.fas.fa-info-circle").click()
            logger.success("Sale details opened successfully")
        except Exception:
            logger.exception("Error while opening sale details")
            raise

    async def customer_data(self):
        try:
            logger.info("Starting to capture customer data")

            name = await self.page.get_by_label("Cliente:").input_value()
            cnpj = await self.page.get_by_label("CPF/CNPJ:").input_value()
            soluti_request = await self.page.get_by_label("Solicitação Soluti:").input_value()
            partner = await self.page.get_by_label("Parceiro:").input_value()
            order_number = await self.page.get_by_label("Número Pedido:").input_value()

            await self.page.locator("span.v-btn__content", has_text="Dados Certificado").click()

            cellphone = await self.page.get_by_label("Celular:").input_value()
            email = await self.page.get_by_label("Email:").input_value()
            cpf = await self.page.get_by_label("CPF Rep. Legal:").input_value()

            logger.success("Customer data captured successfully")
            return Customer(
                name=name,
                email=email,
                cpf=cpf,
                cnpj=cnpj,
                soluti_request=soluti_request,
                cellphone=cellphone,
                order_number=order_number,
                partner=partner
            )

        except Exception:
            logger.exception("Error while capturing customer data")
            raise
