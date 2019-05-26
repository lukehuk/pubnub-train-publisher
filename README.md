# The PubNub Train - Publisher
This is the publisher component of a simple PubNub demonstration project inspired by a locomotive tracking system.

To see the subscriber component of this project visit [this project](https://github.com/lukehuk/pubnub-train-subscriber).

To read more about the background and motivation of this project visit [this article](https://medium.com/p/c90ea36fffce)

## Getting Started
### Prerequisites
This project requires:
* A Raspberry Pi running Python 3. If you need to set up your Pi follow the following steps:
  1. Install the latest (Raspbian OS)[https://www.raspberrypi.org/downloads/raspbian/] locally on your computer
  2. Flash the OS image onto a microSD card. You can use a simple applicaiton such as (Etcher)[https://www.balena.io/etcher/]
  3. Using your computer file system add a blank file `ssh` at the top directory of the microSD card to enable SSH
  4. Put the microSD card into your Pi and use
  5. If you want to use your Pi without peripherals follow the steps outlined on (this lifehacker guide)[https://lifehacker.com/how-to-control-your-raspberry-pi-from-any-computer-usin-1788592777]
* A hardware setup that can interact with the Raspberry Pi GPIO pins. This could just be a simple button, but for the train setup used in my project refer to the article linked in the introduction. 

### Installing
In order to use the application you will need publisher and subscriber PubNub keys. Free registration is possible at [https://dashboard.pubnub.com/signup](https://dashboard.pubnub.com/signup) 

The API keys should be added as the `PUBNUB_SUBSCRIBE_KEY` and `PUBNUB_PUBLISH_KEY` constants:

```
# PubNub Configuration
PUBNUB_PUBLISH_KEY = ""
PUBNUB_SUBSCRIBE_KEY = ""
```

The `PUBNUB_CHANNEL_NAME` constant can be provided in the same way, a default of `train-demo` is given.

The GPIO pins used in the hardware setup to track the train location needs to be included in the `ACTIVE_PINS` array. For example, if GPIO pins `8` and `10` were used:

```
ACTIVE_PINS = [8, 10]
```

### Running
One started, the script will begin listening for GPIO events. If wired correctly, when a button is released (after be pressed by a passing train), a PubNub message publish is triggered.

## Built With
* [PubNub](https://www.pubnub.com/) - Realtime messaging platform 
* [Raspberry Pi](https://www.raspberrypi.org) - A small, cheap programmable computer

## License
This project is licensed under the Apache-2.0 License