from us_visa.logger import logging
from us_visa.exception import USvisaException
import sys
#logging.info("Demo file for us_visa package")
try:
    a=1/0
except Exception as e:
    raise USvisaException(e,sys)