import rasterio
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# if __name__ == "__main__":
    
def slr(in_raster):
    # Load in our CSVs
    icesat2 = r"P:\SDB\Florida Keys\Popcorn\Data\ICESat2\icesat2_clipped.csv"
    pts = pd.read_csv(icesat2)
    
    coords = [(x,y) for x, y in zip(pts.E, pts.N)]
             
    # print(coords)
    
    # Define a path to the raster
    # in_raster = r"R:\GEOG562\Students\sharrm\Final\Data\Sentinel2\S2A_MSI_2021_12_01_16_05_11_T17RNH_rhos_492.tif"
    
    src = rasterio.open(in_raster)
    
    # sampled = rasterio.sample.sample_gen(in_raster, coords)
    
    pts['Raster Value'] = [x[0] for x in src.sample(coords)]
    
    X = pts.drop(columns=['E', 'N', 'Z'])
    y = pts.Z
    
    reg = LinearRegression().fit(X, y)
    r2 = reg.score(X, y)
    b0 = reg.coef_
    b1 = reg.intercept_
    print(r2)
    print(b0)
    print(b1)
    
    pts['y_hat'] = reg.predict(X)
        
    # plt.scatter(pts.Z, pts.y_hat, alpha=0.5)
    
    plt.plot(y, pts.y_hat, '.')
    # plt.plot(b0 + b1*X, '-')
    plt.title('ICESat-2 vs pSDB')
    plt.xlabel('pSDB')
    plt.ylabel('ICESat-2')
    plt.show()
    
    src = None
    icesat2 = None



rol = r"P:\SDB\Florida Keys\Popcorn\Test_Files\ratio_of_logs.tif"

slr(rol)