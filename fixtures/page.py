import logging
import pytest
from playwright.sync_api import sync_playwright, Browser, BrowserContext, Page
import base64
import os
from data.environment import AUTH_STATE
from data import environment
from helpers.auth import Auth


def setup_logging():
    """Настройка логирования."""
    if not logging.root.handlers:  # Проверяем, не настроено ли логирование ранее
        logging.basicConfig(
            level=logging.DEBUG,  # Уровень логирования
            format='%(asctime)s - %(levelname)s - %(message)s',  # Формат вывода лога
            handlers=[logging.StreamHandler()]  # Выводим логи в консоль
        )
        logging.info("Логирование успешно настроено.")

def pytest_addoption(parser):
    """Пользовательские опции командной строки для управления браузером и headless режимом."""
    parser.addoption('--browser-name', action='store', default="chromium",
                     help="Choose browser: chromium, firefox, webkit")
    parser.addoption('--headless', action='store_true', help="Run tests in headless mode")
    parser.addoption('--slow_mo', action='store', default=0, type=int,
                     help='Delay (in milliseconds) between actions for easier debugging')
    parser.addoption('--viewport', action='store', default="1920,1080",
                     help="Set viewport size as width,height (default: 1920x1080)")
    parser.addoption('--timeout', action='store', default=30000, type=int,
                     help="Set default timeout for actions in milliseconds (default: 30s)")
    parser.addoption('--env', action='store', default="devtest6",
                     help="передаем окружение в парсер")


@pytest.fixture(scope="session")
def browser_context_args(request):
    """Фикстура для передачи аргументов при создании контекста браузера."""
    viewport = request.config.getoption('viewport').split(',')
    viewport_size = {'width': int(viewport[0]), 'height': int(viewport[1])}

    context_args = {
        'viewport': viewport_size,
        'locale': 'en-US',  # Можно заменить на 'ru-RU', если нужен русский
        'record_video_dir': None,  # Укажите путь для записи видео при необходимости
        'record_har_path': None,  # Укажите путь для записи сетевых запросов
    }
    return context_args


@pytest.fixture(scope="session")
def browser(request) -> Browser:
    """Фикстура для создания браузера с заданными параметрами."""
    browser_name = request.config.getoption("--browser-name")
    headless = request.config.getoption("--headless")
    slow_mo = request.config.getoption("--slow_mo")
    setup_logging()  # Гарантируем, что логирование настроено

    with sync_playwright() as playwright:
        if browser_name == 'firefox':
            browser = playwright.firefox.launch(headless=headless, slow_mo=slow_mo)
        elif browser_name == 'webkit':
            browser = playwright.webkit.launch(headless=headless, slow_mo=slow_mo)
        else:
            browser = playwright.chromium.launch(
                headless=headless,
                slow_mo=slow_mo,
                args=['--disable-gpu', '--no-sandbox', '--disable-dev-shm-usage']  # Аргументы для headless режима
            )
        yield browser
        browser.close()


@pytest.fixture(scope="session")
def context(browser: Browser, browser_context_args: dict) -> BrowserContext:
    """Фикстура для создания контекста браузера."""
    context = browser.new_context(**browser_context_args)
    context.set_default_timeout(browser_context_args.get('timeout', 30000))

    # Передаем авторизацию в заголовке на pre
    username = os.getenv('PLAYWRIGHT_USERNAME', 'test')
    password = os.getenv('PLAYWRIGHT_PASSWORD', 'tabletable')
    credentials = f"{username}:{password}"
    encoded_credentials = base64.b64encode(credentials.encode()).decode()
    context.set_extra_http_headers({
        "Authorization": f"Basic {encoded_credentials}"
    })

    yield context
    context.close()


@pytest.fixture(scope="function")
def page(context: BrowserContext) -> Page:
    """Фикстура для создания новой страницы (page) для каждого теста."""
    page = context.new_page()
    yield page
    page.close()


@pytest.fixture(scope="session")
def context_auth_group(browser: Browser):
    """Фикстура для создания контекста с авторизацией и использованием сохраненного состояния."""
    context = browser.new_context(
        http_credentials={"username": "test", "password": "tabletable"},
        ignore_https_errors=True
    )
    page = context.new_page()
    auth = Auth(page)
    auth.open_main()
    auth.check_modal_is_this_your_city()
    auth.open_model_auth_window()
    auth.authorization_process()
    auth.check_auth()
    context.storage_state(path=AUTH_STATE)
    print("Context created")
    page.close()
    yield context
    context.close()

@pytest.fixture(scope="session", autouse=True)
def set_environment(request):
    """Настраиваем глобальный объект host в зависимости от параметра --env."""
    env = request.config.getoption("--env") or "devtest"
    from data.environment import host
    host.env = env
    logging.info(f"[DEBUG] Current environment: {host.env}")