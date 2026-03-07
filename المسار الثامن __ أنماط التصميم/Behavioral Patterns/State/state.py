from __future__ import annotations
from abc import ABC, abstractmethod

class AudioPlayer:
    def __init__(self) -> None:
        self.state: State = ReadyState(self)

    def change_state(self, state):
        self.state = state

    def click_lock(self):
        self.state.click_lock()

    def click_play(self):
        self.state.click_play()

    def click_next(self):
        self.state.click_next()

    def click_previous(self):
        self.state.click_previous()

    def next_song(self):
        print("Next Song")

    def previous_song(self):
        print("Previous Song")

    def fast_forward(self, value):
        print("Fast Forward", value)

    def rewind(self, value):
        print("Rewind", value)


class State(ABC):
    def __init__(self, player: AudioPlayer):
        self.player = player

    @abstractmethod
    def click_lock(self):
        pass

    @abstractmethod
    def click_play(self):
        pass

    @abstractmethod
    def click_next(self):
        pass

    @abstractmethod
    def click_previous(self):
        pass



class LockedState(State):
    def __init__(self, player: AudioPlayer):
        super().__init__(player)

    def click_lock(self):
        print("Audio is already locked")

    def click_play(self):
        print("ClickPlay from LockedState, Do Nothing")

    def click_next(self):
        print("ClicNext from LockedState, Do Nothing")

    def click_previous(self):
        print("ClickPrevious from LockedState, Do Nothing")


class ReadyState(State):
    def __init__(self, player: AudioPlayer):
        super().__init__(player)

    def click_lock(self):
        print("ClickLock from ReadyState")
        self.player.change_state(LockedState(self.player))

    def click_play(self):
        print("ClickPlay from ReadyState")
        self.player.change_state(PlayingState(self.player))

    def click_next(self):
        print("ClicNext from ReadyState")
        self.player.next_song()

    def click_previous(self):
        print("ClickPrevious from ReadyState")
        self.player.previous_song()

class PlayingState(State):
    def __init__(self, player: AudioPlayer):
        super().__init__(player)

    def click_lock(self):
        print("ClickLock from PlayingState")
        self.player.change_state(LockedState(self.player))

    def click_play(self):
        print("ClickPlay from PlayingState")
        self.player.change_state(ReadyState(self.player))

    def click_next(self):
        print("ClicNext from PlayingState")
        if True:
            self.player.next_song()
        else:
            self.player.fast_forward(5)

    def click_previous(self):
        print("ClickPrevious from PlayingState")
        if True:
            self.player.previous_song()
        else:
            self.player.rewind(5)


if __name__ == "__main__":
    audio_player = AudioPlayer()

    audio_player.click_play()
    audio_player.click_next()
    audio_player.click_previous()
    audio_player.click_lock()

    playing_state = PlayingState(audio_player)
    audio_player.change_state(playing_state)
    audio_player.click_play()
    audio_player.click_next()
    audio_player.click_previous()
    audio_player.click_lock()

    locked_state = LockedState(audio_player)
    audio_player.change_state(locked_state)
    audio_player.click_play()
    audio_player.click_next()
    audio_player.click_previous()
    audio_player.click_lock()

