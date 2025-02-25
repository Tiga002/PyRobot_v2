#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
    DESTDIR_ARG="--root=$DESTDIR"
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/developer/low_cost_ws/src/pyrobot/robots/LoCoBot/locobot_navigation/orb_slam2_ros"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/developer/low_cost_ws/install/lib/python3/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/developer/low_cost_ws/install/lib/python3/dist-packages:/home/developer/low_cost_ws/build/lib/python3/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/developer/low_cost_ws/build" \
    "/home/developer/pyenv_pyrobot_python3/bin/python" \
    "/home/developer/low_cost_ws/src/pyrobot/robots/LoCoBot/locobot_navigation/orb_slam2_ros/setup.py" \
    build --build-base "/home/developer/low_cost_ws/build/pyrobot/robots/LoCoBot/locobot_navigation/orb_slam2_ros" \
    install \
    $DESTDIR_ARG \
    --install-layout=deb --prefix="/home/developer/low_cost_ws/install" --install-scripts="/home/developer/low_cost_ws/install/bin"
