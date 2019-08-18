import logging
logging.basicConfig(filename="mylog.txt",level=logging.INFO)
logging.info("A New request came:")
try:
    x=int(input("Enter the first number: "))
    y=int(input("Enter the second number: "))
    print(x/y)
except ZeroDivisionError as msg:
    print("Cannot divided with Zero")
    logging.exception(msg)
except ValueError as msg:
    print("Enter only int values")
    logging.exception(msg)
logging.info("request processing completed")