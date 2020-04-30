#
# omnik-pvoutput-daemon is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# omnik-pvoutput-daemon is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Foobar.  If not, see <http://www.gnu.org/licenses/>.
#
import ConfigParser
import httplib
import io
import logging
import urllib
from datetime import datetime

import OmnikInverterMessage
from SolarSystem import SolarSystem


class PvOutput:
    def __init__(self):
        with open("config.ini") as f:
            configFile = f.read()

        config = ConfigParser.RawConfigParser(allow_no_value = True)
        config.readfp(io.BytesIO(configFile))

        self.solarSystems = { }
        for section in config.sections():
            solarSystem = SolarSystem(config, section)
            self.solarSystems[solarSystem.getSerialNumber()] = solarSystem

    def process(self, msg):
        # type: (msg) -> OmnikInverterMessage
        solarSystem = self.solarSystems.get(msg.getID())

        if solarSystem is None:
            logging.info("Received message from unknown Solar System %s" % msg.getID())
            return

        logging.info("Received message from Solar System %s" % msg.getID())
        self.addStatus(solarSystem, msg, datetime.now())

    def addStatus(self, solarSystem, msg, datetime):
        # type: (msg) -> OmnikInverterMessage
        params = {
            "d": datetime.strftime("%Y%m%d"),
            "t": datetime.strftime("%H:%M"),
            "v1": msg.getEToday() * 1000,
            "v2": msg.getPower(),
            "v5": msg.getTemp(),
            "v6": msg.getVAC(1),
            "v7": msg.getVPV(1),
            "v8": msg.getVPV(2),
            "v9": msg.getIPV(1),
            "v10": msg.getIPV(2),
            "v11": msg.getIAC(1),
            "v12": msg.getFAC(1)
        }

        (status, reason, body) = self.sendRequest("/service/r2/addstatus.jsp", self.headers(solarSystem), params)

        if status != httplib.OK:
            logging.error("Failed to add status: %s", body)

    def sendRequest(self, url, headers, params):
        logging.debug("POST to %s: %s", url, params)

        conn = httplib.HTTPConnection('pvoutput.org')
        encoded = urllib.urlencode(params)
        logging.debug(encoded)
        conn.request("POST", url, encoded, headers)

        response = conn.getresponse()
        status = response.status
        reason = response.reason
        body = response.read().decode('utf-8')
        logging.debug("HTTP response: %d (%s): %s", status, reason, body)

        conn.close()
        return (status, reason, body)

    def headers(self, solarSystem):
        return {
            "X-Pvoutput-Apikey": solarSystem.getApiKey(),
            "X-Pvoutput-SystemId": solarSystem.getSystemId(),
            "Content-type": "application/x-www-form-urlencoded",
            "Accept": "text/plain"
        }