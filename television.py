class Television:
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        """
        Initializes a new Television instance with default settings.
        """
        self._status: bool = False
        self._muted: bool = False
        self._volume: int = Television.MIN_VOLUME
        self._channel: int = Television.MIN_CHANNEL

    def power(self) -> None:
        """
        Toggles the power status of the television.
        """
        self._status = not self._status

    def mute(self) -> None:
        """
        Mutes or unmutes the television.
        """
        self._muted = not self._muted

    def channel_up(self) -> None:
        """
        Increases the channel by one. Loops to the minimum channel if maximum is exceeded.
        """
        if self._status:
            if self._channel == Television.MAX_CHANNEL:
                self._channel = Television.MIN_CHANNEL
            else:
                self._channel += 1

    def channel_down(self) -> None:
        """
        Decreases the channel by one. Loops to the maximum channel if minimum is surpassed.
        """
        if self._status:
            if self._channel == Television.MIN_CHANNEL:
                self._channel = Television.MAX_CHANNEL
            else:
                self._channel -= 1

    def volume_up(self) -> None:
        """
        Increases the volume by one unless muted.
        """
        if self._status and not self._muted:
            if self._volume < Television.MAX_VOLUME:
                self._volume += 1

    def volume_down(self) -> None:
        """
        Decreases the volume by one unless muted.
        """
        if self._status and not self._muted:
            if self._volume > Television.MIN_VOLUME:
                self._volume -= 1

    def __str__(self) -> str:
        """
        Returns a string representation of the television's current state.
        """
        return f"Power = {self._status}, Channel = {self._channel}, Volume = {self._volume}"
