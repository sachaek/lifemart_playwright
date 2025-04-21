import playwright.sync_api

from Locators.locator_data import LocatorData


class Order(LocatorData):
    catalog_navigate_category = LocatorData(
        selector=".categories__link-span:has-text('Дополнительно')",
        description='Переходим к категории дополнительно',
        click=True
    )
    add_product = LocatorData(
        selector='.product-action.primary',
        description='Нажимаем на первую кнопку добавления товара по индексу',
        click=True,
        nth=0
    )

    open_product_card = LocatorData(
        selector='a[aria-label="Открыть карточку блюда Фантастическая четвёрка"]',
        description='Открываем карточку блюда',
        click=True,
        nth=0
    )

    add_additional_modifier = LocatorData(
        selector='button.additionally__actions_btn.ghost.loader_gradient',
        description='Нажимаем на добавление модификатора',
        click=True,
        nth=0
    )

    add_cheese_board = LocatorData(
        selector='button[class="left-picture__btn"]:has-text("Сырный")',
        description='Нажимаем на добавление сырного борта',
        click=True
    )

    button_exclude_ingredient = LocatorData(
        selector='a[class="product-comments__comment"]:has-text("Без грибов")',
        description='Исключаем ингредиент',
        click=True
    )

    add_product_from_card = LocatorData(
        selector='button.product-action.primary.loader_gradient > p.product-action__add-block > span.product-action__add-price > span.product-action__add:has-text("1 085 ₽")',
        description='Добавляем блюдо из карточки',
        click=True
    )

    navigate_busket = LocatorData(
        selector='.cart__link > .cart__svg-wrap',
        description='Кнопка перехода в корзину',
        click=True
    )

    details_order_button = LocatorData(
        selector='.totals-nav__btn.primary.loader_circle',
        description='Нажатие на кнопку переход к заказам',
        click=True
    )

    cash_order_button = LocatorData(
        selector='.payment-button__name.cash',
        description='Выбираем оплату наличкой',
        click=True
    )

    change_order_button = LocatorData(
        selector='.payments-change__button:has-text("5000")',
        description='Выбираем сдачу с 500 рублей',
        click=True
    )

    email_order_input = LocatorData(
        selector='input.input-form__input',
        description='Поле ввода e-mail для отправки чека',
        input=True
    )

    modal_product = LocatorData(
        selector='div.modal-element',
        description='Модальное окно с выбором продукции'
    )

    modal_product_button_cancel = LocatorData(
        selector='button.forgotten-products__no.secondary.loader_gradient',
        description='Нажимаем на кнопку "Не нужны приборы и соусы"',
        click=True
    )

    promocode_input = LocatorData(
        selector='input.input-form__input.input-form__input-promo',
        description='Окно для ввода промокода',
        input=True
    )

    button_apply_promo = LocatorData(
        selector='button.input-form__submit.primary.loader_gradient',
        description='Кнопка для применения промокода',
        click=True
    )

    promoevents = LocatorData(
        selector='span.promoevents__text',
        description='Примененная акция'
    )

    add_product_dop = LocatorData(
        selector='.add-products__inc-dish.plus.ghost.loader_gradient',
        description='Нажимаем на кнопки добавления доп продукции'
    )

    button_not_apartment = LocatorData(
        selector="#header >> role=button",
        description="Корзина::тип заказа доставка::" \
                    "Редактирование адреса в модальном окне, кнопка 'частный дом'",
    )

    cart_auth_number_placeholder = LocatorData(
        selector="+7 (999) 999-99-",
        description="Плейсхолдер инпут номера телефона - авторизация в корзине"
    )

    sriracha_sauce = LocatorData(
        selector="div[class='product js-product_id-14555'] > div[class='product-info'] > div[class='product-info__bottom-line']",
        description="Кнопка ценника соуса шрирача"
    )