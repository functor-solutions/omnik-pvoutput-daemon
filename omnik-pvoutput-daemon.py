#!/usr/bin/python

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
import logging

from Daemon import Daemon


def main():
    logging.basicConfig(filename='omnik-pvoutput-daemon.log', level=logging.DEBUG)

    sevr = Daemon()
    sevr.run()

if __name__ == "__main__":
    main()
