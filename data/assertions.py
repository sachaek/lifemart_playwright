from playwright.sync_api import Page, Locator
from data.environment import host
from playwright.sync_api import expect
from pages.base import Base
from Locators.locator_data import LocatorData


class Assertions(Base):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

    def check_URL(self, uri, msg):
        def check_URL(self, uri, msg):
            # Ожидаемый URL и фактический URL без завершающего слэша
            expected_url = f"{host.get_base_url()}{uri}".rstrip('/')
            actual_url = self.page.url.rstrip('/')
            try:
                # Сравниваем URL без завершающих слэшей
                if expected_url != actual_url:
                    raise AssertionError(f"{msg}. Expected: {expected_url}, but got: {actual_url}")
                else:
                    print(f"Success: The URL is correct: {actual_url}")
            except AssertionError as e:
                # Обработка исключения с выводом фактического и ожидаемого URL
                raise AssertionError(str(e))

    def have_text(self, locator, text: str, msg): #элемент имеет текст
        loc = self.page.locator(locator.selector)
        expect(loc).to_have_text(text), msg


    def check_presence(self, locator, msg, timeout=12000, raw_selector=None):
        if not raw_selector:
            loc = self.page.locator(locator.selector)
        else:
            loc = self.page.locator(locator)
        expect(loc).to_be_visible(visible=True, timeout=timeout), msg

    def check_locator_visible(self, locator, msg, timeout=12000):
        """
        Функция проверяет видимость локатора
        локатор может быть экземпляром класса locatorData(),
        Locator (Playwright, например page.get_by_role(role="button", name="Пицца"): Locator)
        str - raw selector, например "div.bagube_2"
        """
        match locator:
            case str():
                loc = self.page.locator(locator)
            case LocatorData():
                loc = self.page.locator(locator.selector)
            case Locator():
                loc = locator
            case _:
                raise TypeError("Некорректный тип локатора, ожидается str|LocatorData| ")

        expect(loc).to_be_visible(visible=True, timeout=timeout), msg



    def check_absence(self, locator, msg):
        loc = self.page.locator(locator.selector)
        expect(loc).to_be_hidden(timeout=700), msg


    def check_equals(self, actual, expected, msg):
        assert actual == expected, msg


    def check_is_less_then(self, first, second, msg):
        assert first < second, msg


    def button_is_disabled(self, locator: LocatorData) -> bool:
        button = self.page.query_selector(locator.selector)
        return button.is_disabled()


    def check_url_content(self, uri,msg):
        assert f"{uri}" in self.page.url, msg


    def check_box_activated(self, locator, msg): #проверка что чек бокс поставлен
        loc = self.page.locator(locator.selector)
        expect(loc).to_be_checked(), msg


    def element_disabled(self, locator, msg): #веб элемент отключен
        loc = self.page.locator(locator.selector)
        expect(loc).to_be_disabled(), msg


    def to_be_editable(self, locator, msg): #возможно редактировать
        loc = self.page.locator(locator.selector)
        expect(loc).to_be_editable(), msg


    def to_be_empty(self, locator, msg): #web element пустой
        loc = self.page.locator(locator.selctor)
        expect(loc).to_be_empty(), msg


    def contain_text(self, locator, text: str, msg): #элемент содержит текст
        loc = self.page.locator(locator.selector)
        expect(loc).to_contain_text(text), msg


    def select_have_values(self, locator, options: list, msg): #Select имеет опции для выбора (опция передается аргументом к проверке)
        loc = self.page.locator(locator.selector)
        loc.select_option(options)
        expect(loc).to_have_values(options), msg