from playwright.async_api import Page
from app.api.schema.customer_schema import Customer

class FinancialReportPage:
    def __init__(self, page: Page):
        self.page = page

    async def reload_page(self):
        await self.page.reload()

    async def click_group(self, group_name: str):
        await self.page.locator("div.v-list-item-title", has_text=group_name).click()

    async def click_item(self, item_name: str):
        item = self.page.locator("div.v-list-item-title", has_text=item_name)
        await item.wait_for(state="visible")
        await item.click()

    async def identification_input(self, identification_code: str):
        input_field = self.page.locator("div:has-text('CNPJ/CPF/Nome/Razão') input").first
        await input_field.wait_for(state="visible")
        await input_field.fill(identification_code)

    async def click_check_button(self):
        await self.page.locator("span:has-text('Consultar') >> ..").click()

    async def click_add_button(self):
        await self.page.locator(
            "i.fas.fa-plus-square.v-icon.notranslate.v-theme--light.v-icon--size-default.v-icon--clickable.cor-sistema--text"
        ).nth(-1).click()

    async def sale_details(self):
        card = self.page.locator("div.v-row:has-text('Detalhes da Venda')")
        await card.locator("i.fas.fa-info-circle").click()

    async def customer_data(self, customer: Customer):
        customer.name = await self.page.get_by_label("Cliente:").input_value()
        customer.cnpj = await self.page.get_by_label("CPF/CNPJ:").input_value()
        customer.soluti_request = await self.page.get_by_label("Solicitação Soluti:").input_value()
        customer.partner = await self.page.get_by_label("Parceiro:").input_value()
        customer.order_number = await self.page.get_by_label("Número Pedido:").input_value()

        await self.page.locator("span.v-btn__content", has_text="Dados Certificado").click()

        customer.cellphone = await self.page.get_by_label("Celular:").input_value()
        customer.email = await self.page.get_by_label("Email:").input_value()
        customer.cpf = await self.page.get_by_label("CPF Rep. Legal:").input_value()

        return customer