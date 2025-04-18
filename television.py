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

    def power(self):
        self.status = not self.status

    def mute(self):
        if self.status:
            self.muted = not self.muted

    def channel_up(self):
        if self.status:
            current_channel = self.channel

            if current_channel + 1 > Television.MAX_CHANNEL:
                self.channel = Television.MIN_CHANNEL
            else:
                self.channel += 1

    def channel_down(self):
        if self.status:
            current_channel = self.channel

            if current_channel - 1 < Television.MIN_CHANNEL:
                self.channel = Television.MAX_CHANNEL
            else:
                self.channel -= 1

    def volume_up(self):
        if self.status:
            if self.volume == Television.MAX_VOLUME:
                self.muted = False
            else:
                self.muted = False
                self.volume += 1

    def volume_down(self):
        if self.status:
            if self.volume == Television.MIN_VOLUME:
                self.muted = False
            else:
                self.muted = False
                self.volume -= 1

    def __str__(self):
        display_vol = self.volume
        if self.muted:
            display_vol = 0

        return f"Power - {self.status}, Channel - {self.channel}, Volume - {display_vol}."