import sys
from NetworkSecurity.logging import logger

class NetworkSecurityException(Exception):
    def __init__(self, error_message, error_details: sys):
        super().__init__(error_message)
        self.error_message = error_message

        try:
            _, _, exc_tb = error_details.exc_info()
            if exc_tb is not None:
                self.lineno = exc_tb.tb_lineno
                self.file_name = exc_tb.tb_frame.f_code.co_filename
            else:
                self.lineno = None
                self.file_name = None
        except:
            self.lineno = None
            self.file_name = None

    def __str__(self):
        return "Error occurred in Python script [{0}] at line number [{1}] with message: [{2}]".format(
            self.file_name, self.lineno, str(self.error_message)
        )

if __name__ == '__main__':
    try:
        logger.logging.info("Enter the try block")
        a = 1 / 0
        print("This will not be printed", a)

    except Exception as e:
        raise NetworkSecurityException(e, sys)
