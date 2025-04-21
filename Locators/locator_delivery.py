from Locators.locator_data import LocatorData

class Delivery:
    header_button_delivery = LocatorData(
        selector='.city-address',
        description="Открываем окно доставки через хеддер",
        click=True,
        nth= 0
    )

    modal_delivery = LocatorData(
        selector='.modal.default-scroll.DeliveryMap',
        description='Модалка выбора адреса и типа доставки',
    )

    modal_delivery_button = LocatorData(
        selector='.address-types > .address-types__button:has-text("Доставка")',
        description="Выбираем доставку через в модальном окне",
        click=True,
        nth=0
    )
    modal_hall_button = LocatorData(
        selector='.address-types > .address-types__button:has-text("Зал")',
        description="Выбираем зал в модальном окне",
        click=True,
        nth=0
    )
    modal_self_order_button = LocatorData(
        selector='.address-types > .address-types__button:has-text("Самовывоз")',
        description="Выбираем самовывоз в модальном окне",
        click=True,
        nth=0
    )

    modal_input = LocatorData(
        selector='.address__input input[placeholder="Введите адрес"]',
        description= 'Ввод адреса в модальном окне',
        input = True
    )

    list_address = LocatorData(
        selector='.address-autocomplete',
        description='Получение списка адресов'
    )

    modal_button_ok= LocatorData(
        selector='.address__input-wrapper-ok',
        description='Кнопка ок в модалке доставки',
        click=True
    )

    header_address = LocatorData(
        selector='.with-address__address',
        description ='Выбранный адрес в хеддере сайта'

    )

    sauce_locator = LocatorData(
        selector= """#category_id-66 > .products > div:nth-child(2) > .product > .product-info > .product-info__bottom-line > .product-info__bottom-line-center > .product-action-wrap > .product-action""",
        description = "button of second sauce"
    )

    modal_window = LocatorData(
        selector="div.map__map-content",
        description = "Модальное окно выбора адреса"
    )

    button_of_type_delivery_active = LocatorData(
        selector="button.address-types__button.active",
        description="""Модальное окно выбора адреса:: АКТИВНАЯ кнопка типа доставки
        Пример Использования button_of_type_delivery.text_content() == 'Зал' or 'Доставка'"""
    )

    autocomplete_street = LocatorData(
        selector="div.address-autocomplete__street",
        description="Локатор указывающий на блок с автоподстановкой адреса"
    )

    header_type_delivery_and_time = LocatorData(
        selector="p.with-address__type",
        description="Локатор хеддера, содержит инфу о типе доставки и времени, например Зал ~ 15 минут"
    )