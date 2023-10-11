# Тестотвое задание для Bewise.ai
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white) 
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white) 

## Задача

Реализовать на Python3 простой веб сервис (с помощью FastAPI или Flask, например), выполняющий следующие функции:
В сервисе должно быть реализовано REST API, принимающее на вход POST запросы с содержимым вида {"questions_num": integer}  ;

После получения запроса сервис, в свою очередь, запрашивает с публичного API (англоязычные вопросы для викторин) https://jservice.io/api/random?count=1 указанное в полученном запросе количество вопросов.
Далее, полученные ответы должны сохраняться в базе данных из п. 1, причем сохранена должна быть как минимум следующая информация (название колонок и типы данный можете выбрать сами, также можете добавлять свои колонки): 1. ID вопроса, 2. Текст вопроса, 3. Текст ответа, 4. - Дата создания вопроса. В случае, если в БД имеется такой же вопрос, к публичному API с викторинами должны выполняться дополнительные запросы до тех пор, пока не будет получен уникальный вопрос для викторины.
Ответом на запрос из п.2.a должен быть предыдущей сохранённый вопрос для викторины. В случае его отсутствия - пустой объект.

## Запуск проекта:

### Слонировать репозиторий и перейти в папку с проектом
```bash
git clone git@github.com:94R1K/Bewise.ai_test.git
```

```bash
cd Bewise.ai_test/
```

### Запустить проект через docker-compose
```bash
docker-compose up
```

И далее проект доступен на: 

```
http://localhost:8000/redoc
```

## Пример запроса к API сервиса

### POST-запрос на получение англоязычных вопросов для викторин:
```
http://localhost:8000/get_questions/
```

### Ответ от API (Если есть уникальный вопрос для викторины):

```json
{
    "last_question": "The largest delta in the world is the one of this river that reaches the sea in Bangladesh & India"
}
```

### Ответ от API (Если нет уникального вопроса для викторины):
```json
{}
```


## Остановка оркестра контейнеров

В терминале, где был запуск зажать: *Ctrl+С*


# Об авторе
Лошкарев Ярослав Эдуардович \
Python-разработчик (**Backend**) \
Россия, г. Москва \
E-mail: **real-man228@yandex.ru**

[![TG](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/yallluv)
[![VK](https://img.shields.io/badge/Вконтакте-%232E87FB.svg?&style=for-the-badge&logo=vk&logoColor=white)](https://vk.com/yalluv)
