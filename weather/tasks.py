from django.conf import settings

from celery import shared_task
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@shared_task()
def thirty_second_func():
    logger.info('I run every 30 seconds using Celery Beat')
    return 'Done'



