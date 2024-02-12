# auto_ria_scrapy
legend: 
    -name - це папка
    --name.ext - це файл

Тестове завдання по скрапінгу веб додатку. 
    Струкрута: 
        -auto_ria_scrapy 
            -auto_ria_scrapy 
                -alembic
                    -version
                    --env.py
                -auto_ria_scrapy
                    -spiders 
                        --__init__.py
                        --auto_ria_scrapy.py 
                    --__init__.py
                    --items.py
                    --middlewares.py
                    --pipelines.py
                    --settings.py
                -database
                    --db.py
                    --models.py 
                -dumps 
                --alembic.ini 
                --app.log 
                --main.py 
                --scrapy.cfg 
            -scrapy_env 
            --.env 
            --docker-compose.yml 
            --README.md 
            --docker-compose.yml
            --requirements.txt

Логіка роботи скрапера:
    після активації скрапера він витягує з основгого посиланя(https://auto.ria.com/car/used/) посиланя на всі машини які є на сайті, потім ці посиланя передаються в наступну функцію яка переходить по кожному отриманому посиланю і витягує потрібну нам інформацію:(url (строка)
    title (строка)
    price_usd (число)
    odometer (число, нужно перевести 95 тыс. в 95000 и записать как число)
    username (строка)
    phone_number (число, пример структуры: +38063……..)
    image_url (строка)
    images_count (число)
    car_number (строка)
    car_vin (строка)
    datetime_found (дата сохранения в базу)
    ) 

    Після отримана інформація вичіщається і приводиться до єдиного стандарту і далі записується до бази даних. 

Щоб запустити скрапера виконайте наспутні кроки: 
    1.встановіть все необхідні пакети за допомогою команди: pip install -r requirements.txt
    2.запустіть docker-compose командою: docker-compose up
    3.активуйте віртуальне середовище командою: scrapy_env\Scripts\activate
    4.перейдіть в папку auto_ria_scrapy командою: cd auto_ria_scrapy
    5.запустіть скрапера командою python main.py
        5.1 спочатку активується дамп бази даних щоб зробити бекап. в терміналі впишіть пароль: 567234
        5.2 після успішного бекапу запуститься скрапер і почне витягувати дані з авторія. процес скрапуваня займає якийсь час(процес скрапуваня можна зупинити завчасно комбінацією клавіш ctrl+c)
    

Нажаль не вдалось реалізувати механізм автоматичного запуску скрапера і не вдалось обійти потребу кожен рас водити пароль перед тим як зробити бекап бази даних через брак досвіду і знання. Створення задачі по запуску скрипта в Task Scheduler на віндовс не дало належного результату, скрипт не запускається. 