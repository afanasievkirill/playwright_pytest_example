from playwright.sync_api import Page, expect
import pytest


def test_add_group(desktop_app_auth) -> None:
    desktop_app_auth.group.create()
