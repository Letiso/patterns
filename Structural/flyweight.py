import json


class Flyweight:
    def __init__(self, internal_state: list):
        self._internalState = internal_state

    def getStatus(self, external_state: list):
        internal_state = json.dumps(self._internalState)
        external_state = json.dumps(external_state)

#         print(f"""{'*' * 40}
# self._internalState: {self._internalState}
# json.dumps(self._internalState): {json.dumps(self._internalState)}
# json.loads(self._internalState): {'["BMW", "M5", "red"]'}
# {'*' * 40}
# """)

        print(f"\nFlyweights shared {internal_state} fields, but {external_state} fields is unique for every object")


class FlyweightFactory:
    def __init__(self, initial_flyweights: list) -> None:
        self._flyweights = dict()

        for state in initial_flyweights:
            self._flyweights[self.getKey(state)] = Flyweight(state)

    @staticmethod
    def getKey(state: list) -> str:
        return '_'.join(sorted(state))

    def getFlyweight(self, internal_state) -> Flyweight:
        key = self.getKey(internal_state)

        if self._flyweights.get(key):
            print('Reusing existing flyweight...')
        else:
            print('Creating new flyweight...')
            self._flyweights[key] = Flyweight(internal_state)

        return self._flyweights[key]

    def listFlyweights(self) -> None:
        print(f"{'_' * 70}\nFlyweights factory contains {len(self._flyweights)} templates:\n")
        for index, flyweight in enumerate(self._flyweights): print(f"{index + 1}: {flyweight}")
        print('_' * 70)


def addCar_to_PoliceDataBase(factory: FlyweightFactory,
                             plates: str, owner: str,
                             brand: str, model: str,  color: str) -> None:

    print(f"\nClient code: Adding a car to police Data Base...")
    flyweight = factory.getFlyweight([brand, model, color])
    flyweight.getStatus([plates, owner])


if __name__ == '__main__':
    carTemplatesFactory = FlyweightFactory([
        ["Chevrolet", "Camaro2018", "pink"],
        ["Mercedes Benz", "C300", "black"],
        ["Mercedes Benz", "C500", "red"],
        ["BMW", "M5", "red"],
        ["BMW", "X6", "white"],
    ])

    carTemplatesFactory.listFlyweights()

    addCar_to_PoliceDataBase(carTemplatesFactory, "CL234IR", "James Doe", "BMW", "M5", "red")

    addCar_to_PoliceDataBase(carTemplatesFactory, "CL234IR", "James Doe", "BMW", "X1", "red")

    carTemplatesFactory.listFlyweights()
