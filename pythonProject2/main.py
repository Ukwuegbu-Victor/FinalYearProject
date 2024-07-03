import sys
import numpy as np
from input import input
from echo import echo
from gridgen import gridgen


def main(cases_file):
    with open(cases_file, 'r') as casefile:
        ncase = int(casefile.readline().strip())

        cases = []
        for _ in range(ncase):
            data = casefile.readline().split()
            cases.append(data[:4])

    for icase, case in enumerate(cases, start=1):
        datafn, outpfn1, outpfn2, _ = case

        outpfn4, xl, yl, nx, ny = input(datafn)

        ib, jb = 1, 1
        id, jd = 99, 99
        ie = (ib - 1) + nx
        je = (jb - 1) + ny

        echo(outpfn1, datafn, ib, ie, jb, je, id, jd, xl, yl, nx, ny)
        dx, dy, *grid_data = gridgen(ib, ie, jb, je, nx, ny, xl, yl, 1.0)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <cases_file>")
        sys.exit(1)

    cases_file = sys.argv[1]
    main(cases_file)
