class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        self.status = False
        self.muted = False
        self.volume = Television.MIN_VOLUME
        self.channel = Television.MIN_CHANNEL

    def power(self) -> None:
        """Toggles the status attribute"""
        self.status = not self.status

    def mute(self) -> None:
        """Toggles the muted attribute if the status attribute is set to True"""
        if self.status:
            self.muted = not self.muted

    def channel_up(self) -> None:
        """Increments the channel attribute, wrapping to the minimum if it would exceed the default maximum"""
        if self.status:
            current_channel = self.channel

            if current_channel + 1 > Television.MAX_CHANNEL:
                self.channel = Television.MIN_CHANNEL
            else:
                self.channel += 1

    def channel_down(self) -> None:
        """Decrements the channel attribute, wrapping to the maximum if it would exceed the default minimum"""
        if self.status:
            current_channel = self.channel

            if current_channel - 1 < Television.MIN_CHANNEL:
                self.channel = Television.MAX_CHANNEL
            else:
                self.channel -= 1

    def volume_up(self) -> None:
        """Increments the volume attribute up to but not exceeding the default maximum, unmutes if muted"""
        if self.status:
            self.muted = False
            if self.volume < Television.MAX_VOLUME:
                self.volume += 1

    def volume_down(self) -> None:
        """Decrements the volume attribute down to but not exceeding the default minimum, unmutes if muted"""
        if self.status:
            self.muted = False
            if self.volume > Television.MIN_VOLUME:
                self.volume -= 1

    def __str__(self) -> str:
        """Returns a summary of the current status of the class instance as a string"""
        display_vol = self.volume
        if self.muted:
            display_vol = 0

        return f"Power = {self.status}, Channel = {self.channel}, Volume = {display_vol}."