#!/usr/bin/env bash

# $1 treepath
# $2 taxonomy file (unarchived)

export SCRIPTS_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

treename=`basename $1`
mkdir -p $treename

t2t reroot -n $SCRIPTS_DIR/archaea.ids \
    -t $1 \
    -o $treename/rt \
    --out-of-target $SCRIPTS_DIR/arbitrary_bacteria.txt

t2t decorate \
    -m $2 \
    -t $treename/rt \
    --no-suffix \
    --min-count 1 \
    -o $treename/rt-dec

t2t compare-to-decorated \
    --decorated-taxonomy $treename/rt-dec-consensus-strings \
    --backbone-taxonomy $2 \
    --level 1 \
    --output $treename/lvl1-comparison \
    --get-records

