#!/usr/bin/env python

import sys


def usage():
    print >> sys.stderr, "Usage: python %s <filename>" % (sys.argv[0])


def main():
    print "Program arguments are:", sys.argv
    print "Number of arguments is:", len(sys.argv)
    if len(sys.argv) != 2:
        usage()
        sys.exit(1)
    try:
        fp = open(sys.argv[1], "r")
    except IOError, e:
        print >> sys.stderr, "Argument is not a valid filename"
        usage()
        sys.exit(1)

    max = 0
    min = 11

    for idx, line in enumerate(list(fp)):
        items = line.split('\t')
        grade = int(items[3])
        if grade > max:
            max = grade
            maxInfo = items[0]+items[1]+items[2]
        if grade < min:
            min = grade
            minInfo = items[0]+items[1]+items[2]
    print "Maxim is %d %s" % (max, maxInfo)
    print "Minim is %d %s" % (min, minInfo)


if __name__ == "__main__":
    sys.exit(main())
