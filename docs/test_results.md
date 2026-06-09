# Отчет о результатах тестирования

## Сводка

| Показатель | Значение |
|---|---:|
| Количество тест-кейсов | 7 |
| Пройдено | 7 |
| Не пройдено | 0 |
| Заблокировано | 0 |
| Браузеры | Chrome, Firefox |
| Инструменты | Selenium Grid, Pytest, pytest-xdist, Docker |

## Проверенная конфигурация

| Параметр | Значение |
|---|---|
| ОС тестировщика | Windows / Linux |
| Grid URL | http://localhost:4444/wd/hub |
| Hub UI | http://localhost:4444/ui |
| Браузерные узлы | Chrome Node, Firefox Node |
| Тестируемый сайт | https://www.wikipedia.org/ |

## Команды запуска

```bash
docker compose up -d
pytest -n 2 --browser chrome,firefox
```

## Результаты

| ID | Тест | Chrome | Firefox | Итог |
|---|---|---|---|---|
| TC-001 | Открытие главной страницы | Passed | Passed | Passed |
| TC-002 | Проверка поля поиска | Passed | Passed | Passed |
| TC-003 | Поиск статьи | Passed | Passed | Passed |
| TC-004 | Проверка языковой навигации | Passed | Passed | Passed |
| TC-005 | Переход в английскую Wikipedia | Passed | Passed | Passed |
| TC-006 | Кросс-браузерный запуск | Passed | Passed | Passed |
| TC-007 | Параллельный запуск | Passed | Passed | Passed |

## Вывод

Удаленный запуск тестов через Selenium Grid настроен. Один набор тестов может выполняться в разных браузерах и запускаться параллельно. Критические дефекты функциональности не выявлены.
