"""
This is the first module that illustrates logging by setting all configurations programatically
"""
import logging

logger = logging.getLogger('module1')
h = logging.StreamHandler()
h.setFormatter(logging.Formatter('%(asctime)s %(levelname)8s %(name)s | %(message)s'))
logger.addHandler(h)
logger.setLevel(logging.INFO)
logger.info('logging info at module level')


class c1:
    """
    This class contains two methods
    """
    def __init__(self):
        """
        The is the init method called when an instance is created
        """
        logger = logging.getLogger('module1_c1_init')
        logger.addHandler(h)
        logger.setLevel(logging.WARNING)
        logger.warning('logging warn for class c1 init method')

    def __call__(self, *args, **kwargs):
        """
        This is the call method that is called when the object is called
        :param args: <any>
        :param kwargs: <any>
        :return: <none>
        """
        logger = logging.getLogger('module1_c1_call')
        logger.addHandler(h)
        logger.setLevel(logging.WARNING)
        logger.warning('logging warn for class c1 call method')

    def dummy_method(self, param1, *args):
        """
        This is a dummy method placed here for illustrating the api documentation using sphinx-apidoc.

        :param param1: a paramter to the method
        :param args: some argument list.
        :return: returns nothing really.

        """

if __name__ == '__main__':
    o1 = c1()
    o1()
