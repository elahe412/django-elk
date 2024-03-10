from celery import shared_task
import logging


@shared_task
def log_message(message):
    logging.info(message)
    return f"Logged: {message}"
