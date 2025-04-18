from pytest import *
from television import Television

# Defaults:
# Power = False
# Muted = False
# MIN_VOLUME = 0
# MAX_VOLUME = 2
# MIN_CHANNEL = 0
# MAX_CHANNEL = 3

def test_power_toggle():
    tv = Television()
    assert not tv.status
    tv.power()
    assert tv.status
    tv.power()
    assert not tv.status

def test_mute_toggle():
    tv = Television()
    tv.power()
    assert not tv.muted
    tv.mute()
    assert tv.muted
    tv.mute()
    assert not tv.muted

def test_volume_functions():
    tv = Television()
    tv.power()

    assert tv.volume == Television.MIN_VOLUME
    tv.volume_up()
    assert tv.volume == 1
    tv.volume_up()
    assert tv.volume == Television.MAX_VOLUME
    tv.volume_up()
    assert tv.volume == Television.MAX_VOLUME

    tv.volume_down()
    assert tv.volume == 1
    tv.volume_down()
    assert tv.volume == Television.MIN_VOLUME
    tv.volume_down()
    assert tv.volume == Television.MIN_VOLUME

def test_channel_functions():
    tv = Television()
    tv.power()

    tv.channel = Television.MAX_CHANNEL
    tv.channel_up()
    assert tv.channel == Television.MIN_CHANNEL

    tv.channel = Television.MIN_CHANNEL
    tv.channel_down()
    assert tv.channel == Television.MAX_CHANNEL

def test_volume_mute_interact():
    tv = Television()
    tv.power()
    tv.mute()

    assert tv.muted
    tv.volume_down()
    assert not tv.muted

    tv.volume_up()
    tv.mute()
    tv.volume_down()
    assert not tv.muted

    tv.volume = Television.MAX_VOLUME
    tv.mute()
    assert tv.muted
    tv.volume_up()
    assert not tv.muted

    tv.volume_down()
    tv.mute()
    assert tv.muted
    tv.volume_up()
    assert not tv.muted

def test_volume_when_off():
    tv = Television()
    original_volume = tv.volume
    tv.volume_up()
    assert original_volume == tv.volume

    tv.volume = Television.MIN_VOLUME
    original_volume = tv.volume
    tv.volume_down()
    assert original_volume == tv.volume

def test_mute_when_off():
    tv = Television()
    mute_status = tv.muted
    assert not tv.muted
    tv.mute()
    assert not tv.muted

def test_str_func():
    tv = Television()

    expected_str = "Power = False, Channel = 0, Volume = 0."
    assert str(tv) == expected_str

    tv.power()
    tv.channel_up()
    tv.channel_up()
    tv.volume_up()

    expected_str = "Power = True, Channel = 2, Volume = 1."
    assert str(tv) == expected_str

    tv.channel_up()
    tv.channel_up()
    tv.channel_up()
    tv.volume_down()
    tv.volume_down()

    expected_str = "Power = True, Channel = 1, Volume = 0."
    assert str(tv) == expected_str

    tv.power()
    tv.volume_up()
    tv.channel_down()

    expected_str = "Power = False, Channel = 1, Volume = 0."
    assert str(tv) == expected_str

    tv.power()
    tv.volume_up()
    tv.volume_up()
    tv.volume_up()
    tv.channel_down()
    tv.channel_down()

    expected_str = "Power = True, Channel = 3, Volume = 2."
    assert str(tv) == expected_str


    tv.mute()

    expected_str = "Power = True, Channel = 3, Volume = 0."
    assert str(tv) == expected_str

    tv.power()
    tv.mute()

    expected_str = "Power = False, Channel = 3, Volume = 0."
    assert str(tv) == expected_str