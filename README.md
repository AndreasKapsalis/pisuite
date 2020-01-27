# Installation
Sample script intended to run on a RaspberryPi with the camera and the KY-038 sound sensor modules installed. 
Create a virtualenv with a Python3 version and install the requirements:
```
pip install -r requirements.txt
``` 
Create a `.env` file in the folder root and populate it with the following variables:
```
PIN= #The GPIO pin which the KY-038 module is connected
GPIO_HOST= #The host where the GPIOd daemon is running
TELEGRAM_API_TOKEN= # The telegram bot API token. See https://core.telegram.org/bots/api for more info
TELEGRAM_CHAT_ID= # The id of the chat to send updates to
```
Then run the application with:
```
python app.py
```
This starts the main thread which is a telegram bot command handler.

You can terminate the program with a simple keyboard interrupt `(Ctrl-C)`
# Commands
If you have set up a telegram bot you can issue the following commands:
`/start_sound_sensor` -- Enables the sound sensor, which sums the number of times it detected any sound within a minute and sends an update to a channel
`/stop_sound_sensor` -- Disables the sound sensor
`/photo` -- Takes a photo 

# TODO
- Enable capture of video
- Add support for motion and light sensors