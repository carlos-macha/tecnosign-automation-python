from playwright.async_api import Page

class FinancialReportPage:
    def __init__(self, page: Page):
        self.page = page

    async def click_group(self, group_name: str):
        await self.page.locator("div.v-list-item-title", has_text=group_name).click()

    async def click_item(self, item_name: str):
        item = self.page.locator("div.v-list-item-title", has_text=item_name)
        await item.wait_for(state="visible")
        await item.click()