import datetime
import sys
import RPi.GPIO as GPIO
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub

# PubNub Configuration
PUBNUB_PUBLISH_KEY = ""
PUBNUB_SUBSCRIBE_KEY = ""
PUBNUB_CHANNEL_NAME = "train-demo"
# The GPIO pins that are being used for train tracking
ACTIVE_PINS = []
# Voltage fluctuations (jitter) can occur when pressing/releasing buttons/switches. Bounce time
# avoids false readings by ignoring voltage changes for a period of time after an initial event.
BOUNCETIME_MS = 200


# Called when a PubNub publish completed, prints information indicating the publish completion status
def publish_callback(result, status):
    if status.is_error():
        print("ERROR" + status.error_data.information)
    else:
        print("SUCCESS: " + str(result.timetoken))


# Handles the publish of a PubNub message
def publish_message(triggered_pin, is_rising):
    pubnub.publish().channel(PUBNUB_CHANNEL_NAME).message([triggered_pin, is_rising]).pn_async(publish_callback)


# Called when a Raspberry Pi GPIO pin changes from a high voltage to a low voltage state. Publishes a PubNub message
def falling_callback(triggered_pin):
    print("Button " + str(triggered_pin) + " was released " + str(datetime.datetime.now()))
    sys.stdout.flush()  # This avoids messages in quick succession appearing jumbled in the log
    publish_message(triggered_pin, False)


# Initialise PubNub
pnconfig = PNConfiguration()
pnconfig.subscribe_key = PUBNUB_SUBSCRIBE_KEY
pnconfig.publish_key = PUBNUB_PUBLISH_KEY
pnconfig.ssl = False
pubnub = PubNub(pnconfig)

# Initialise GPIO
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BOARD)
for pin in ACTIVE_PINS:
    print("Setting up pin: " + str(pin))
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(pin, GPIO.FALLING, callback=falling_callback, bouncetime=BOUNCETIME_MS)

# Waits for keyboard return carriage before terminating the application
message = input("Running. Press enter to quit\n\n")
GPIO.cleanup()
