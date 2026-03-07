from __future__ import annotations
from abc import ABC, abstractmethod

class Device(ABC):
    @abstractmethod
    def is_enable(self):
        pass

    @abstractmethod
    def enable(self):
        pass

    @abstractmethod
    def disable(self):
        pass

    @abstractmethod
    def get_volume(self):
        pass

    @abstractmethod
    def set_volume(self, precent):
        pass

    @abstractmethod
    def get_channel(self):
        pass

    @abstractmethod
    def set_channel(self, channel):
        pass


class TV(Device):

    def __init__(self):
        self._enable = False
        self._volume = 50
        self._channel = 1

    def is_enable(self):
        return self._enable

    def enable(self):
        self._enable = True
        print("TV: Power On")

    def disable(self):
        self._enable = False
        print("TV: Power Off")

    def get_volume(self):
        return self._volume

    def set_volume(self, precent):
        self._volume = max(0, min(100, precent))
        print(f"TV: Volume set to {self._volume}")

    def get_channel(self):
        return self._channel

    def set_channel(self, channel):
        self._channel = max(1, channel)
        print(f"TV: Channel set to {self._channel}")


class Radio(Device):

    def __init__(self):
        self._enable = False
        self._volume = 30
        self._channel = 5

    def is_enable(self):
        return self._enable

    def enable(self):
        self._enable = True
        print("Radio: Power On")

    def disable(self):
        self._enable = False
        print("Radio: Power Off")

    def get_volume(self):
        return self._volume

    def set_volume(self, precent):
        self._volume = max(0, min(100, precent))
        print(f"Radio: Volume set to {self._volume}")

    def get_channel(self):
        return self._channel

    def set_channel(self, channel):
        self._channel = max(1, channel)
        print(f"Radio: Channel set to {self._channel}")

class RemoteControl:
    def __init__(self, device: Device):
        self._device = device

    def toggle_power(self):
        if self._device.is_enable():
            self._device.disable()
        else:
            self._device.enable()

    def volume_up(self):
        new_vol = self._device.get_volume() + 10
        self._device.set_volume(new_vol)

    def volume_down(self):
        new_vol = self._device.get_volume() - 10
        self._device.set_volume(new_vol)

    def channel_up(self):
        new_channel = self._device.get_channel()
        self._device.set_channel(new_channel + 1)

    def channel_down(self):
        new_channel = self._device.get_channel()
        self._device.set_channel(new_channel - 1)

class AdvancedRemote(RemoteControl):
    def mute(self):
        self._device.set_volume(0)
        print("Device Muted.")


if __name__ == "__main__":
    tv = TV()
    remote = RemoteControl(tv)
    remote.toggle_power()
    remote.volume_up()
    remote.channel_down()
    remote.toggle_power()
    print('\n')
    radio = Radio()
    remoteR = AdvancedRemote(radio)
    remoteR.toggle_power()
    remoteR.channel_up()