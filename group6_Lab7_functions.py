from arcpy.sa import *
from arcpy import env

# arcpy workspace
env.workspace = r'R:\GEOG562\Students\sharrm\Lab7\Lab7_ArcProject\Group6_Lab7.gdb'

# file inputs
years_raster = "forest_disturbance"

# temp input for testing
year = '2006'

# create raster containing values for year of interest
dist_2003 = Con(Raster(years_raster) == 2006, 2006)
dist_2003.save(f'output_{year}')