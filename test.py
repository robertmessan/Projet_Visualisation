class WordCount:
    def __init__(self, text: str):
        self.text = text
        self.word_list = self.preprocess()

    def __str__(self):
        return self.text

    @staticmethod
    def from_file(file_name):
        with open(file_name, 'r') as file:
            text = ''.join(file.readlines())
        return WordCount(text)

    # Just for fun
    @staticmethod
    def write_in_file(file_name):
        with open(file_name, 'a+') as file:
            file.write("I love creating great algorithms that explore the black golden")
        return file

    def preprocess(self):
        text = self.text.lower()
        text = text.replace('.', ' ')
        text = text.replace('\n', ' ')
        words = text.split(' ')

        words = [word for word in words if word]
        return words

    def __len__(self):
        return len(set(self.word_list))

    def count_words(self):
        word_count = {}
        for word in self.word_list:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
        return word_count

    def get_most_common_word(self):
        word_count = self.count_words()
        return max(word_count, key=word_count.get)


def main():
    text = "The little boy was called Tom. Tom was happy because the dog was happy."
    wc = WordCount(text)
    print(wc)

    wc_from_file = WordCount.from_file("~/Robert.txt")
    print(wc_from_file)
    change = WordCount.write_in_file("~/Robert.txt")
    print(change)

    print("Length:", len(wc))
    print("Word count:", wc.count_words())
    print("Most common word:", wc.get_most_common_word())


if __name__ == "__main__":
    main()
