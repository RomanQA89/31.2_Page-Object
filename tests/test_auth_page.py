from pages.auth_page import AuthPage
import time


def test_auth_page(selenium):
    page = AuthPage(selenium)
    page.enter_email('pihianov.rom@yandex.ru')
    page.enter_pass('12345')
    page.btn_click()

    assert page.get_relative_link() == '/all_pets', 'login error'

    time.sleep(5)
