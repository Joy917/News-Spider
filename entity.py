class Article:
    def __init__(self):
        self.title = ""
        self.title_cn = ""
        self.url = ""
        self.date = ""
        self.text = ""
        self.text_cn = ""

    def __str__(self):
        return self.title + "===" + self.url + "===" + self.date

    def __hash__(self):
        return hash(self.url)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False
