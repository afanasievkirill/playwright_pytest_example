from playwright.sync_api import Page, expect


class Group:
    def __init__(self, page: Page):
        self.page = page

    def go_to_group_page(self):
        self.page.get_by_role("link", name="groups").click()
        expect(self.page).to_have_url("http://localhost/addressbook/group.php")

    def create(self, name: str, header: str, footer: str):
        self.go_to_group_page()
        self.page.get_by_role("button", name="New group").first.click()
        expect(self.page).to_have_url(
            "http://localhost/addressbook/group.php?new=New+group"
        )

        self.page.fill('input[name="group_name"]', name)
        self.page.fill('textarea[name="group_header"]', header)
        self.page.fill('textarea[name="group_footer"]', footer)

        self.page.get_by_role("button", name="Enter information").click()

        expect(self.page.locator("div.msgbox")).to_have_text(
            "A new group has been entered into the address book.return to the group page"
        )
