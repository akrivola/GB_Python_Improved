import logging

logger = logging.getLogger(__name__)


def log_all():
    logger.debug('Отладочная информация')
    logger.info('Немного информации')
    logger.error('Поймали ошибку')
    logger.warning("Внимание")
    logger.critical('Всё')


if __name__ == '__main__':
    log_all()
