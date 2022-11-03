from pytest import fixture
from playwright.sync_api import sync_playwright
from settings import *

from page_object.application import App


@fixture(scope="session")
def get_playwright():
    with sync_playwright() as playwright:
        yield playwright


@fixture(scope="session")
def desktop_app(get_playwright, request):
    base_url = request.config.getini("base_url")
    app = App(get_playwright, base_url, **BROWSER_OPTIONS)
    app.goto("/addressbook/index.php")
    yield app
    app.close()


@fixture(scope="function")
def desktop_app_auth(desktop_app):
    app = desktop_app
    app.goto("/addressbook/index.php")
    app.login("admin", "secret")
    yield app
    app.logout()


@fixture(scope="session")
def mobile_app(get_playwright, request):
    base_url = request.config.getini("base_url")
    device = request.config.getoption("--test_device")
    app = App(get_playwright, base_url, device=device, **BROWSER_OPTIONS)
    app.goto("/addressbook/index.php")
    yield app
    app.close()


@fixture(scope="function")
def mobile_app_auth(mobile_app):
    app = mobile_app
    app.goto("/addressbook/index.php")
    app.login("admin", "secret")
    yield app
    app.logout()


def pytest_addoption(parser):
    parser.addoption("--test_device", action="store", default="")
    parser.addini("base_url", help="Базовый урл сайта для тестов.")
