#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests, json


def addition(a, b):
    return eval("%s + %s" % (a, b))


result = addition(request.json["a"], request.json["b"])
print("The result is %d." % result)
