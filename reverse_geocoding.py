#!/usr/bin/env python
# by Antoine Mazières (http://mazier.es ; {github|twitter}@mazieres)
# Cortext Lab -- http://www.cortext.net/
import sys
import json
import gzip
import os
import re

from collections import defaultdict
from abrvs import abrvs

reload(sys)
sys.setdefaultencoding("utf-8")


def load_polygons_db():
    f = gzip.open("polygons.json.gz", "r")
    polygons = json.load(f)
    f.close()
    return polygons

def point_inside_polygon(x, y, poly):
    n = len(poly)
    inside =False
    p1x,p1y = poly[0]
    for i in range(n+1):
        p2x,p2y = poly[i % n]
        if y > min(p1y,p2y):
            if y <= max(p1y,p2y):
                if x <= max(p1x,p2x):
                    if p1y != p2y:
                        xinters = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x,p1y = p2x,p2y
    return inside

def point_inside_country(lon, lat, abrv, polygons_db):
    country = polygons_db[abrv]
    for poly in country:
        if point_inside_polygon(lon, lat, poly):
            return True
    return False

def find_country(lon, lat, polygons_db):
    for abrv in abrvs:
        if point_inside_country(lon, lat, abrv, polygons_db):
            return abrv
    return None

def findall_country(coords, polygons_db):
    res = {}
    for coord in coords:
        lon, lat = coord[0], coord[1]
        res[coord] = find_country(lon, lat, polygons_db)
    return res
