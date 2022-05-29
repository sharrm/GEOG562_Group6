# -*- coding: utf-8 -*-
"""
@author: sharrm
"""

import sys
import os
import numpy as np
import matplotlib.pyplot as plt
import rasterio
import rasterio.mask
# from rasterio import plot
# from rasterio.plot import show
import fiona
import geopandas as gpd
# from osgeo import gdal
import linear_regression as slr

# input files
in_shp = r"P:\SDB\Florida Keys\Popcorn\Test_Files\clipper.shp"
# in_raster = r"P:\SDB\Florida Keys\Popcorn\Test_Files\rel_test.tif"
blue = r"P:\SDB\Florida Keys\Popcorn\Test_Files\S2A_MSI_2021_12_01_16_05_11_T17RNH_rhos_492.tif"
green = r"P:\SDB\Florida Keys\Popcorn\Test_Files\S2A_MSI_2021_12_01_16_05_11_T17RNH_rhos_560.tif"
red = r"P:\SDB\Florida Keys\Popcorn\Test_Files\S2A_MSI_2021_12_01_16_05_11_T17RNH_rhos_665.tif"

# options (thinking ahead to using this on multiple bands)
SDBred = True
SDBgreen = True

# list of bands
rasters = [blue, green, red]

# dict to store output file names
masked_rasters = {}

# open bounding shapefile
# with fiona.open(in_shp, 'r') as shapefile:
#     shape = [feature['geometry'] for feature in shapefile]

# loop through input rasters
# for band in rasters:
#     # read raster, extract spatial information, mask the raster using the input shapefile
#     with rasterio.open(band) as src:
#         out_image, out_transform = rasterio.mask.mask(src, shape, crop=True)
#         out_meta = src.meta
        
#     # writing information
#     out_meta.update({"driver": "GTiff",
#                       "height": out_image.shape[1],
#                       "width": out_image.shape[2],
#                       "transform": out_transform})
    
#     # simply customizing the output filenames here -- there's probably a better method
#     if '492' in band: # blue wavelength (492nm)
#         outraster_name = os.path.join(os.path.dirname(band), 'masked_' + os.path.basename(band)[-7:-4] + '.tif')
#         masked_rasters['blue'] = outraster_name
#     elif '560' in band: # green wavelength (560nm)
#         outraster_name = os.path.join(os.path.dirname(band), 'masked_' + os.path.basename(band)[-7:-4] + '.tif')
#         masked_rasters['green'] = outraster_name
#     elif '665' in band: # red wavelength (665nm)
#         outraster_name = os.path.join(os.path.dirname(band), 'masked_' + os.path.basename(band)[-7:-4] + '.tif')
#         masked_rasters['red'] = outraster_name

#     # write masked raster to a file
#     with rasterio.open(outraster_name, "w", **out_meta) as dest:
#         dest.write(out_image)
    
#     # close the file
#     dest = None

if SDBgreen == True:
    # read blue band
    with rasterio.open(masked_rasters['blue']) as src:
        blue_image, out_transform = rasterio.mask.mask(src, shape, crop=True)
        out_meta = src.meta
    
    # read green band
    with rasterio.open(masked_rasters['green']) as src:
        green_image, out_transform = rasterio.mask.mask(src, shape, crop=True)
        out_meta = src.meta
            
    # export
    out_meta.update({"driver": "GTiff",
                      "height": out_image.shape[1],
                      "width": out_image.shape[2],
                      "transform": out_transform})
    
    # increase band values by factor of 1,000
    ratioBlueArrayOutput = blue_image * 1000
    ratioGreenArrayOutput = green_image * 1000
    
    # calculate natural log of each band
    lnBlueArrayOutput = np.log(ratioBlueArrayOutput)
    lnGreenArrayOutput = np.log(ratioGreenArrayOutput)
    
    # compute ratio between bands
    ratioImage = lnBlueArrayOutput / lnGreenArrayOutput
    
    # output raster filename with path
    outraster_name = os.path.join(os.path.dirname(blue), 'ratio_of_logs.tif')
    
    # write ratio between bands to a file
    with rasterio.open(outraster_name, "w", **out_meta) as dest:
        dest.write(ratioImage)
    
    # close the file
    dest = None

# slr
print(outraster_name)
slr.slr(outraster_name)

# input files
# blueband = r"P:\SDB\Florida Keys\Popcorn\Test_Files\masked_492.tif"
# greenband = r"P:\SDB\Florida Keys\Popcorn\Test_Files\masked_560.tif"
# redband = r"P:\SDB\Florida Keys\Popcorn\Test_Files\masked_665.tif"
# mask = r"U:\ce567\sharrm\Lab7\dataset_files\mask_buck.shp"

# def read_band(band):
#     with rasterio.open(masked_rasters['blue']) as src:
#         read_image, out_transform = rasterio.mask.mask(src, shape, crop=True)
#         out_meta = src.meta

#     return read_image, out_meta, out_transform

# def relative_bathymetry(band1, band2):
#     band1, ref, transform = read_band(band1)
#     band2, ref, transform = read_band(band2)

#     # Stumpf algorithm
#     ratiologs = np.log(1000 * band1) / np.log(1000 * band2)

#     return ratiologs, ref, transform

# def write_raster(band1, band2):
#     output_rol = relative_bathymetry(band1, band2)

#     # output raster filename with path
#     outraster_name = os.path.join(os.path.dirname(band1), 'ratio_of_logs.tif')

#     # write ratio between bands to a file
#     with rasterio.open(outraster_name, "w", **out_meta) as dest:
#         dest.write(ratioImage)

#     # close the file
#     dest = None

#     return None

# write_raster(blueband, redband)