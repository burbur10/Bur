import logging
import traceback
#try:
  #  s= [0,9,6]
 #   val=s[4]
#except:IndexError is e
#logging.error(e)
import traceback
try:
    s= [0,9,4,8]
    val=s[4]
except:
    logging.error("The error is %s", traceback.format_exc())
