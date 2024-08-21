import os

import earthaccess
from netCDF4 import Dataset

earthaccess.login()

# Download some MODIS/Terra Thermal Anomalies/Fire 5-Min L2 Swath 1km data (100 files)
results = earthaccess.search_data(
    concept_id="C2271754179-LPCLOUD", count=1, temporal=("2015-06-01", "2015-12-31")
)
file = earthaccess.download(results, "earthaccess_data")[0]

cwd = os.getcwd()
fh = Dataset(os.path.join(cwd, file), mode="r")
print(fh.variables["fire mask"].shape)
print(fh.variables["FP_line"].shape)
