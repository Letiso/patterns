import json


class Flyweight:
    def __init__(self, internal_state: list):
        self._internalState = internal_state

    def getCarTemplate(self) -> list:
        return self._internalState


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


class CarRegisterCard:
    def __init__(self, internal_state: Flyweight, external_state: list):
        self._internalState = internal_state
        self._externalState = external_state

    def __str__(self):
        internal_state = json.dumps(self._internalState.getCarTemplate())
        external_state = json.dumps(self._externalState)

        #         print(f"""{'*' * 40}
        # self._internalState: {self._internalState}
        # json.dumps(self._internalState): {json.dumps(self._internalState)}
        # json.loads(self._internalState): {'["BMW", "M5", "red"]'}
        # {'*' * 40}
        # """)

        return f"Car 'united' data: {external_state}, {internal_state}"
        # return f"\nFlyweight shared {internal_state} fields, " \
        #        f"but {external_state} fields is unique for every object"


class PoliceDataBase:
    def __init__(self):
        self._dataBase = dict()
        self._flyweightFactory = FlyweightFactory(
            [["Chevrolet", "Camaro2018", "pink"],
             ["Mercedes Benz", "C300", "black"],
             ["Mercedes Benz", "C500", "red"],
             ["BMW", "M5", "red"],
             ["BMW", "X6", "white"], ])

    def addCar_to_Register(self, plates: str, owner: str,
                           brand: str, model: str, color: str) -> None:
        print(f"\nClient code: Adding a car to police Data Base...\n{plates, owner, brand, model, color}")
        flyweight = self._flyweightFactory.getFlyweight([brand, model, color])

        self._dataBase[plates] = CarRegisterCard(flyweight, [plates, owner])

    def getCar(self, plates: str):
        print(f"\nGet a car by query '{plates}'")
        print(self._dataBase[plates])

    def getAllCars(self):
        print(f"{'*' * 75}\nList of every car card in the data base...")
        for carPlate, carCard in self._dataBase.items():
            print(f"\nCar plate:{carPlate}\n{str(carCard)}")
        print('*' * 75)


if __name__ == '__main__':
    policeCarRegister = PoliceDataBase()

    def client_code(*car_data):
        policeCarRegister.addCar_to_Register(*car_data)
        policeCarRegister._flyweightFactory.listFlyweights()


    existing_car_template = ("CL234IR", "James Doe", "BMW", "M5", "red")
    not_known_car_template = ("CL234IB", "Sue Doe", "BMW", "X1", "red")

    client_code(*existing_car_template)

    client_code(*not_known_car_template)

    policeCarRegister.getAllCars()

    policeCarRegister.getCar("CL234IR")
