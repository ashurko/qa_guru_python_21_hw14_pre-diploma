import allure

from pages.home_page import JobsPage, GamesPage, HomePage

home_page = HomePage()
game_page = GamesPage()
jobs_page = JobsPage()

@allure.feature("Главная")
def test_home_title_contains_playrix():
    home_page.open('https://playrix.com/').should_have_title("Playrix")

@allure.feature("Саппорт")
def test_go_to_support_page():
    home_page.go_to_contact().go_to_helpshift().check_helpshift_url()

@allure.feature("Вакансии")
def test_open_job_page():
    jobs_page.open_job_page("QA").should_have_qa_jobs("QA")

@allure.feature("Страница игры на сайте")
def test_open_game_page():
    game_page.open_fishdom_page().should_have_fishdom_text_description()

@allure.feature("Страница игры в сторе")
def test_open_store_game_page():
    game_page.open_fishdom_page().open_store_link().should_open_app_store()

@allure.feature("Страница игры в X")
def test_go_to_twitter():
    home_page.go_to_twitter().should_be_open_twitter()


