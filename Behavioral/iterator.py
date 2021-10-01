from collections.abc import Iterable, Iterator


class AlphabeticalOrderIterator(Iterator):
    def __init__(self, collection: list, reverse: bool = False) -> None:
        self._collection: list = sorted(collection)
        self._reverse: bool = reverse
        self._position: int = 0 if not reverse else -1

    def __next__(self) -> any:
        try:
            value = self._collection[self._position]
            self._position += 1 if not self._reverse else -1
        except IndexError:
            raise StopIteration

        return value


class WordsCollection(Iterable):
    def __init__(self, collection: list) -> None:
        self._collection = collection

    def __iter__(self) -> AlphabeticalOrderIterator:
        return AlphabeticalOrderIterator(self._collection)

    @property
    def collection(self) -> list:
        return self._collection

    def reversedIter(self) -> AlphabeticalOrderIterator:
        return AlphabeticalOrderIterator(self._collection, True)


if __name__ == '__main__':
    wordsCollection = WordsCollection(['First word', 'Second word', 'Third word', 'Fourth word', 'Fifth word'])
    def underline(count: int): return print('_' * count)

    def clientCode(words: WordsCollection) -> None:
        underline(30)
        print("Alphabetical order:\n\n" + "\n".join(words))
        underline(30)

        print("Reversed alphabetical order:\n\n" + "\n".join(words.reversedIter()))
        underline(30)

    clientCode(wordsCollection)

