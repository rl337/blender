BINDIR=`dirname "$0"`

if [ "X$BLENDER_HOME" == "X" ]; then
    BLENDER_HOME="/Applications/blender-2.78a-OSX_10.6-x86_64"
fi

BLENDER_BIN="$BLENDER_HOME/blender.app/Contents/MacOS/blender"

if [ ! -f "$BLENDER_BIN" ]; then
    echo "Blender binary not found as $BLENDER_BIN" 1>&2
    exit -1
fi

PYTHONPATH="$BINDIR/." "$BLENDER_BIN" --background --python "$@"
