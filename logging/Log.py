import sys
import traceback
import logging


def setup_logging_to_file(filename):
    logging.basicConfig(filename=filename,
                        filemode='w',
                        level=logging.DEBUG,
                        format='[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s in %(module)s - %(message)s')


def extract_function_name():
    tb = sys.exc_info()[-1]
    stk = traceback.extract_tb(tb, 1)
    func_name = stk[0][3]
    return func_name


def log_exception(e):
    logging.error(
        "Function {function_name} raised {exception_class} ({exception_docstring}): {exception_message}".format(
            function_name=extract_function_name(),  # this is optional
            exception_class=e.__class__,
            exception_docstring=e.__doc__,
            exception_message=e.message))
