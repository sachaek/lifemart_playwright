import os


class Environment:
    PRE = 'pre'
    PROD = 'prod'
    DEVTEST1 = 'devtest1'
    DEVTEST2 = 'devtest2'
    DEVTEST3 = 'devtest3'
    DEVTEST4 = 'devtest4'
    DEVTEST5 = 'devtest5'
    DEVTEST6 = 'devtest6'
    DEVTEST7 = 'devtest7'
    DEV = 'dev'

    URLS = {
        PRE: 'https://www-devtest6.lifemart.ru/',
        DEVTEST7: 'https://www-devtest7.lifemart.ru/',
        DEVTEST6: 'https://www-devtest6.lifemart.ru/',
        DEVTEST5: 'https://www-devtest5.lifemart.ru/',
        DEVTEST4: 'https://www-devtest4.lifemart.ru/',
        DEVTEST3: 'https://www-devtest3.lifemart.ru/',
        DEVTEST2: 'https://www-devtest2.lifemart.ru/',
        DEVTEST1: 'https://www-devtest1.lifemart.ru/',
        PROD: 'https://www.lifemart.ru/',
        DEV: 'https://www.lifemart.ru/'
    }

    def __init__(self, env: str|None = None):
        self.env = env or self.PRE


    def get_base_url(self):
        if self.env in self.URLS:
            return self.URLS[self.env]
        else:
            raise Exception(f"Unknown value of ENV variable {self.env}")

    def get_base_url_api(self):
        match self.env:
            case env if env.startswith("devtest") and env[7:].isdigit() and 1 <= int(env[7:]) <= 7:
                return  f"https://{self.env}.lifemart.ru/"
            case "pre" | "shot":
                return f'https://www-devtest6.lifemart.ru/'
            case "prod":
                return f'https://www.lifemart.ru/'
            case _:
                raise ValueError(f"Environment error: sent {self.env}")


host = Environment()


def get_project_path():
    # Получаем абсолютный путь к текущему скрипту
    script_path = os.path.abspath(__file__)

    # Получаем путь к директории, в которой находится скрипт
    data_path = os.path.dirname(script_path)
    project_path = os.path.dirname(data_path)
    return data_path, project_path


PROJECT_PATH = get_project_path()[1]
DATA_PATH = get_project_path()[0]

# переменная которая ссылается на AUTH_PATH/auth_state.json
AUTH_STATE = os.path.join(DATA_PATH, 'auth_state.json')


if __name__ == "__main__":
    print(f"project path {PROJECT_PATH} \nauth_path: {DATA_PATH}\nauth context: {AUTH_STATE}")
