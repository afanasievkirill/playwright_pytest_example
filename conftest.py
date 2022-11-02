from pytest import fixture
from playwright.sync_api import sync_playwright

from page_object.application import App


@fixture(scope="session")
def get_playwright():
    with sync_playwright() as playwright:
        yield playwright


@fixture(scope="session")
def desktop_app(get_playwright, base_url="http://localhost"):
    app = App(get_playwright, base_url)
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
