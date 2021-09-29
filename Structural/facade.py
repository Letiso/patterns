from random import randrange


class TextSubsystem:
    def __init__(self):
        self._initMessage = 'Text system'

    def init(self) -> str:
        return f"{self._initMessage} is ready\n"

    def generateText(self) -> str:
        return f"{self._initMessage}: generated text"


class NumbersSubsystem:
    def __init__(self):
        self._initNumbers = 'Numbers system'
        self._numbersRange = 15

    def init(self) -> str:
        return f"{self._initNumbers} is ready\n"

    def generateNumbers(self) -> list:
        return [randrange(self._numbersRange) for counter in range(self._numbersRange)]


class GeneratorsFacade:
    def __init__(self, text_generator: TextSubsystem = None, numbers_generator: NumbersSubsystem = None):
        self._textGenerator = text_generator or TextSubsystem()
        self._numbersGenerator = numbers_generator or NumbersSubsystem()

    def generateData(self) -> list:
        result = list()

        for generator in self._textGenerator, self._numbersGenerator:
            print(generator.init(), end="")

        result.append('\nself._textGenerator.generateText()')
        result.append(
            f"Numbers system: {' - '.join([str(number) for number in self._numbersGenerator.generateNumbers()])}")

        return result


def client_code(facade: GeneratorsFacade) -> None:
    for generatedData in facade.generateData():
        print(generatedData, end="\n\n")


if __name__ == '__main__':
    generatorsFacade = GeneratorsFacade()

    client_code(generatorsFacade)
