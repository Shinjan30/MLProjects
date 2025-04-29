import sys

def error_message_details(error,error_details:sys):
    _,_,exc_tb = error_details.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = f"Error occurred in script: [{file_name}] at line number: [{line_number}] error message: [{str(error)}]"
    return error_message

def handle_exception(error, error_details:sys):
    error_message = error_message_details(error, error_details)
    # Log the error message to a file or console
    # For simplicity, we will just print it here
    print(error_message)