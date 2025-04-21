from playwright.sync_api import Page, expect

from pages.base import Base


class Delivery(Base):
    def __init__(self, page: Page):
        super().__init__(page)

    def open_main_page(self):
        self.open("ru/ekaterinburg")
        self.page.get_by_role("button", name="Да").click()

    def modal_to_select_address(self):
        expect(self.page.get_by_label("choose city")).to_contain_text("Екатеринбург")
        self.page.get_by_role("button", name="Выберите адрес").click()

    def confirm_address(self):
        self.page.get_by_role("textbox", name="Улица, дом").click()
        self.page.get_by_role("textbox", name="Улица, дом").fill("Хохрякова 74")
        self.page.get_by_role("link", name="улица Хохрякова,").click()
        self.page.get_by_role("button", name="Ок", exact=True).click()

    def check_address(self):
        expect(self.page.locator("#header")).to_be_visible()
        expect(self.page.locator("#header")).to_contain_text("улица Хохрякова, 74")