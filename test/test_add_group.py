from playwright.sync_api import Page
import pytest


def test_add_group(page: Page):
    page.goto("/addressbook/index.php")
    assert page.title() == "Address book"
