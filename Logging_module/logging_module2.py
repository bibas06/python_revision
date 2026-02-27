import logging
logging.basicConfig(level=logging.INFO,filename='log1.log',filemode='w')
x=69
logging.info(f"the value of x is {x}")
try:
    1/0
except ZeroDivisionError as e:
    logging.error("Zero division error",exc_info=True)#or use logging.exception("Zero division error")
