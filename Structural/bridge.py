from abc import ABC, abstractmethod


# Realisation interface
class Device(ABC):
    def __init__(self):
        self._isEnabled = None
        self._volume = self._prevVolume = self._channel = self._channelsAmount = 0

    @property
    def isEnabled(self) -> bool:
        return self._isEnabled

    @isEnabled.setter
    def isEnabled(self, value: bool):
        self._isEnabled = value

    def enable(self):
        self.isEnabled = True

    def disable(self):
        self.isEnabled = False

    @property
    def volume(self) -> int:
        return self._volume

    @volume.setter
    def volume(self, volume: int):
        self._volume = volume

    @property
    def prevVolume(self) -> int:
        return self._prevVolume

    @prevVolume.setter
    def prevVolume(self, volume: int):
        self._prevVolume = volume

    @property
    def channelsAmount(self) -> int:
        return self._channelsAmount

    @channelsAmount.setter
    def channelsAmount(self, amount: int):
        self._channelsAmount = amount

    @property
    def channel(self) -> int:
        return self._channel

    @channel.setter
    def channel(self, channel: int):
        self._channel = channel


# Concrete Realisations
class Radio(Device):
    def __init__(self):
        super().__init__()
        self._channelsAmount = 19


class TV(Device):
    def __init__(self):
        super().__init__()
        self._channelsAmount = 31


# Abstractions
class Remote:
    def __init__(self, device: Device):
        self._device = device

    def togglePower(self):
        print(f'{"_" * 75}\ntogglePower()')
        if self._device.isEnabled:
            self._device.disable()
        else: self._device.enable()
        print(f"{self._device.__class__.__name__} is turned {'on' if self._device.isEnabled else 'off'} now"
              f"\n{'_' * 75}")

    def volumeUp(self):
        print(f'{"-" * 10}\nvolumeUp()')
        print(f'Current volume: {self._device.volume}', end="")
        if self._device.volume < 100:
            self._device.volume += 10
            print(f'\t - \tVolume is up and now: {self._device.volume}')
        else: print('\t - \tAlready maximum volume')

    def volumeDown(self):
        print(f'{"-" * 10}\nvolumeDown()')
        print(f'Current volume: {self._device.volume}', end="")
        if self._device.volume:
            self._device.volume += 10
            print(f'\t - \tVolume is down and now: {self._device.volume}')
        else: print('\t - \tAlready minimum volume')

    def nextChannel(self):
        print(f'{"-" * 10}\nnextChannel()')
        print(f'Current channel: {self._device.channel}', end="")
        if self._device.channel < self._device.channelsAmount:
            self._device.channel += 1
        else: self._device.channel = 0
        print(f'\t - \tNext channel now: {self._device.channel}')

    def previousChannel(self):
        print(f'{"-" * 10}\npreviousChannel()')
        print(f'Current channel: {self._device.channel}', end="")
        if self._device.channel:
            self._device.channel -= 1
        else: self._device.channel = self._device.channelsAmount
        print(f'\t - \tPrevious channel now: {self._device.channel}')


class AdvancedRemote(Remote):
    def mute(self):
        print(f'{"-" * 10}\nmute()')
        print(f'Current volume: {self._device.volume}', end="")
        if self._device.volume:
            self._device.prevVolume = self._device.volume
            self._device.volume = 0
        else: self._device.volume = self._device.prevVolume
        print(f'\t - \tVolume now: {self._device.volume}')


# Client code
def client_code(remote: Remote):
    remote.togglePower()

    remote.previousChannel()
    remote.nextChannel()

    remote.volumeDown()
    remote.volumeUp()
    remote.volumeUp()


if __name__ == '__main__':
    radioSimpleRemote = Remote(Radio())
    tvAdvancedRemote = AdvancedRemote(TV())

    client_code(radioSimpleRemote)
    radioSimpleRemote.togglePower()

    print('\n')

    client_code(tvAdvancedRemote)
    tvAdvancedRemote.mute()
    tvAdvancedRemote.mute()
    tvAdvancedRemote.togglePower()
