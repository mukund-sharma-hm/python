# 1. Write a decorator to log the following details whenever a function is called
# 	a. The File needs to be name of the <module>_<YYYYMMDD>.log
# 	b. The messages in the logs file should follow the format as below
# 		<module name> <function name> <DD-MM-YY> <hh:mm:ss> <Dict of Arguments passed to the function>

import datetime

def logger(func):
    """decorator for logging"""    
    def wrapper(*args, **kwargs):

        date = datetime.datetime.now()
        formatted_date = date.strftime("%Y-%m-%d")
        formatted_time = date.strftime( "%H:%M:%S")
        module = func.__module__
        function_name = func.__name__
        args_dict = {"args": args, "kwargs": kwargs}

        logs = f"{module} {function_name}, {formatted_date}, {formatted_time}, {args_dict}"

        with open(f"{module}_{formatted_date}.log","a", encoding="utf-8",) as log_file:
            log_file.write(logs + "\n")

    return wrapper
