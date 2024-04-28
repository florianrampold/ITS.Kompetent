#!/usr/bin/env bash
# Usage: wait-for-it.sh host:port [-t timeout] [-- command args]
#   -h HOST | --host=HOST       Host or IP under test
#   -p PORT | --port=PORT       TCP port under test
#   alternatively, you can use the first positional argument with host:port
#   -t TIMEOUT | --timeout=TIMEOUT
#                                Timeout in seconds, zero for no timeout
#   -- COMMAND ARGS              Execute command with args after the test finishes

TIMEOUT=15
QUIET=0
CHILD=0
CHILD_PID=0
RESULT=0

# timeout function
timeout() { perl -e 'alarm shift; exec @ARGV' "$@"; }

# clean up child process if script is terminated
cleanup() {
    if [ $CHILD -eq 1 ]; then
        kill $CHILD_PID
    fi
    exit $RESULT
}

# wait until host is reachable
wait_for() {
    if [ $QUIET -eq 1 ]; then
        timeout $TIMEOUT bash -c "until echo > /dev/tcp/$HOST/$PORT; do sleep 1; done"
    else
        timeout $TIMEOUT bash -c "until echo > /dev/tcp/$HOST/$PORT; do echo 'Waiting for $HOST:$PORT...'; sleep 1; done"
    fi
    RESULT=$?
    if [ $RESULT -ne 0 ]; then
        echo "Operation timed out" >&2
    fi
    return $RESULT
}

# parse arguments
while [ $# -gt 0 ]
do
    case "$1" in
        *:* )
        HOST=$(printf "%s\n" "$1"| cut -d : -f 1)
        PORT=$(printf "%s\n" "$1"| cut -d : -f 2)
        shift 1
        ;;
        --quiet)
        QUIET=1
        shift 1
        ;;
        -t)
        TIMEOUT="$2"
        if [[ $TIMEOUT =~ ^[0-9]+$ ]]; then
            shift 2
        else
            echo "Error: Illegal number of timeouts" >&2
            exit 1
        fi
        ;;
        --timeout=*)
        TIMEOUT="${1#*=}"
        shift 1
        ;;
        --)
        shift
        CHILD=1
        break
        ;;
        --help)
        echo "Usage: $0 host:port [-t timeout] [-- command args]"
        exit 0
        ;;
        *)
        echo "Unknown argument: $1"
        exit 1
        ;;
    esac
done

if [ "$HOST" == "" -o "$PORT" == "" ]; then
    echo "Error: you need to provide a host and port to test." >&2
    exit 1
fi

wait_for

# execute command
if [ $CHILD -eq 1 ]; then
    CHILD_PID=$!
    if [ $RESULT -eq 0 ]; then
        exec "$@"
    fi
fi

cleanup

