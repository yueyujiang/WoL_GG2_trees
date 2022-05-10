#!/usr/bin/env python3
"""PhyloPhlAn-style MSA trimmer

Usage:
    cat input.aln | python me.py > output.aln

When:
    After trimal and before concatenation.

Modified from:
    https://github.com/biobakery/phylophlan/blob/master/phylophlan/phylophlan.py

Mimic PPA's `--fast --diversity high` behavior. See:
    https://github.com/biobakery/phylophlan/wiki#accurate-or-fast-1

License:
    PhyloPhlAn3 is licensed under MIT. See:
    https://github.com/biobakery/phylophlan/blob/master/license.txt
"""

import fileinput
import math
import pickle
from math import log, sqrt, ceil
from collections import Counter


# parameters
submat = 'pfasum60.pkl'
gap_th = 0.85  # maximum fraction of gaps per site
var_th = 0.9   # maximum fraction of most frequent character per site
fra_th = 0.67  # maximum fraction of gaps per sequence
unk_th = 0.3   # maximum fraction of unknown character (- and x) per site
sub_fr = 0.1   # proportion of sites to subsample


def gap_cost(seq, norm=True):
    gaps = seq.count('-')
    if norm:
        if len(seq) != 0:
            gaps /= len(seq)
        else:
            gaps = 1
    return gaps


def symbol_diversity(seq, log_base=21):
    sh = 0.0
    for _, abs_freq in Counter(seq.upper()).items():
        rel_freq = abs_freq / len(seq)
        sh -= rel_freq * log(rel_freq)

    sh /= log(min(len(seq), log_base))
    return sh if (sh > 0.15) and (sh < 0.85) else 0.99


def normalized_submat_scores(aa, submat):
    aas = 'ACDEFGHIKLMNPQRSTVWY'
    aa = aa.upper()
    m = 0.0
    if aa not in '-XZ':
        for bb in aas:
            m += submat[(aa, bb)] / sqrt(submat[(aa, aa)] * submat[(bb, bb)])
    return m


def stereochemical_diversity(seq, submat):
    set_seq = set(seq.upper())
    aa_avg = sum([normalized_submat_scores(aa, submat) for aa in set_seq])
    aa_avg /= len(set_seq)
    r = sum([abs(aa_avg - normalized_submat_scores(aa, submat)) for aa in set_seq])
    r /= len(set_seq)
    r /= sqrt(20 * (max(submat.values()) - min(submat.values()))**2)
    return r


def trident(seq, submat, alpha=1, beta=0.5, gamma=3):
    return ((1 - symbol_diversity(seq)) ** alpha *
            (1 - stereochemical_diversity(seq, submat)) ** beta *
            (1 - gap_cost(seq)) ** gamma)


def itercols(aln):
    """Iterate columns of an alignment.
    """
    for i, c in enumerate(aln[0]):
        yield ''.join(x[i] for x in aln)


def dropcols(aln, ii):
    """Drop alignment columns by index.
    """
    return [''.join([c for i, c in enumerate(x) if i not in ii]) for x in aln]


def main():

    # read substitution matrix
    with open(submat, 'rb') as f:
        mat = pickle.load(f)

    # read alignment
    ids, aln = [], []
    for line in fileinput.input():
        line = line.rstrip()
        if line.startswith('>'):
            ids.append(line[1:])
            aln.append('')
        else:
            aln[-1] += line

    # drop sites by high gap proportion
    todel = []
    for i, col in enumerate(itercols(aln)):
        if gap_cost(col) >= gap_th:
            todel.append(i)
    if todel:
        aln = dropcols(aln, todel)

    # drop sites by lack of variance
    todel = []
    for i, col in enumerate(itercols(aln)):
        col = col.replace('-', '')
        th = var_th * len(col)
        for _, fq in Counter(col).items():
            if fq >= th:
                todel.append(i)
                break
    if todel:
        aln = dropcols(aln, todel)

    # drop sequences by high fragmentation
    tokeep = [i for i, x in enumerate(aln) if gap_cost(x) < fra_th]
    aln = [aln[i] for i in tokeep]
    ids = [ids[i] for i in tokeep]

    # calculate trident score of each site
    th = unk_th * len(aln)
    scores = []
    for i, col in enumerate(itercols(aln)):
        fqs = Counter(col.upper())
        if len(set(fqs) - {'-', 'X'}) <= 1:
            continue
        if fqs['-'] + fqs['X'] > th:
            continue
        scores.append((trident(col, mat), i))

    # subsample sites by score
    # npos = int(ceil(len(aln[0]) * 0.1))
    npos = 100
    best = [i for _, i in sorted(scores)[-npos:]]
    aln = [''.join([c for i, c in enumerate(x) if i in best]) for x in aln]

    # output alignment
    for id, seq in zip(ids, aln):
        print('>' + id)
        print(seq)


if __name__ == '__main__':
    main()
