from __future__ import annotations
from abc import ABC, abstractmethod

class RemoteControl:
    def __init__(self, device: Device):
        self._device = device

    def toggle_power(self):
        if self._device.is_enable():
            self._device.disable()
        else:
            self._device.enable()

    def volume_down(self):
        self._device.set_volume(self._device.get_volume() - 10)

    def volume_up(self):
        self._device.set_volume(self._device.get_volume() + 10)

    def channel_down(self):
        self._device.set_channel(self._device.get_channel() - 1)

    def channel_up(self):
        self._device.set_channel(self._device.get_channel() + 1)


class AdvanceRemote(RemoteControl):
    def mute(self):
        self._device.set_volume(0)
        print('Device Muted.')
        # add more features


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
    def is_enable(self):
        print("from Tv, isEnable")
        return True

    def enable(self):
        print("from Tv, enable")

    def disable(self):
        print("from Tv, Disable")

    def get_volume(self):
        return "From Tv, Volume"

    def set_volume(self, precent):
        print("From Tv, SetVolume")

    def get_channel(self):
        return "From Tv, Channel"

    def set_channel(self, channel):
        print("From Tv, setChannel")


class Radio(Device):
    def is_enable(self):
        print("from Radio, isEnable")
        return True

    def enable(self):
        print("from Radio, enable")

    def disable(self):
        print("from Radio, Disable")

    def get_volume(self):
        return "From Radio, Volume"

    def set_volume(self, precent):
        print("From Radio, SetVolume")

    def get_channel(self):
        return "From Radio, Channel"

    def set_channel(self, channel):
        print("From Radio, SetChannel")


if __name__ == "__main__":
    tv = TV()
    remote = RemoteControl(tv)
    remote.toggle_power()

    radio = Radio()
    remote = AdvanceRemote(radio)
    remote.toggle_power()