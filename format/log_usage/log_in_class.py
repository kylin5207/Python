import logging

class MyClass:
    def __init__(self):  # Corrected from 'init' to '__init__'
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.setLevel(logging.DEBUG)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def do_something(self):
        self.logger.debug("Doing something...")
        # Do something here
        self.logger.info("Something done!")

obj = MyClass()  # Corrected the instantiation
obj.do_something()