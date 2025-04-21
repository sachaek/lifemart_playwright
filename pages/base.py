import re

from playwright.sync_api import Page, TimeoutError, Response, expect, Locator
from data.environment import host
from Locators.locator_data import LocatorData
import base64


class Base:
    def __init__(self, page: Page):
        self.page = page
        self.base_url = host.get_base_url()

    def open(self, uri) -> Response | None:
        return self.page.goto(f"{self.base_url}{uri}", wait_until='domcontentloaded')

    def click(self, locator: LocatorData) -> None:  # клик, при необходимости сам делает скролл к нужному элементу
        self.page.click(locator.selector)

    def input(self, locator: LocatorData, data: str) -> None:  # ввод в поле
        self.page.locator(locator.selector).fill(data)

    def get_text(self, locator: LocatorData,
                 index: int,
                 timeout: int = None) -> str:  # достаем текст, если локатор один, то в аргумент прокидываем значение 0
        return self.page.locator(locator.selector).nth(index).text_content(timeout=timeout)

    def click_element_by_index(self, locator: LocatorData, index: int) -> None:  # находим элемент по индексу и кликаем
        self.page.locator(locator.selector).nth(index).click()

    def input_value_by_index(self, locator: LocatorData, index: int,
                             data: str) -> None:  # вводим данные в нужные поля по индексу
        self.page.locator(locator.selector).nth(index).fill(data)

    def wait_for_element(self, locator, timeout=12000) -> None:  # ожидание какого то элемента если нужно
        self.page.wait_for_selector(locator, timeout=timeout)

    def wait_for_all_elements(self, locator, timeout=5000):  # ожидание всех элементов
        elements = self.page.query_selector_all(locator)

        for element in elements:
            self.page.wait_for_selector(locator, timeout=timeout)

        return elements

    def current_url(self) -> str:  # возвращает урл
        return self.page.url

    def checkbox_by_index(self, locator: LocatorData, index: int):  # находим чекбокс по инкдексу и кликаем
        elements = self.page.query_selector_all(locator)
        # Проверка наличия элемента с указанным индексом
        if 0 <= index < len(elements):
            # Поставить чек-бокс по элементу с указанным индексом
            elements[index].check()
        else:
            print(f"Элемент с индексом {index} не найден.")

    def click_first_element(self,
                            locator: LocatorData):  # кликаем по первому элементу, если по индексу выдает out of range
        self.page.locator(locator.selector).first.click()

    def click_by_text(self, text: str):  # находим элемент(кнопку)с нужным текстом внутри и кликаем
        self.page.get_by_text(text).click()

    def input_in_shadow_root(self, shadow_locator: LocatorData, shadow_input_locator: LocatorData, data: str):
        # ищем элемент в шадоуруте
        shadow_root = self.page.evaluate_handle(f'document.querySelector("{shadow_locator}").shadowRoot')
        input_element = shadow_root.evaluate_handle(f'document.querySelector("{shadow_input_locator}")')
        input_element.as_element().fill(data)

    def checkbox(self, locator: LocatorData) -> None:  # проверяем является ли элемент чек-боксом и проставляем чекбокс
        self.page.locator(locator.selector).check()

    def is_element_present(self, locator: LocatorData) -> bool:  # если элемент есть то все ок
        try:
            self.page.wait_for_selector(locator.selector, timeout=10000)
        except TimeoutError as e:
            return False
        return True

    def is_element_NOT_presence(self, locator: LocatorData) -> bool:  # если элемента нет, то все ок
        try:
            self.page.wait_for_selector(locator.selector, timeout=5000)
        except TimeoutError as e:
            return True
        return False

    def selector(self, locator: LocatorData, value: str):  # выпадающи список, выбираем значение в валуе
        self.page.select_option(locator.selector, value)

    def drag_and_drop(self, source, target):  # перетаскивать из-куда то
        self.page.drag_and_drop(source, target)

    def alert_accept(self,
                     locator: LocatorData):  # сначала идет слушатель, который говорит, что нужно сделать с алертом
        self.page.on('dialog', lambda dialog: dialog.accept())  # анонимная функция обрабатывающая событие
        self.click(locator)

    def open_new_tab_and_check_presence(self, locclick,
                                        locpresence):  # ожидаем открытие нового таба и свитчаемся и делаем ассерт, что нужный элемент есть на странице
        with self.page.expect_popup() as page1_info:
            self.page.click(locclick)
        page1 = page1_info.value
        page1.bring_to_front()
        loc = page1.locator(locpresence)
        expect(loc).to_be_visible(visible=True, timeout=12000)

    def close_tab(self, number):  # закрываем таб и возвращаемся на предыщущий, number-номер таба который хотим закрыть
        all_tabs = self.page.context.pages
        all_tabs[number].close()

    def switch_to_previous_tab(self,
                               number):  # number - номер вкладки на которую хотим свичнуться, сначала используем этот метод, потом закрываем вкладки
        all_tabs = self.page.context.pages  # Получаем список всех вкладок в контексте браузера
        new_tab = all_tabs[number]  # Получаем вкладку по указанному индексу
        self.page.bring_to_front()  # Переключаемся на текущую вкладку (делаем ее активной)
        self.page.wait_for_load_state()  # Ожидаем завершения загрузки страницы в текущей вкладке
        return new_tab

    def close_all_tabs_except_first(self):  # закрываем все табы, кроме первогоо
        all_tabs = self.page.context.pages
        for p in range(1, len(all_tabs)):
            all_tabs[p].close()

    def refresh(self) -> Response | None:  # рефреш страницы
        return self.page.reload(wait_until='domcontentloaded')

    def alert_with_double_input(self, key1, value1, key2, value2):
        # ключ значения нужно вводить в кавычках,в ключ указывать название поля, а в значение что хотим ввести
        dialog = self.page.wait_for_event('dialog')
        inputs = {key1: value1, key2: value2}
        dialog.fill(inputs)
        dialog.accept()

    def press_from_keyboard(self, code: str):
        for number in code:
            self.page.keyboard.press(number)

            # Функция принимает на вход locator из LocatorData
            # Проверяет видимость элемента, при видимости возвращает true
            # Нужно передать время для тайм-аута ожидания

    def visible_locator(self, loc, timeout=10000):
        test = expect(self.page.locator(loc)).to_be_visible(timeout=timeout)
        test.print(test)
        return expect(self.page.locator(loc)).to_be_visible(timeout=timeout)

    def click_button_by_name(self, name: str, visible: bool = False, vis_timeout: int = 1000,
                             allow_expect: bool = False, force: bool = False,
                             click_count: int = 1, delay_click: int = None):
        button = self.page.get_by_role("button", name=name)
        if visible:
            button.wait_for(state="visible", timeout=vis_timeout)
        elif allow_expect:
            expect(button).not_to_have_attribute("disabled", value=re.compile(".*"), timeout=3000)
        button.click(trial=True)
        button.click(force=force, click_count=click_count, delay=delay_click)

    def click_button_by_locator(self, locator: str | LocatorData | Locator,
                                visible: bool = False, vis_timeout: int = 1000,
                                allow_expect: bool = False, force: bool = False,
                                click_count: int = 1, delay_click: int = None):

        if isinstance(locator, str):
            button = self.page.locator(locator)
        elif isinstance(locator, LocatorData):
            button = self.page.locator(locator.selector)
        elif isinstance(locator, Locator):
            button = locator
        else:
            raise AssertionError("Wrong type of locator, expected str, locator data or LocatorPlaywright")

        if visible:
            button.wait_for(state="visible", timeout=vis_timeout)
        elif allow_expect:
            expect(button).not_to_have_attribute("disabled", value=re.compile(".*"), timeout=3000)
        button.click(trial=True)
        button.click(force=force, click_count=click_count, delay=delay_click)

    def click_button_by_name_slow(self, name, click_count=1, vis_timeout=6000):
        self.click_button_by_name(name=name, visible=True, vis_timeout=vis_timeout,
                                  allow_expect=True, force=True,
                                  click_count=click_count, delay_click=200)

    def click_button_by_locator_slow(self, locator, click_count=1):
        self.click_button_by_locator(locator=locator, visible=True, vis_timeout=6000,
                                     allow_expect=True, force=True,
                                     click_count=click_count, delay_click=200)
