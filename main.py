class DataStorage:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"DataStorage: {self.value}"


class Local(DataStorage):
    def __str__(self):
        return f'{super().__str__()} - local'


class Web(DataStorage):
    def __init__(self, value, domain):
        super().__init__(value)
        self.domain = domain

    def __str__(self):
        return f'{super().__str__()} - web, domain: {self.domain}'


class Removable(DataStorage):
    def __init__(self, value, dev_type):
        super().__init__(value)
        self.dev_type = dev_type

    def __str__(self):
        return f'{super().__str__()} - removable, domain: {self.dev_type}'


class Session(Web):
    def __str__(self):
        return f'{super().__str__()} - session'


if __name__ == '__main__':
    ds = DataStorage([1, 2, 3])
    loc = Local(["a", "b", "c"])
    web = Web("light", ".githubcom")
    rm = Removable([1, 2, 3], 1)
    session = Session("user", ".githubcom")
    print(ds, loc, web, rm, session, sep="\n")
