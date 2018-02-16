#!/bin/bash
### BEGIN INIT INFO
# Provides: omniksol4kd.py
# Required-Start: $network $syslog
# Required-Stop: $network
# Default-Start: 2 3 4 5
# Default-Stop: 0 1 6
# Description: Start or stop the omniklog web server
### END INIT INFO

DIR=/volume1/automation/omnik-pvoutput-daemon

case "$1" in
    start)
        python ${DIR}/omnik-pvoutput-daemon.py &
        ;;
    stop)
        echo "Not implemented" >&2
        ;;
    *)
        echo "Usage: $0 start|stop" >&2
        exit 3
        ;;
esac
