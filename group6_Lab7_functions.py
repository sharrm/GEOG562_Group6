from arcpy.sa import *
from arcpy import env

# arcpy workspace
env.workspace = r'R:\GEOG562\Students\sharrm\Lab7\Lab7_ArcProject\Group6_Lab7.gdb'

# file inputs
disturbance_raster = "forest_disturbance"

# temp input for testing
# year = '2006'

years = range(2002, 2013, 1)

for year in years:
    # create raster containing values for year of interest
    dist_year = Con(Raster(disturbance_raster) == year, year)
    dist_year.save(f'disturbance_{year}')