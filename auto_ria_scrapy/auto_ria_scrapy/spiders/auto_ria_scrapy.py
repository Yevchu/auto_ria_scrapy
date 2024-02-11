import scrapy
from scrapy_splash import SplashRequest
from sqlalchemy.orm import Session

from database.models import Base, CarsInfo
from database.db import SessionLocal
from datetime import datetime

session = SessionLocal()

class AutoRiaSpider(scrapy.Spider):

    name = 'AutoRia'
    start_url = 'https://auto.ria.com/uk/car/used/'

    def start_requests(self):
        yield SplashRequest(self.start_url, callback=self.parse, args={'wait': 0.5})

    def parse(self, response, **kwargs):
        for cars_card in response.css('div.content-bar'):
            urls = cars_card.css('.head-ticket a::attr(href)').getall()

            if urls: 
                for url in urls:
                    request = scrapy.Request(
                        url,
                        callback=self.parse_cars_info,
                        cb_kwargs=dict(main_url=response.url, url=url)
                    )
                    yield request

            next_page = response.css('div.boxed nav.unstyle.pager span.page-item.next a::attr(href)').get()
            if next_page is not None:
                yield response.follow(next_page, callback=self.parse)

    def parse_cars_info(self, response, main_url, **kwargs):
        
        title = response.css('h1::text').get()
        price_usd = response.css('span.price_value strong::text').get()
        username = response.css('div.seller_info_name::text').get()
        odometer = response.css('div.bold.dhide::text').get()
        phone_link = response.css('a.phone.bold.dhide.unlink.successfulCall[data-phone-unmask-target-id]')
        carousel_container = response.css('#photosBlock .carousel-inner')
        image_urls = carousel_container.css('img::attr(src)').getall()
        images_count = response.css('span.dhide::text').get()
        car_number = response.css('div.t-check span.state-num.ua::text').get()
        car_vin = response.css('span.label-vin::text').get()

        phone_number = ''
        if phone_link:
            phone_number = phone_link.attrib['data-phone-unmask-target-id']
            phone_number = phone_number.replace('unmask_', '380')
        if odometer:
            odometer = odometer.replace('тис. км пробіг', '000').replace(' ', '')
        if price_usd:
            price_usd = price_usd.replace('$', '').replace(' ', '')
        if images_count:
            images_count = images_count.replace('з ', '')
        
        if not username:
            username = "Неможливо на разі отримати і'мя продавця"
        if not car_number:
            car_number = 'Номер відсутній'
        if not car_vin:
            car_vin = 'Відсутня інформація із цифрових реєстрів МВС по VIN-коду'
            
        self.add_or_update_car_info(
            db=session,
            url=response.url,
            title=title,
            price_usd=price_usd,
            username=username,
            odometer=odometer,
            phone_number=phone_number,
            image_url=image_urls[0],
            images_count=images_count,
            car_number=car_number,
            car_vin=car_vin,
            updated_at=datetime.now()
        )

        yield {
            'url': response.url,
            'title': title.strip(),
            'price_usd': price_usd.strip(),
            'username': username.strip(), #TODO: і'мя записани латинськими буквами не скрапуються скрапером, поки не знаю що з цим робити
            'odometer': odometer.strip(),
            'phone_number': phone_number.strip(),
            'image_url ': image_urls[0].strip(), #TODO: чи треба тут всі фото чи треба тільки перше? 
            'images_count': images_count.strip(),
            'car_number': car_number.strip(),
            'car_vin': car_vin.strip(),
        }

    def add_or_update_car_info(self, db: Session, url:str, **kwargs):
    
        existing_car_from_db = db.query(CarsInfo).filter_by(url=url).first()

        if existing_car_from_db:
            for key, value in kwargs.items():
                setattr(existing_car_from_db, key, value)
        else: 
            new_car = CarsInfo(url=url, **kwargs)
            db.add(new_car)
        db.commit()

