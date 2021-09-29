# inheritance

class UsualString:
    def request(self) -> str:
        return "UsualString: The default strings behavior."


class BytesString:
    @staticmethod
    def specific_request() -> list:
        return [ord(letter) for letter in "Decoded bytes string."]


class Adapter(UsualString, BytesString):
    def request(self) -> str:
        return f"Adapter: {bytes(self.specific_request()).decode(encoding='utf-8')}"


def client_code(string: UsualString) -> None:
    print(string.request(), end="\n")


if __name__ == "__main__":
    print("Client: I can work just fine with the UsualString objects:")
    usual_string = UsualString()
    client_code(usual_string)
    print("")

    bites_string = BytesString()
    print(f"Client: The BytesString class can't be represented as a {usual_string.__class__.__name__}.\n"
          "See, I don't understand it:")
    print(f"BytesString: {bites_string.specific_request()}", end="\n\n")

    print("Client: But I can work using the Adapter:")
    adapter = Adapter()
    client_code(adapter)
