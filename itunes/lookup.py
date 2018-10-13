# -*- coding: utf-8 -*-
"""This module contains utilities for performing a variety of different
lookups against the iTunes store API
"""
from itunes import COUNTRY, API_VERSION, BaseObject
__all__ = ['lookup', 'lookup_upc', 'Lookup', 'LookupUPC']


class Lookup(BaseObject):
    """A data model for an individual resource look up against iTunes"""
    resource = 'lookup'

    def __init__(self, id, entity=None, limit=50):
        super(self.__class__, self).__init__(id=id, entity=entity, limit=limit)
        self.id = id


def lookup(id):
    """Perform an individual :class:`Lookup` on a single resource in the iTunes
    Store API
    """
    items = Lookup(id).get()
    if not items:
        raise NoResultsFoundException()
    return items[0]


class LookupUPC(BaseObject):
    """A data model for an individual resource look up against iTunes"""
    resource = 'lookup'

    def __init__(self, upc, entity=None, limit=50):
        super(self.__class__, self).__init__(upc=upc, entity=entity, limit=limit)
        self.upc = upc


def lookup_upc(upc):
    """Perform an individual :class:`LookupUPC` on a single resource in the iTunes
    Store API
    """
    items = LookupUPC(upc).get()
    if not items:
        raise NoResultsFoundException()
    return items[0]
