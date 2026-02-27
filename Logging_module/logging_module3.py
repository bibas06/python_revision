import logging
logging.basicConfig(level=logging.INFO,filename='log3.log',filemode='w')
logger=logging.getLogger(__name__)
logger.info('test the custom logger')