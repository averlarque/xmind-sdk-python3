#!/usr/bin/env python

"""
    xmind.core.title
    ~~~~~~~~~~~~~~~

    :copyright:
    :license:

"""

__author__ = "woody@xmind.net <Woody Ai>"

from . import const

from .mixin import WorkbookMixinElement


class TitleElement(WorkbookMixinElement):
    TAG_NAME = const.TAG_TITLE

    def __init__(self, node=None, ownerWorkbook=None):
        super(TitleElement, self).__init__(node, ownerWorkbook)


def main():
    pass

if __name__ == '__main__':
    main()
