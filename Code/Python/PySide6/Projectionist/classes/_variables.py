#!/usr/bin/env python3
# coding: utf-8

def init() -> None:
    global __ProjectionistVersionMajor
    __ProjectionistVersionMajor = "0"
    global __ProjectionistVersionMinor
    __ProjectionistVersionMinor = "0"
    global __ProjectionistVersionBuild
    __ProjectionistVersionBuild = "0"
    global __ProjectionistVersionCompile
    __ProjectionistVersionCompile = "1000"
    global __ProjectionistVersion
    __ProjectionistVersion = __ProjectionistVersionMajor + "."
    + __ProjectionistVersionMinor + "."
    + __ProjectionistVersionBuild + "."
    + __ProjectionistVersionCompile


def main() -> None:
    print("WARNING:")
    print("There is no executable code in this file.")
    print("It is used to store GLOBAL Variables and Constants")


if __name__ == '__main__':
    main()
