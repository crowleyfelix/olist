from .error import Error


class SchemaError(Error):
    def __init__(glom_error=None):
        messages = ["Invalid data passed"]

        if glom_error:
            messages = glom_error.msgs

        super(SchemaError, self).__init__(messages, 400)
