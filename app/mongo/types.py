class List(object):
    def __init__(self, cursor):
        self._cursor = cursor

    def __iter__(self):
        return self

    def __next__(self):
        try:
            document = self._cursor.next()
            document.pop("_id")
            return document
        except StopIteration as ex:
            self._cursor.close()
            raise ex
