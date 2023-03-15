# Simple serial logger + http server

## Requirements

1. Arduino running `main-weather.ino` from [this repo](https://github.com/tocococa/arduino-weather-station.git).

2. Linux machine (Raspberry Pi Model 1 in my case).

## Execution

1. Compile the http server with `make` at `./server/darkhttpd`, this is a fork from [darkhttpd](https://github.com/emikulic/darkhttpd) by emikulic.

2. Run `nohup python3 logger.py &` to start the logger in the background.

3. Run `(./darkhttpd ./public_index/ --port 8081 &)` to start the server and serve on `localhost:8081`.

4. Optional: run Ngrok with `./ngrok http 8081` to expose the server, or use whatever you prefer.

## Observations

The logger will try and choose between a serial port from windows or unix-like systems, if this fails, you will get an error message. Fix the port yourself.
