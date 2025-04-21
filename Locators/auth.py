from Locators.locator_data import LocatorData

class Auth:
    select_city_click  = LocatorData(
        selector='text="Да"',
        description="Согласиться с выбранным городом в попапе",
        click=True
    )

    close_map_click = LocatorData(
        selector='.map__close',
        description="Закрытие карты",
        click=True
    )

    auth_click = LocatorData(
        selector='.no-auth',
        description='Кнопка авторизации для десктопной версии браузера',
        click=True
    )

    input_number_auth_click = LocatorData(
        selector='label=Телефон',
        description="Поле ввода номера телефона",
        click=True
    )

    # input_number_auth_fill = LocatorData(
    #     selector='label=Телефон',
    #     description="Поле ввода номера телефона",
    #     input=True
    # )

    input_number_auth_fill = LocatorData(
        selector='input.input-form__input',
        description="Поле ввода номера телефона",
        input=True
    )

    button_set_auth_click = LocatorData(
        selector='button.login__send-button',
        description="Кнопка подтверждения данных и отправки кода",
        click=True
    )

    input_code = LocatorData(
        selector='.inputOtp',
        description="Поле ввода кода для авторизации",
        click=True,
        nth=0
    )

    select_call_click = LocatorData(
        selector="role=button[name='По звонку']",
        description="Выбор звонка для авторизации",
        click=True
    )

    select_yes_city = LocatorData(
        selector="role=button[name='Да']",
        description="Нажимаем да при уточнении города",
        click=True
    )

    choose_sms_au = LocatorData(
        selector="role=button[name='СМС']",
        description="Выбираем авторизацию по смс",
        click=True
    )

    send_accept = LocatorData(
        selector="role=button[name=' Отправить подтверждение ']",
        description="Подтверждаем авторизацию по номеру телефона",
        click=True
    )

    resend_code = LocatorData(
        selector="role=button[name=' Позвонить повторно ']",
        description="Снова высылаем код подтверждения",
        click=True
    )

    auth_acceptation = LocatorData(
        selector="div.auth-user",
        description="Локатор авторизованного пользователя, иконка в шапке справа",
        click=True
    )

    input_code_auth_area = LocatorData(
        selector="input.inputOtp",
        description="первое поле (1/4) для ввода смс кода"
    )

    button_go_auth = LocatorData(
        selector="div.no-auth",
        description="Кнопка для авторизации"
    )

    button_go_bonus_card_from_header = LocatorData(
        selector="div.auth-user__bonus",
        description="Кнопка перехода на страницу бонусной карты из шапки"
    )