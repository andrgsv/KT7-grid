# Конфигурация Selenium Grid

## Цель конфигурации

Настроить удаленное выполнение Selenium-тестов через Selenium Grid с возможностью параллельного запуска в нескольких браузерах.

## Выбранный вариант настройки

В проекте используется Docker Compose, так как он позволяет быстро поднять Hub и Node без ручной установки Selenium Server на разные машины.

## Состав Grid

| Компонент | Назначение | Адрес / образ |
|---|---|---|
| Hub | Центральный узел, принимающий тесты | selenium/hub:4.27.0 |
| Chrome Node | Узел для выполнения тестов в Chrome | selenium/node-chrome:4.27.0 |
| Firefox Node | Узел для выполнения тестов в Firefox | selenium/node-firefox:4.27.0 |

## Адреса

| Назначение | URL |
|---|---|
| Web-интерфейс Grid | http://localhost:4444/ui |
| Remote WebDriver URL | http://localhost:4444/wd/hub |

## Команды

Запуск Grid:

```bash
docker compose up -d
```

Проверка контейнеров:

```bash
docker compose ps
```

Запуск тестов:

```bash
pytest -n 2 --browser chrome,firefox
```

Остановка Grid:

```bash
docker compose down
```

## Альтернативный запуск через JAR

Если Docker недоступен, можно использовать Selenium Server JAR.

Запуск Hub:

```bash
java -jar selenium-server-<version>.jar hub
```

Запуск Node:

```bash
java -jar selenium-server-<version>.jar node --hub http://<hub-ip>:4444
```

## Вывод

Конфигурация позволяет запускать один набор тестов удаленно и параллельно в разных браузерах. Это повышает скорость тестирования и помогает проверять кросс-браузерную совместимость.
