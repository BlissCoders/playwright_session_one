class LoginPage:

    def __init__(self, page):
        self.page = page
        self.username = page.get_by_role("textbox", name="email")
        self.password = page.get_by_label("Password")
        self.login_button = page.get_by_role("button", name="Login")
        self.success_message = page.get_by_role("alert")

    @classmethod
    def open(cls, page, url:str="http://192.168.1.79:5000/login") -> 'LoginPage':
        page.goto(url)
        return cls(page)


    def login(self, username:str, password:str):
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()
        assert self.success_message.inner_text() == 'Successful login!'