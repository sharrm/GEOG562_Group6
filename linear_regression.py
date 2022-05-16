import rasterio
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

if __name__ == "__main__":
    
    # Load in our CSVs
    icesat2 = r"R:\GEOG562\Students\sharrm\Final\Data\ICESat2\processed_ATL03_20211208020242_11701307_005_01_gt1l_o_o.csv"
    pts = pd.read_csv(icesat2)
    
    coords = [(x,y) for x, y in zip(pts.E, pts.N)]
             
    print(coords)
    
    # Define a path to the raster
    in_raster = r"R:\GEOG562\Students\sharrm\Final\Data\Sentinel2\S2A_MSI_2021_12_01_16_05_11_T17RNH_rhos_492.tif"
    
    src = rasterio.open(in_raster)
    
    # sampled = rasterio.sample.sample_gen(in_raster, coords)
    
    pts['Raster Value'] = [x[0] for x in src.sample(coords)]
    
    X = pts.drop(columns=['E', 'N', 'Z'])
    y = pts.Z
    
    reg = LinearRegression().fit(X, y)
    reg.score(X, y)
    reg.coef_
    reg.intercept_
    
    pts['y_hat'] = reg.predict(X)
    
    
    plt.scatter(pts.Z, pts.y_hat, alpha=0.5)
    plt.show()
    
    
