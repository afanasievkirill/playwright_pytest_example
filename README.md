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
