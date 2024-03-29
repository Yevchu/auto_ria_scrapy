import os 
import subprocess
from datetime import datetime
from dotenv import load_dotenv
import logging

load_dotenv()

POSTGRES_DB = os.getenv('POSTGRES_DB')
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_HOST = os.getenv('POSTGRES_HOST')
POSTGRES_PORT = os.getenv('POSTGRES_PORT')
CRON_HOUR = os.getenv('CRON_HOUR')
CRON_MINUTE = os.getenv('CRON_MINUTE') 

logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def run_scraper():
    command = 'scrapy crawl AutoRia'
    logging.info('Start the scraper...')
    try:
            subprocess.run(command, shell=True)
            logging.info('Scraper finished successfully.')
    except Exception as e:
        logging.error('Error occurred during scraper execution:', exc_info=True)

def create_db_dump():
    current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    dump_folder = 'dumps'
    dump_file_name = f'{dump_folder}/database_dump_{current_datetime}.sql'

    command = [
        # 'C:\\Program Files\\PostgreSQL\\16\\bin\\pg_dump.exe',
        'pg_dump',
        '-U', POSTGRES_USER, 
        '-d', POSTGRES_DB, 
        '-f', dump_file_name
    ]

    if not os.path.exists(dump_folder):
        os.makedirs(dump_folder)

    logging.info('Creating database dump...')
    try:
        subprocess.run(command, shell=True)
    except Exception as e:
        logging.error('Error occurred during database dump creation:', exc_info=True)


def run_daily_task():
    logging.info('Running daily task...')
    try:
        create_db_dump()
        run_scraper()
        logging.info('Daily task completed.')
    except Exception as e:
        logging.error('Error occurred during daily task execution:', exc_info=True)


if __name__ == "__main__":
    run_daily_task()

