# breeze-intercomparison
Notebooks for processing and examination of satellite wind velocity data in comparison to common model wind information over the ocean within the ACS wave modelling domain.

# Data
## Model information
Surface wind speed as a magnitude of the component vectors (uas and vas) from:
* BARRA2 - ob53
* BARPA-R - py18
* CCAM_v2203 - hq89
* ERA5_native - rt52

## Validation datasets
* ASCAT wind speed data - https://data.eumetsat.int/product/EO:EUM:DAT:METOP:OSI-104
* satellite altimeter data - per AODN / accessed from lg17
* CCMP v3.1 wind speed (mix of satellite and reanalysis) - https://www.remss.com/measurements/ccmp

# Filtering / collation
* ASCAT data - ASCAT is issued in unscreened swath tiles - methods for screening and chopping to the area of interest are found in `extract_ascat.ipynb`  
* CCMP data - CCMP is global and issued for both land and sea tiles - masking for land is provided using NaturalEarth tiles available in `cartopy`, methods for doing so are included in `ccmp_wind_processing.ipynb`
All wind data products are restricted to the limits of the scatterometer data (no winds greater than 30 m.s-1) for comparison purposes (this removes 19 instances from the CCMP dataset for 2016)

# Comparison
* Each satellite wind speed instance is compared to the nearest model wind speed, both in location and time. Where more than one validation point occurs in the same time and space, these values are averaged before comparison.
* Global comparison metrics are calculated (r2, nrmse, bias) for each comparison - this workflow is virtually identical for each validation set
* Spatial aggregation / distribution was provided by regridding onto a 25km Australian Albers grid (similar to EPSG:3577), except for CCMP, where all maps were provided at that product spatial resolution (15 arcmin)

