import allure
from selene import browser, have, be


class HomePage:
    @allure.step('Открываем главную страницу')
    def open(self, url):
        browser.open(url)
        return self

    @allure.step("Проверить, что title содержит название")
    def should_have_title(self, text):
        browser.should(have.title_containing(text))
        return self

    @allure.step('Открыть страницу контактов из футера')
    def go_to_contact(self):
        footer = browser.element('footer')
        link = footer.all("a[href*='contact']").filtered_by(be.visible).first
        link.should(be.visible).click()
        return self

    @allure.step('Переходим в саппорт')
    def go_to_helpshift(self):
        browser.element('.support__button').click()
        return self

    @allure.step('Проверяем URL сервиса поддержки')
    def check_helpshift_url(self):
        browser.should(have.url_containing("playrix.helpshift"))
        return self

    @allure.step('Открыть страницу Twitter из футера')
    def go_to_twitter(self):
        footer = browser.element('footer')
        link = footer.all("a[href='https://twitter.com/Playrix']").filtered_by(be.visible).first
        link.should(be.visible).click()
        return self

    @allure.step('Проверить правильно ли открылась страница')
    def should_be_open_twitter(self):
        browser.should(have.url_containing("x.com"))
        browser.element("[data-testid='UserName']").should(have.text('Playrix'))


class GamesPage:
    @allure.step('Отрываем страницу Fishdom')
    def open_fishdom_page(self):
       browser.element("a.main-menu__link[href='/games']").click()
       #browser.execute_script('window.scrollBy(0, 1000)')
       browser.element('a.game--fishdom.games-list__item').should(be.visible).click()
       return self


    @allure.step('Проверяем переход на страницу Fishdom')
    def should_have_fishdom_text_description(self):
        browser.element('.header-block__header').should(have.text('Fishdom'))
        return self

    @allure.step('Переходим на страницу игры в сторе')
    def open_store_link(self):
        #browser.execute_script('window.scrollBy(0, 500)')
        browser.element("a.application-stores__item[href*='apple']").should(be.visible).click()
        return self

    @allure.step('Проверяем стор и игру, на которую ведет ссылка')
    def should_open_app_store(self):
        browser.should(have.url_containing('apps.apple.com'))
        browser.element("h1.product-header__title.app-header__title").should(have.text("Fishdom"))
        return self

class JobsPage:
    @allure.step("Открываем страницу поиска работы: {job}")
    def open_job_page(self, job):
        browser.element("a[href*='/job']").hover()
        browser.element("a[href*='/job/open']").click()
        browser.all(".tags-list__name").by(have.exact_text(job)).first.click()
        return self

    @allure.step('Проверяем работу фильтра')
    def should_have_qa_jobs(self, job):
        browser.element('.jobs-card__section-name').should(have.text(job))
        return self


