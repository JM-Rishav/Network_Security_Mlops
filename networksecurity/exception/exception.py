# For handling any custom exceptions that may arise in the network security module.

import sys
from networksecurity.logger import logging
class NetworkSecurityException(Exception):
    def __init__(self, error_message, error_detils:sys):
        self.error_message = error_message
        _,_,exc_tb = error_detils.exc_info()

        self.lineno = exc_tb.tb_lineno
        self.filename = exc_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return f"Error Message: {self.error_message} | Line Number: {self.lineno} | File Name: {self.filename}"
        self.file_name, self.line_number, self.error_message = error_message


if __name__ =='__main__':
    try: 
        a = 1 / 0  # This will raise a ZeroDivisionError
        print("This line will not be executed.",a)
    except NetworkSecurityException as e:
        raise NetworkSecurityException("An error occurred in the network security module.", sys) from e