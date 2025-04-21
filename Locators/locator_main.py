from Locators.locator_data import LocatorData

class Main:
    city_select_first_step_button = LocatorData(
        selector=".city-select-first-step__button.city-select-first-step__button-yes.primary.loader_gradient",
        description="Подтверждаем, что город верный",
        click=True,
        nth=0
    )

    address_input = LocatorData(
        selector="input[placeholder=\"Введите адрес\"]",
        description="Строка ввода адреса",
        click=True,
        input=True
    )

    address_option = LocatorData(
        selector="span:has-text('улица Хохрякова')",
        description="Адрес",
        click=True,
        nth=0
    )

    delivery_title = LocatorData(
        selector="div.icon-delivery__title",
        description="Время доставки"
    )

    ok_button = LocatorData(
        selector="button.address__input-wrapper-ok",
        description="Подтверждаем адрес",
        click=True
    )

    delivery_address = LocatorData(
        selector="span.address",
        description="Адрес"
    )

    product = LocatorData(
        selector="span:has-text('Сет 6 роллов 8 вкусов')",
        description="Товар в каталоге"
    )

    cart_button = LocatorData(
        selector="a.cart__link",
        description="Корзина в правом верхнем углу"
    )

    cart_order = LocatorData(
        selector="button.cart-preview__btn-go.primary.loader_gradient",
        description="Оформить заказ",
        click=True
    )

    cart_number_input = LocatorData(
        selector="input.input-form__input[placeholder=\"+7 (999) 999-99-99\"]",
        description="Поле ввода телефона",
        click=True,
        nth=0
    )

    cart_promo_input = LocatorData(
        selector="input.input-form__input.input-form__input-promo",
        description="Поле ввода промокода",
        click=True
    )

    input_valid = LocatorData(
        selector="input.input-form__input.visible.valid",
        description="Поле заполнено корректно"
    )

    order_details_button = LocatorData(
        selector="button.totals-nav__btn.primary.loader_circle:has-text('К деталям заказа')",
        description="Открыть детали заказа"
    )

    modifier_add_button = LocatorData(
        selector="button.add-products__inc-dish.plus.ghost.loader_gradient",
        description="Добавляем доп",
        nth=0
    )

    modifier_accept_button = LocatorData(
        selector="button.forgotten-products__add.primary.loader_gradient",
        description="Подтверждаем выбор допов",
        click=True
    )

    payment_type_cash_button = LocatorData(
        selector="button.payment-button.col.disabled > span.payment-button__name.cash",
        description="Оплата наличными",
        click=True
    )

    payment_no_change = LocatorData(
        selector="button.payments-change__button.payments-change__button_no.payments-change__button_active",
        description="Без сдачи",
        click=True
    )
    
    create_order_button = LocatorData(
        selector="button.totals-nav__btn.primary.loader_circle:has-text('Оформить заказ')",
        description="Оформить заказ",
        click=True
    )

    private_house_toggle = LocatorData(
        selector=".address-type > button.toggle-default.dark",
        description="Тоггл частного дома",
        click=True
    )

    save_address_button = LocatorData(
        selector="span:has-text(' Сохранить ')",
        description="Сохраняем адрес доставки",
        click=True
    )

    confirm_by_call_button = LocatorData(
        selector=".external-confirm__buttons.external-confirm__buttons_thee-btn > button.call.external-confirm__button",
        description="Подтверждение по звонку",
        click=True
    )

    login_button = LocatorData(
        selector=".login__form-container > button.login__send-button.primary.loader_gradient",
        description="Подтвердить заказ",
        click=True
    )

    outside_delivery_address = LocatorData(
        selector=f"text={'Адрес вне зоны доставки'}",
        description="Информационное сообщение 'Адрес вне зоны доставки'"
    )

    delivery_address_in_map = LocatorData(
        selector=f"text={'Доставка от 455 ₽'}",
        description="Информационное сообщение о стоимости адреса доставки на карте"
    )