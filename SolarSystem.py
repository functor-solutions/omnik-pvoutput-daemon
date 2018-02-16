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

#
# Represents a configured solar system.
#
class SolarSystem:
    def __init__(self, config, section):
        self.serialNumber = config.get(section, "serial")
        self.systemId = config.get(section, "systemId")
        self.apiKey = config.get(section, "apiKey")

    def getSerialNumber(self):
        return self.serialNumber

    def getSystemId(self):
        return self.systemId

    def getApiKey(self):
        return self.apiKey