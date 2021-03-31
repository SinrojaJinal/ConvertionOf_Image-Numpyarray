import logging

class Logger:

    logger = logging.getLogger(__name__)
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(name)s: %(message)s')
        
    file_handler = logging.FileHandler('logs.log')
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    def write_logs(level, message):
        
        # Setting Custom Levels
        if level == 'info':
            Logger.logger.setLevel(logging.INFO)
            Logger.logger.info(message)
        
        elif level == 'debug':
            Logger.logger.setLevel(logging.DEBUG)
            Logger.logger.debug(message)
        
        elif level == 'error':
            Logger.logger.setLevel(logging.ERROR)
            Logger.logger.error(message)

        elif level == 'warning':
            Logger.logger.setLevel(logging.WARNING)
            Logger.logger.warning(message)

        elif level == 'critical':
            Logger.logger.setLevel(logging.CRITICAL)
            Logger.logger.critical(message)