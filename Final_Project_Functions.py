########################################
# This is the function section of the code for Group 6's final project in GEOG 462
# Group Members include Matthew Sharr, Jasen White, and Juliana Wold.

########################################
# Inputting Sentinel 2 or Landsat imagery

# This function should read in a TIF file and convert it into a Numpy Array
# Technique is from: https://stackoverflow.com/questions/7569553/working-with-tiffs-import-export-in-python-using-numpy
def pil_to_numpy(inputPath):
    import numpy as np
    import os
    from PIL import Image

    if not os.path.isfile(inputPath):
        print(f"That file does not appear to exist. Please check the file path: \n"
              f"{inputPath}")
        return False, None
    try:
        imFile = Image.open(inputPath)

    except:
        print(f"There was an issue opening the file {inputPath}\n"
              f"Please check the file path and try again.")
        return False, None

    # # Show the TIF file (Currently just returns a black image)
    # imFile.show()

    # convert the imported TIF into a Numpy Array
    imarray = np.array(imFile)

    # Verify that the NumPy array and the imported TIF file are the same size
    sizeNumpy = imarray.shape
    sizePIL = imFile.size
    sizeCheck = sizeNumpy == sizePIL
    if not sizeCheck:
        print("ERROR: The size of the NumPy array does not match the size of the PIL array.")
        return False, None

    else:
        print(f"The size check is satisfactory. \nNumPy size = {sizeNumpy} \nPIL size = {sizePIL}\n"
              f"Outputting the the Numpy array for {inputPath}\n")

        return True, imarray

    # If necessary, the Numpy Array can be converted back into a PIL image using this code:
    # Image.fromarray(imarray)


# End of conversion from tif files to NumPy arrays.
#########################################

########################################
# Conduct a band math operation using the Blue and Green NumPy arrays.

# # Check the threshold
#
# if threshold > numpy.max(arr):
#     print("Threshold is greater than the maximum of the array")
#     return False, None
# else:
#     outarr = arr > threshold  # a band math operation here!  The result is a boolean array of the type "ndarray"
#
# # Convert Array to raster (keep the origin and cellsize the same as the input)
# try:
#     print("Writing to ")
#     if imagefile[-4] != '.':  # Checking if the image doesn't have an extension
#         outfile = imagefile + 'thresh'  # add string to the end of the original name if no extension
#     else:
#         outfile = imagefile[:-4] + "thresh" + imagefile[-4:]  # add string before the extension if present
#     print(outfile)
#
#    
# except:
#     print("Problem writing file")
#     return False, None
