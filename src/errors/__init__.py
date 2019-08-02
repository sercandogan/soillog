"""
Errors
"""


class Error(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code
        super(Exception, self).__init__({'message': message, 'code': code})



class Temp_Humidity_IOError(Error):
    def __init__(self):
        Error.__init__(self, "Couldn't read temp and humidity value.", 500)

