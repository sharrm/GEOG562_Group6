import sys
import numpy as np
import matplotlib.pyplot as plt
import rasterio
import rasterio.mask
# from rasterio import plot
# from rasterio.plot import show
import fiona
import geopandas as gpd
# from osgeo import gdal

in_shp = r"P:\SDB\Florida Keys\Popcorn\Test_Files\clipper.shp"
in_raster = r"P:\SDB\Florida Keys\Popcorn\Test_Files\rel_test.tif"

with fiona.open(in_shp, 'r') as shapefile:
    shape = [feature['geometry'] for feature in shapefile]
    print(shape)

with rasterio.open(in_raster) as src:
    out_image, out_transform = rasterio.mask.mask(src, shape, crop=True)
    out_meta = src.meta

# export
out_meta.update({"driver": "GTiff",
                 "height": out_image.shape[1],
                 "width": out_image.shape[2],
                 "transform": out_transform})

with rasterio.open(r"P:\SDB\Florida Keys\Popcorn\Test_Files\masked.tif", "w", **out_meta) as dest:
    dest.write(out_image)

