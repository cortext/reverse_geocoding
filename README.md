# Reverse Geocoding

Homemade [reverse geocoding](https://en.wikipedia.org/wiki/Reverse_geocoding).
Tells you to which country belong a set of coordinates.

Based on data found @ <http://www.gadm.org/>.

**WARNING: USES A LOT OF RAM (~4Go) AND IS STILL VERY SLOW.**

## Installation

```bash
git clone git@github.com:cortext/reverse_geocoding.git
cd reverse_geocoding
wget 'http://file.cortext.net/files/polygons.json.gz'
```

## Usage

```ipython
In [1]: from reverse_geocoding import *

In [2]: polygons_db = load_polygons_db()

In [3]: find_country(2.3470599, 48.858859, polygons_db) # This is Paris
'FRA'

In [4]: abrvs[find_country(2.3470599, 48.858859, polygons_db)]
'France'

In [5]: dat = [
   ...:   (13.4251364, 52.5075419), # Berlin
   ...:   (2.3470599, 48.858859), # Paris
   ...:   (-73.979681, 40.7033127) # New-York
   ...: ]

 In [6]: findall_country(dat, polygons_db)
 {(-73.979681, 40.7033127): 'USA', (13.4251364, 52.5075419): 'DEU', (2.3470599, 48.858859): 'FRA'}
```

## To Do

+ More functions, like `is_in_country`
+ Multiprocessing
+ More administrative levels
