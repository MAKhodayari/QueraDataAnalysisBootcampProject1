# %%
import pandas as pd
import numpy as np
from math import sqrt
# %%
df = pd.read_csv("/media/mohammadsaleh/bootcamp/project1/Quera_Data_Science/fidilio scrape/data.csv")

# %%
df.columns
# %%
lat_lon = np.array(df[['latitude', 'longitude']])
lat_lon
# %%
def oghli(x1 , y1 , x2 , y2):
    fasele = sqrt((x1-x2)**2+(y1-y2)**2)
    return fasele

# %%
s1 = oghli(-0.212,0.289714286 , -1.045714286 , 0.998571429)
# %%
s2 = oghli(34.505956, 51.834168 , 39.782055, 44.614161)
# %%
a = 51.834168- (-0.212 * s2/s1)
a
# %%
(-1.045714286)*(s2/s1)#+a
# %%
b = 44.614161 - (s2/s1)+a
b
# %%
(s2/s1)*4.56 , (s2/s1)*7.59
# %%
a
# %%
[1,2]*2

# %%
def m(x1 , y1 , x2 , y2):
    shib = (y1-y2)/(x1-x2)
    return shib
def arz_az_mabda(x1 , y1 , m):
    return y1-(m*x1)

# %%
a = m(0.289714286 , -0.212 , 34.505956, 51.834168)
b = arz_az_mabda(0.289714286 , -0.212, a)
# %%
c = m(0.998571429 , -1.045714286 ,39.782056, 44.614162 )
d = arz_az_mabda(0.998571429 , -1.045714286 , c)

# %%
x = (b-d)/(c-a)
x
# %%
y = a*x+b
y
# %%
(-0.212-y)
# %%
(s2/s1)
# %%
