# Dataset Download & Verification Status

**Project:** How Data Centers and AI Data Centers Affect the Environment and How Can We Prevent It Using Historical Data  
**Location:** `C:\Users\janvi\Desktop\EDA Project\EDA Data\`  
**Date:** November 3, 2026  

---

## 1. Summary Statistics

- **Total Datasets Mentioned in README:** 13
- **Total Datasets Successfully Downloaded & Verified:** 10 (76.9%)
- **Total Datasets Partially Downloaded:** 0
- **Total Datasets Not Downloaded / Requiring Manual Download:** 3 (23.1%)
- **Total Files Downloaded & Extracted:** 67,091 files
- **Total Disk Volume:** ~6.88 GB

---

## 2. Detailed Dataset Breakdown

| ID | Dataset / Data Source | Organization / Source Link | Status | Files & Format | Size on Disk | Notes & Verification Details |
|---|---|---|---|---|---|---|
| **D1** | **AI Data Centers** | [Epoch AI](https://epoch.ai/data/data-centers-documentation) | ✅ **Downloaded & Verified** | `epoch_data_centers.csv` | 72.0 KB | Complete facility and construction timeline dataset with coordinates and capacity. |
| **D2** | **Generative AI Workload Power Profiles** | [National Laboratory of the Rockies / DOE](https://data.nlr.gov/submissions/312) | ✅ **Downloaded & Verified** | `nlr_genai_workload_power_profiles.zip`<br>*(Extracted: 3,148 CSV traces)* | 3,778.5 MB (3.78 GB) | High-resolution power consumption traces for LLM training and inference workloads. Full archive downloaded and unzipped. |
| **D3** | **IM3 Open Source Data Center Atlas** | [DOE / PNNL / OSTI](https://data.msdlive.org/records/65g71-a4731) | ✅ **Downloaded & Verified** | `im3_us_data_center_locations.gpkg` | 824.0 KB | Official spatial GeoPackage database of U.S. data center facilities and locations. |
| **D4** | **Open U.S. Data Centers Tracker** | [FracTracker Alliance](https://fractracker.org/data-centers/) | ✅ **Downloaded & Verified** | `fractracker_data_centers.csv`<br>`fractracker_data_centers.geojson` | 3.83 MB | Queried and extracted all **1,733 data center facilities** from the official ArcGIS FeatureServer, including coordinates, status, and environmental variables. |
| **D5** | **IM3 Projected U.S. Data Center Locations** | [DOE / PNNL / IM3](https://github.com/IMMM-SFA/datacenter-atlas) | ✅ **Downloaded & Verified** | `datacenter_atlas_project.zip`<br>*(Extracted full repository)* | 250.8 MB | Complete repository containing model projections through 2035, siting scenarios, and processing notebooks. |
| **D6** | **EPRI U.S. Data Center Load Projections** | [EPRI](https://powering-intelligence.epri.com/) | ⚠️ **Manual Download Required** | `Pending manual export` | - | **Reason:** Interactive web dashboard application. The state-level scenario projections must be exported directly via the portal interface or downloaded as the Powering Intelligence report PDF from a browser. |
| **D7** | **EIA-930 Hourly U.S. Electric Grid Monitor** | [U.S. EIA](https://www.eia.gov/electricity/gridmonitor/) | ✅ **Downloaded & Verified** | `EIA930_BALANCE_2024_Jan_Jun.csv` | 39.8 MB | Official six-month half-year hourly balance file (44 columns, hourly demand, net generation by fuel source, interchange across all balancing authorities). |
| **D8** | **Emissions & Generation Resource Integrated Database (eGRID)** | [U.S. EPA](https://www.epa.gov/egrid/detailed-data) | ✅ **Downloaded & Verified** | `egrid2023_data.xlsx` | 20.2 MB | Official EPA Excel workbook containing generation mix, carbon emission rates, and subregion/state-level power characteristics. |
| **D9** | **Water Use in the United States** | [U.S. Geological Survey](https://water.usgs.gov/watuse/data/) | ⚠️ **Manual Download Required** | `Pending manual download` | - | **Reason:** USGS retired direct unauthenticated CSV endpoints (Circular 1441) and transitioned them to the ScienceBase catalog ([DOI: 10.5066/F7TB15V5](https://doi.org/10.5066/F7TB15V5)), which requires browser access to download `usco2015.xlsx`. |
| **D10** | **EPA EJScreen Data, 2015–2024** | [EPA / Zenodo](https://zenodo.org/records/14767363) | ⚠️ **Manual Download Required** | `Pending manual download` | - | **Reason:** Zenodo blocks automated/programmatic downloads with HTTP 403 Forbidden (*"Access to this resource has been restricted due to unusual traffic from your network"*). Requires opening the link in a browser and clicking download. |
| **D11** | **Low-Income Energy Affordability Data (LEAD)** | [DOE / OpenEI](https://catalog.data.gov/dataset/low-income-energy-affordability-data-lead-tool-2022-update) | ✅ **Downloaded & Verified** | `VA-2022-LEAD-data.zip`<br>`TX-2022-LEAD-data.zip`<br>*(Extracted: 16 CSV files)* | 2,775.1 MB (2.78 GB) | Comprehensive county and census-tract energy burden datasets for primary data center hubs (Virginia and Texas). Downloaded and unzipped. |
| **D12** | **Environmental Footprint Data** | [Boavizta](https://github.com/Boavizta/environmental-footprint-data) | ✅ **Downloaded & Verified** | `boavizta-data-us.csv`<br>`boavizta-data-fr.csv` | 735.0 KB | Complete CSV tables containing life-cycle assessment (LCA) environmental footprints, embodied carbon, and server specs. |
| **D13** | **Hardware / Computing Environmental Data** | [Boavizta](https://github.com/Boavizta/boaviztapi) | ✅ **Downloaded & Verified** | `boaviztapi_repo.zip`<br>*(Extracted: 338 files)* | 12.5 MB | Complete reference data and Python calculation archetypes for digital and server environmental impacts. |

---

## 3. Directory Layout in `EDA Data`

```
EDA Data/
├── README.md                                  # Original project README (preserved intact)
├── dataset_download_status.md                 # This comprehensive verification status document
├── data.py                                    # Existing intake script (preserved intact)
├── D1_Epoch_AI_Data_Centers/
│   └── epoch_data_centers.csv
├── D2_NLR_GenAI_Power_Profiles/
│   ├── nlr_genai_workload_power_profiles.zip
│   └── extracted/                             # 3,148 workload trace CSV files
├── D3_IM3_Data_Center_Atlas/
│   └── im3_us_data_center_locations.gpkg
├── D4_FracTracker_US_Data_Centers/
│   ├── fractracker_data_centers.csv           # 1,733 records with coordinates & MW capacity
│   └── fractracker_data_centers.geojson
├── D5_IM3_Projected_Locations/
│   ├── datacenter_atlas_project.zip
│   └── extracted/                             # 2035 projections & siting scenarios
├── D6_EPRI_Load_Projections/                  # Awaiting manual export from dashboard
├── D7_EIA930_Grid_Monitor/
│   └── EIA930_BALANCE_2024_Jan_Jun.csv       # 44 columns, hourly grid generation & demand
├── D8_EPA_eGRID/
│   └── egrid2023_data.xlsx                   # EPA subregion emissions & resource mix
├── D9_USGS_Water_Use/                         # Awaiting manual download from ScienceBase
├── D10_EPA_EJScreen/                          # Awaiting manual download from Zenodo
├── D11_DOE_LEAD/
│   ├── VA-2022-LEAD-data.zip
│   ├── TX-2022-LEAD-data.zip
│   ├── VA_extracted/                          # County & tract energy burden tables
│   └── TX_extracted/                          # County & tract energy burden tables
├── D12_Boavizta_Footprint_Data/
│   ├── boavizta-data-us.csv
│   └── boavizta-data-fr.csv
└── D13_Boavizta_Hardware_API/
    ├── boaviztapi_repo.zip
    └── extracted/                             # Hardware models & lifecycle factor provider
