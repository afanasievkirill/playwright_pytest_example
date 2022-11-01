from playwright.sync_api import Page, expect
import pytest


def test_add_group(page: Page) -> None:
    page.goto("/addressbook/index.php")

    page.fill('input[name="user"]', "admin")
    page.fill('input[name="pass"]', "secret")
    page.get_by_role("button", name="Login").click()
    expect(page).to_have_url("http://localhost/addressbook/index.php")

    page.get_by_role("link", name="groups").click()
    expect(page).to_have_url("http://localhost/addressbook/group.php")

    page.get_by_role("button", name="New group").first.click()
    expect(page).to_have_url("http://localhost/addressbook/group.php?new=New+group")

    page.fill('input[name="group_name"]', "playwright_name")
    page.fill('textarea[name="group_header"]', "playwrith_header")
    page.fill('textarea[name="group_footer"]', "playwright_footer")

    page.get_by_role("button", name="Enter information").click()

    expect(page.locator("div.msgbox")).to_have_text(
        "A new group has been entered into the address book.return to the group page"
    )

    page.get_by_role("link", name="groups").click()
    expect(page).to_have_url("http://localhost/addressbook/group.php")

    page.get_by_role("link", name="Logout").click()
    expect(page.locator('input[name="user"]')).to_be_visible()
