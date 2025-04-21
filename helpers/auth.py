import time

from playwright.sync_api import expect

from pages.base import Base


class Auth(Base):
    def __init__(self, page):
        super().__init__(page)

    def open_main(self):
        self.open("ru/ekaterinburg")

    def check_modal_is_this_your_city(self):
        expect(self.page.locator("div").filter(has_text="Ваш город — Екатеринбург? ДаНет").nth(3)).to_be_visible(
            timeout=10000)

    def open_model_auth_window(self):
        self.page.get_by_role("button", name="Да").click()
        self.page.get_by_role("button", name="Навигация").click()
        self.page.get_by_role("link", name="go to profile").click()

    def authorization_process(self):
        self.page.get_by_role("textbox", name="+7 (9xx) xxx-xx-xx").fill("+7 (999) 999-99-99")
        self.page.get_by_role("button", name="По звонку").click()
        self.page.get_by_role("button", name="Подтвердить").click()
        self.page.get_by_role("textbox", name="• • • •").click()
        self.page.get_by_role("textbox", name="• • • •").fill("5917")

        time.sleep(5)
        self.page.get_by_role("button", name="Навигация").click(force=True, click_count=2)

    def check_auth(self):
        expect(self.page.get_by_role("link", name="go to profile")).to_be_visible()