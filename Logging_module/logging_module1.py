import logging
logging.basicConfig(level=logging.INFO,filename='log.log',filemode='w',
                    format="%(asctime)s - %(levelname)s - %(message)s")#this statement only runs one time 
                                                                       #so runs this at the very starting of program
logging.debug('debug')
logging.info('info')
logging.warning('warning')
logging.error('error')
logging.critical('critical')
#without using any kind of levels the o/p will be excute for warning and statements under it(i.e. warning,error,critical).
#root=name of logger