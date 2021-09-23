from abc import ABC, abstractmethod


class Device(ABC):
    def __init__(self):
        self._isEnabled = self._channelsCount = None
        self._volume = self._channel = 0

    @property
    def isEnabled(self) -> bool:
        return self._isEnabled

    @isEnabled.setter
    def isEnabled(self, value: bool):
        self._isEnabled = value

    def enable(self):
        self._isEnabled = True

    def disable(self):
        self._isEnabled = False

    @property
    def channelsCount(self):
        return self._channelsCount

    @channelsCount.setter
    def channelsCount(self, count: int):
        self._channelsCount = count

    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, volume: int):
        self._volume = volume

    @abstractmethod
    def getChannel(self): pass

    @abstractmethod
    def setChannel(self, channel: int): pass


class Radio(Device):
    def __init__(self):
        super().__init__()
        self._channelsCount = 20

    def getVolume(self):
        return self._volume

    def setVolume(self, volume: int):
        self._volume = volume

    def getChannel(self):
        return self._channel

    def setChannel(self, channel: int):
        self._channel = channel


class TV(Device):
    def __init__(self):
        super().__init__()
        self._channelsCount = 31

    def getVolume(self):
        return self._volume

    def setVolume(self, volume: int):
        self._volume = volume

    def getChannel(self):
        return self._channel

    def setChannel(self, channel: int):
        self._channel = channel


class Remote:
    def __init__(self, device: Device):
        self._device = device

    def togglePower(self):
        if self._device.isEnabled:
            self._device.disable()
        else: self._device.enable()
        print(f"{self._device.__class__.__name__} is turned {'on' if self._device.isEnabled else 'off'} now")

    def volumeUp(self):
        if self._device.volume < 100:
            self._device.volume += 10
            print('Volume is up')
        else: print('Maximal volume')

    def volumeDown(self):
        if self._device.volume > 0:
            self._device.volume += 10
            print('Volume is down')
        else: print('Minimal volume')

    def nextChannel(self):
        if (channel := self._device.getChannel()) <= self._device.channelsCount:
            self._device.setChannel(channel + 1)
        else: self._device.setChannel(0)
        print()

    def previousChannel(self):
        if (channel := self._device.getChannel()) >= 0:
            self._device.setChannel(channel - 1)
        else: self._device.setChannel(self._device.channelsCount)


def client(remote: Remote):
    [remote.togglePower()
     for loop in range(3)]

    remote.previousChannel()
    remote.nextChannel()


if __name__ == '__main__':
    client(Remote(Radio()))