```

---

## 4. Instructions for the 3 Datasets Requiring Manual Download

For the 3 datasets protected by anti-bot verification or interactive portals:

1. **D6 (EPRI Projections):**
   - Open [https://powering-intelligence.epri.com/](https://powering-intelligence.epri.com/) in your web browser.
   - Go to the State-Level Data Center Power Dashboard or Reports section.
   - Save the report or exported state data table into `EDA Data\D6_EPRI_Load_Projections\`.

2. **D9 (USGS Water Use):**
   - Open [https://www.sciencebase.gov/catalog/item/5e43efc3e4b0edb47be84c3d](https://www.sciencebase.gov/catalog/item/5e43efc3e4b0edb47be84c3d) (or [DOI: 10.5066/F7TB15V5](https://doi.org/10.5066/F7TB15V5)) in your browser.
   - Click to download `usco2015.xlsx` (County-level water use data).
   - Place the file inside `EDA Data\D9_USGS_Water_Use\`.

3. **D10 (EPA EJScreen 2015–2024):**
   - Open [https://zenodo.org/records/14767363](https://zenodo.org/records/14767363) in your browser.
   - Complete the Cloudflare verification if prompted, scroll to "Files", and download the national or state percentile CSV.
   - Place the file inside `EDA Data\D10_EPA_EJScreen\`.
