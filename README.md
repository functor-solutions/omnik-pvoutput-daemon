# Omnik PVOutput Daemon
A simple Python daemon which can be used as a remote server of the Omnik Solar Inverter. The
daemon can easily run on a Synology NAS.

## Configuration of the Daemon
Copy the `config.ini.template` file to `config.ini` and fill in the necessary values.

Each *section* inside the configuration file represents exactly one Omnik Solar Inverter
which can push data towards this daemon.

For each Solar Inverter the following settings are available:
* `serial`: the serial number of the Omnik Solar Inverter.
* `systemId`: the id of the system on [pvoutput.org](https://www.pvoutput.org/).
* `apiKey`: the API key to access [pvoutput.org](https://www.pvoutput.org/).

## Configuration of the Omnik Solar Inverter
1. Logon to the admin interface of your Omnik Solar Inverter.
2. Go to *Advanced* > *Remote Server*.
3. Enter the IP address and port of where you are running the daemon software.

## Installation
1. Clone this Git repository to a local folder.
2. Run `python omnik-pvoutput-daemon.py`

## PVOutput Data Mapping
The following data is pushed towards the [pvoutput.org](https://www.pvoutput.org/)
API:
* Energy Produced (today)
* Current Power
* Current Temperature
* Current Voltage (AC)

If you are using the donation mode of [pvoutput.org](https://www.pvoutput.org/), the
additional fields are filled in as follows:
* PV1 Voltage (DC) on `v7`.
* PV2 Voltage (DC) on `v8`.
* PV1 Current (DC) on `v9`.
* PV2 Current (DC) on `v10`.
* AC Current on `v11`.
* AC Frequency on `v12`.

## Credits
The code of this product is based upon:
* [t3kpunk/Omniksol-PV-Logger](https://github.com/t3kpunk/Omniksol-PV-Logger) for receiving data 
  from the Omnik Solar Inverter.
* [Woutrrr/Omnik-Data-Logger](https://github.com/Woutrrr/Omnik-Data-Logger) for parsing the Omnik Solar Inverter
  messages.
* [erijo/sunnyportal-py](https://github.com/erijo/sunnyportal-py) for sending data
  to [pvoutput.org](https://www.pvoutput.org/).