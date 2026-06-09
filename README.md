# КТ №7. Удаленный запуск тестов через Selenium Grid

Учебный проект для практической работы **«КТ №7. Удаленный запуск (Grid)»**.

Проект демонстрирует удаленный запуск Selenium-тестов через **Selenium Grid** с использованием Python, Selenium WebDriver, Pytest и pytest-xdist. В качестве тестируемого сайта выбран **Wikipedia**, так как сайт доступен без регистрации, имеет понятную функциональность поиска и подходит для кросс-браузерного тестирования.

## Что входит в проект

```text
selenium_grid_KT7/
├── docs/
│   ├── KT7_report.docx
│   ├── KT7_report.pdf
│   ├── defect_reports.md
│   ├── grid_configuration.md
│   ├── test_cases.md
│   ├── test_plan.md
│   └── test_results.md
├── pages/
│   ├── base_page.py
│   └── wikipedia_page.py
├── tests/
│   └── test_wikipedia_grid.py
├── conftest.py
├── docker-compose.yml
├── pytest.ini
└── requirements.txt
```

## Выбранный сайт

**Сайт:** https://www.wikipedia.org/

**Причина выбора:**

- сайт не требует регистрации;
- есть понятная ключевая функция - поиск статей;
- можно проверить загрузку страницы, поиск, навигацию и элементы интерфейса;
- сайт подходит для запуска тестов в разных браузерах через Selenium Grid.

## Установка зависимостей

Создайте виртуальное окружение и установите зависимости:

```bash
python -m venv venv
source venv/bin/activate      # Linux / macOS
# venv\Scripts\activate       # Windows
pip install -r requirements.txt
```

## Запуск Selenium Grid через Docker

Для запуска Grid используется Docker Compose.

```bash
docker compose up -d
```

После запуска откройте интерфейс Grid:

```text
http://localhost:4444/ui
```

В интерфейсе должны отображаться доступные узлы Chrome и Firefox.

## Запуск тестов удаленно через Grid

Запуск только в Chrome:

```bash
pytest --browser chrome
```

Запуск только в Firefox:

```bash
pytest --browser firefox
```

Запуск в двух браузерах:

```bash
pytest --browser chrome,firefox
```

Параллельный запуск через pytest-xdist:

```bash
pytest -n 2 --browser chrome,firefox
```

## Переменная окружения для Grid URL

По умолчанию используется адрес:

```text
http://localhost:4444/wd/hub
```

Можно переопределить адрес:

```bash
export SELENIUM_GRID_URL=http://192.168.1.3:4444/wd/hub
pytest -n 2 --browser chrome,firefox
```

В Windows PowerShell:

```powershell
$env:SELENIUM_GRID_URL="http://192.168.1.3:4444/wd/hub"
pytest -n 2 --browser chrome,firefox
```

## Остановка Grid

```bash
docker compose down
```

## Что проверяют тесты

1. Открытие главной страницы Wikipedia через удаленный браузер.
2. Наличие основных элементов главной страницы.
3. Поиск статьи через поле поиска.
4. Проверка работы языковой навигации.
5. Параллельный запуск одного набора тестов в Chrome и Firefox.

## Примечание

Тесты не используют регистрацию, авторизацию, платежи или персональные данные. Все проверки выполняются на открытых страницах Wikipedia.
