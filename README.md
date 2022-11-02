# playwright_pytest_example

<a id="markdown-описание" name="Предварительные настройки."></a>

## Предварительные настройки.

Подготовить виртуальное окружение Python.

```
$ python -m venv venv
```

Активировать виртуальное окружение Python.

```
$ .\venv\Scrypt\activate
```

Установить зависимости.

```
$ pip install -r requirements.txt
```

<a id="markdown-описание" name="Запуск тестов."></a>

## Запуск тестов.

Запуск всех тестов в Хэдлесс моде.

```
$ pytest --base-url http://localhost
```

Запуск всех тестов.

```
$ pytest --headed --base-url http://localhost
```

<a id="markdown-описание" name="Генерация тестов."></a>

## Генерация тестов.

```
$ playwright codegen ${URL}
```

<a id="markdown-описание" name="Полезные ссылки."></a>

## Полезные ссылки.

```
$ https://playwright.dev/python/
```

```
$ https://devhints.io/css
```

```
$ https://devhints.io/xpath
```
