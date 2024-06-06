import sys
from src.logger import logging


# <<<<<<<<<<<<<<  ✨ Codeium Command 🌟 >>>>>>>>>>>>>>>>
# +def error_message_detail(error, error_detail:sys):
# +    """
# +    This function generates a detailed error message for the error that occurred.
# +    
# +    Args:
# +        error (Exception): The error that occurred.
# +        error_detail (sys): Contains details about the error.
# +        
# +    Returns:
# +        str: The detailed error message.
# +    """
# +    
# +    # Get the error details from the error_detail object
# +    _, _, exc_tab = error_detail.exc_info()
# +    
# +    # Get the name of the Python script where the error occurred
# +    error_name = exc_tab.tb_frame.f_code.co_filename
# +    
# +    # Get the line number where the error occurred
# +    error_lineno = exc_tab.tb_lineno
# +    
# +    # Generate the detailed error message
# +    error_message = "error occured in python script name [{0}], line no [{1}], error message [ {2}]".format(
# +        error_name, error_lineno, str(error)
# +    )
# +    
# +    return error_message
def error_message_detail(error, error_detail:sys):
    
    _, _, exc_tab = error_detail.exc_info()
    error_name = exc_tab.tb_frame.f_code.co_filename
    error_message = "error occured in python script name [{0}], line no [{1}], error message [ {2}]".format(
        error_name, exc_tab.tb_lineno, str(error)
    )
    
    return error_message



class CustomException(Exception):
# +    """
# +    This is a custom exception class that takes in an error message and error detail
# +    as arguments and returns a detailed error message. The error message is a string
# +    that describes the error that occurred. The error detail is an object that contains
# +    details about the error, such as the line number and the name of the Python script
# +    where the error occurred. This custom exception class is useful for handling errors
# +    in a program and providing detailed error messages to the user.
# +
# +    Attributes:
# +    - `error_message` (str): The detailed error message.
# +    """
     # def __init__(self, error_message, error_detail:sys):
# +        """
# +        Initializes a CustomException object.
# +
# +        Args:
# +        - error_message (str): The error message that describes the error that occurred.
# +        - error_detail (sys): Contains details about the error, such as the line number
# +          and the name of the Python script where the error occurred.
# +        """
        # super().__init__(error_message)
    def __init__(self,error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, 
                                                   error_detail=error_detail)
    def __str__(self):
        return self.error_message





# test lines for logger.py
# if __name__ == "__main__":
#     try:
#         a= 1/0
#     except Exception as e:
#         logging.info ("Divide by zero error")
#         raise CustomException(e, sys)