class BeanProcess:
    def __init__(self, name: str):
        self.short_name = name


class BeanProcesses:
    WASHED = BeanProcess('washed')
    HONEY = BeanProcess('honey')
    NATURAL = BeanProcess('natural')
    OTHER = BeanProcess('other')
