#!/usr/bin/env bash

# $1 treepath
# $2 taxonomy file (unarchived)

export SCRIPTS_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

treename=`basename $1`
taxonomyname=`basename $2`
outdir=${treename}_${taxonomyname}
mkdir -p $outdir

t2t reroot -n $SCRIPTS_DIR/archaea.ids \
    -t $1 \
    -o $outdir/rt \
    --out-of-target $SCRIPTS_DIR/arbitrary_bacteria.txt
#cp $1 $outdir/rt

t2t decorate \
    -m $2 \
    -t $outdir/rt \
    --no-suffix \
    --min-count 1 \
    -o $outdir/rt-dec \
    --add-nameholder 

t2t compare-to-decorated \
    --decorated-taxonomy $outdir/rt-dec-consensus-strings \
    --backbone-taxonomy $2 \
    --level 1 \
    --output $outdir/lvl1-comparison \
    --get-records

