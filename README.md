# 🎓 QA.GURU Playrix Project

*Небольшой проект по автоматизации Playrix, базовой проверке нескольких кейсов*
# <code><img width="30%" title="plrx_logo" src="data/logo/300_transparent.png" /></code>
## О проекте

Этот проект является дипломной работой по курсу QA.GURU и представляет собой фреймворк для автоматизации тестирования веб-сайта ["Playrix"](https://www.playrix.com). В реализации использованы инструменты и библиотеки:

<p  align="center">
  
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" height="70" width="70"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/jenkins/jenkins-original.svg" height="70" width="70"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pytest/pytest-original.svg" height="70" width="70"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/github/github-original.svg" height="70" width="70"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/selenium/selenium-original.svg" height="70" width="70"/>
  <img width="9%" title="Selene" src="data/logo/selene.png" alt="selene"/>
  <img width="8%" title="Allure Report" src="data/logo/allure_report.png" alt="allure">
  <img width="8%" title="Allure Testops" src="data/logo/allure_testops.png" alt="alluretest">
  <img width="8%" title="Selenoid" src="data/logo/selenoid.png" alt="selenoid">
</p>

## <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" height="20" width="20"> Запуск тестов локально

1) Клонировать репозиторий: git clone https://github.com/ashurko/qa_guru_python_21_hw14_pre-diploma.git
2) Установить зависимости: pip install -r requirements.txt
3) Запуск тестов с генерацией отчетов Allure: pytest --alluredir=reports/allure-results

##   <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/jenkins/jenkins-original.svg" height="20" width="20"/> Создание сборки на удаленном сервере - Jenkins

1) Авторизоваться в Jenkins
2) Перейти в джобу https://jenkins.autotests.cloud/job/anton_shurko_hw14/
3) Для запуска тестов в Jenkins нажать "Build With Parameters"
4) Выбрать необходимые параметры
5) Нажать Run Build

<p><img title="jenkins_build" src="data/logo/jenkins_flow1.png"></p>

<p><img title="jenkins_build" src="data/logo/jenkins_flow2.png"></p>

## <img width="4%" title="allure" src="data/logo/allure_report.png"> Визуализация результатов (Allure Reports и Allure TestOps)

Для просмотра результатов тестового прогона в Allure клик на соответствующую ему иконку

<p><img title="Allure" src="data/logo/allure_result1.png"></p>
<p><img title="Allure" src="data/logo/allure_result2.png"></p>



Для просмотра результатов тестового прогона в Allure TestOps кликнув на соответствующую ему иконку в джобе Jenkins

<p><img title="allure_testops" src="data/logo/job_testops.png"></p>БУДЕТ ДОПОЛНЕНО
<p><img title="allure_testops" src="data/logo/img_testops.png"></p>БУДЕТ ДОПОЛНЕНО


## <img width="4%" title="tg" src="data/logo/tg.png"> Интеграция с Telegram в Jenkins для автоматической отправки результатов тестового прогона через бота

<p><img title="telegram" src="data/logo/report_tg.png"></p>