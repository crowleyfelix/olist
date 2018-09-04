class Error(Exception):
    def __init__(self, messages, status_code):
        self.messages = messages
        self.status_code = status_code

        super(Error, self).__init__(' | '.join(messages))
