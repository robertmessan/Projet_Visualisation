class WordCount:
    def __init__(self, text):
        self.text = text

    @staticmethod
    def tostring(self):
        return self.text

    def from_file(self, nom_fi):
        self.text += nom_fi
        return self


if __name__ == '__main__':
    test = WordCount("The little boy was called Tom. Tom was happy because the dog was happy.")
    print(test.tostring(test))
    file = "This boy is me!"
    test= test.from_file(file)
    print(test.tostring(test))
