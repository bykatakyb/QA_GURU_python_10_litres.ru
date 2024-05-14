<h1> Проект по тестированию сервиса "Литрес"</h1>

> <a target="_blank" href="https://www.litres.ru">litres.ru</a>

![This is an image](design/image/litres_page.png)

<h3> Список Автоматиризованныйх проверок:</h3>

### UI-тесты
- [x] Авторизация с валидными данными 
- [x] Авторизация с невалидными данными (негативный кейс) 
- [x] Проверка состояния корзины по умолчанию для авторизованного пользователя
- [x] Проверка состояния корзины по умолчанию для неавторизованного пользователя (негативный кейс)
- [x] Проверка наличия баннера с промоакцией внутри корзины
- [x] Добавление продукта в корзину
- [x] Удаление продукта из корзины
- [x] Проверка поиска продукта по названию
- [x] Проверка поиска продукта по автору

### API-тесты
- [x] Авторизация с валидными данными 
- [x] Авторизация с невалидными данными (негативный кейс) 
- [x] Проверка поиска продукта по названию
- [x] Проверка поиска несуществующего продукта (негативный кейс) 


----
### Проект реализован с использованием:
<img src="design/icons/python-original.svg" width="50"> <img src="design/icons/intellij_pycharm.png" width="50"> <img src="design/icons/pytest.png" width="50"> <img src="design/icons/selene.png" width="50"> <img src="design/icons/allure_report.png" width="50"> <img src="design/icons/jenkins.png" width="50"> <img src="design/icons/selenoid.png" width="50"> <img src="design/icons/allure_testops.png" width="50"> <img src="design/icons/jira.png" width="50"> <img src="design/icons/tg.png" width="50"> 

----
### Локальный запуск
> Для локального запуска необходимо выполнить команду:
```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest tests
```

----
### Удаленный запуск автотестов выполняется через интерфейс сервиса Jenkins
> <a target="_blank" href="https://jenkins.autotests.cloud/job/vbukatov_diploma/">Jenkins</a>



#### Для запуска автотестов в Jenkins:

1. Открыть <a target="_blank" href="https://jenkins.autotests.cloud/job/vbukatov_diploma/">Страницу проекта</a>
2. Выбрать пункт `Build Now`
3. Результаты выполнения тестов сборки можно посмотреть в отчёте Allure

----
### Allure отчет


#### Общие результаты


#### Список тест кейсов


#### Пример отчета о прохождении ui-теста


#### Пример отчета о прохождении api-теста



----
### Полная статистика по прохождению тестпланов, отчёты и приложения к ним хранятся в Allure TestOps
> <a target="_blank" href="https://allure.autotests.cloud/project/4235/dashboards">AllureTestOps</a> (доступ по запросу у `admin@qa.guru`)

#### Тест-планы проекта


#### Общий список всех кейсов, имеющихся в системе (без разделения по тест-планам и виду выполнения тестирования)



#### Пример отчёта выполнения одного из автотестов



#### Тестовые артефакты



#### Пример dashboard с общими результатами тестирования



#### История запуска тестовых наборов



----
### Интеграция с Jira
> <a target="_blank" href="https://jira.autotests.cloud/browse/HOMEWORK-1230">Jira</a>

![This is an image](design/image/jira.png)

----
### Оповещение о результатах прогона тестов в Telegram

![This is an image](design/image/tg_notification.png)

----
### Пример видео прохождения UI-автотеста

![autotest_gif](design/image/autotest.gif)