import sys # this library will manage all the system level errors
from src.logger import logging # for logging purpose

def error_message_detail(error,error_detail:sys):
    """_summary_

    Args:
        error (_type_): _description_
        error_detail (sys): _description_

    Returns:
        _type_: _description_
    """
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] in the line number [{1}] and the \
    error message[{2}]".format(file_name,exc_tb.tb_lineno,str(error))

    return error_message

    
class CustomException(Exception): #own custom exception class
    def __init__(self,error_message,error_detail:sys):
        """_summary_

        Args:
            error_message (_type_): _description_
            error_detail (sys): _description_
        """
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
    
    def __str__(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.error_message