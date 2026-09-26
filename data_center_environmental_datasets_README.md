# Data Sources --- Data Centers & AI Data Centers Environmental Impact

## Project

**Project:** How Data Centers and AI Data Centers Affect the Environment and how can we prevent it using historical data

This repository documents publicly available datasets that can be used
to investigate relationships between data-center / AI-data-center
expansion and electricity, water, carbon emissions, energy sources,
cooling, grid, hardware, and socioeconomic/environmental conditions.

> These are potential data sources. The final EDA project will use only
> the datasets that are compatible after schema, coverage, and
> data-quality inspection.

## Dataset Sources

## Dataset Sources

| ID | Dataset / Data Source | Website / Organization | Dataset / Website Link |
|---|---|---|---|
| D1 | **AI Data Centers** | Epoch AI | https://epoch.ai/data/data-centers-documentation |
| D2 | **Generative AI Workload Power Profiles** | National Laboratory of the Rockies / DOE | https://data.nlr.gov/submissions/312 |
| D3 | **IM3 Open Source Data Center Atlas** | DOE / PNNL / OSTI | [IM3 Open Source Data Center Atlas](https://im3.pnnl.gov/visualizations)|
| D4 | **Open U.S. Data Centers Tracker** | FracTracker Alliance | https://fractracker.org/data-centers/ |
| D5 | **IM3 Projected U.S. Data Center Locations** | DOE / OSTI | [IM3 Projected U.S. Data Center Locations](https://im3.pnnl.gov/visualizations) |
| D6 | **EPRI U.S. Data Center Load Projections / Powering Intelligence** | EPRI | https://powering-intelligence.epri.com/ |
| D7 | **EIA-930 Hourly U.S. Electric Grid Monitor** | U.S. EIA | https://www.eia.gov/electricity/gridmonitor/ |
| D8 | **Emissions & Generation Resource Integrated Database (eGRID)** | U.S. EPA | https://www.epa.gov/egrid/detailed-data |
| D9 | **Water Use in the United States** | U.S. Geological Survey | https://water.usgs.gov/watuse/data/ |
| D10 | **EPA EJScreen Data, 2015–2024** | EPA / Zenodo | https://zenodo.org/records/14767363 |
| D11 | **Low-Income Energy Affordability Data (LEAD)** | DOE / OpenEI | https://catalog.data.gov/dataset/low-income-energy-affordability-data-lead-tool-2022-update |
| D12 | **Environmental Footprint Data** | Boavizta | https://github.com/Boavizta/environmental-footprint-data |
| D13 | **Hardware / Computing Environmental Data** | Boavizta | https://github.com/Boavizta/boaviztapi |

## What Each Source Provides

### D1 --- Epoch AI: AI Data Centers

AI data-center facility information and construction timelines. Data is
available for download as CSV/ZIP. **Use:** AI data-center growth,
facility timelines, location and infrastructure.

### D2 --- DOE/NLR: Generative AI Workload Power Profiles

High-resolution power-consumption traces for generative-AI workloads,
including training/inference and different compute-node configurations.
**Use:** AI workload → power-consumption analysis.

### D3 --- IM3 Open Source Data Center Atlas

Existing U.S. data-center locations with derived geographic/facility
information such as area, county and state. **Use:** Spatial
distribution and concentration of data centers.

### D4 --- FracTracker U.S. Data Centers Tracker

Existing, permitted and proposed U.S. data centers compiled from public
records and permits. **Use:** Current/planned expansion, project status,
geography and environmental/regulatory context.

### D5 --- IM3 Projected U.S. Data Center Locations

Model projections of future U.S. data-center facilities through 2035
under multiple growth and siting scenarios. **Use:** Future expansion,
power demand, siting, grid and water-stress scenarios.

### D6 --- EPRI U.S. Data Center Load Projections

Data and projections related to U.S. data-center electricity demand and
AI-driven load growth. **Use:** Current/historical load and future
electricity-demand scenarios.

### D7 --- EIA-930 Hourly Electric Grid Monitor

Hourly U.S. electricity demand, generation and interchange data.
**Use:** Connecting data-center expansion with regional electricity/grid
conditions.

### D8 --- EPA eGRID

Electricity-generation, emissions, emission-rate, resource-mix and
power-sector characteristics. **Use:** Carbon/emissions and
electricity-source analysis.

### D9 --- USGS Water Use

State, county and national water-use data across multiple categories.
**Use:** Water-resource context around data-center locations.

### D10 --- EPA EJScreen Data

Annual environmental and socioeconomic indicators at detailed geographic
levels. **Use:** Environmental and socioeconomic context around
data-center development. **Note:** Supporting dataset; not
data-center-specific.

### D11 --- DOE LEAD

Detailed household energy-affordability / energy-burden data. **Use:**
Possible community and energy-burden analysis. **Note:** Supporting
dataset; not data-center-specific.

### D12 --- Boavizta Environmental Footprint Data

Environmental-footprint data for ICT equipment, including
data-center-related equipment such as servers and network equipment.
**Use:** Hardware lifecycle footprint, embodied carbon and energy
demand.

### D13 --- Boavizta Hardware / Computing Environmental Data

Reference data and methodologies for environmental impacts of digital
equipment and computing systems. **Use:** Hardware-level environmental
analysis for computing/AI infrastructure.

## Project Data Architecture

``` text
AI DATA CENTERS
      |
      +--> Epoch AI --------------------> AI growth / facilities
      |
      +--> NLR GenAI Power Profiles -----> AI workload / power
      |
      +--> IM3 / FracTracker ------------> locations / expansion
      |
      +--> EPRI / EIA-930 ---------------> electricity / grid
      |
      +--> EPA eGRID --------------------> emissions / energy mix
      |
      +--> USGS --------------------------> water-resource context
      |
      +--> EJScreen ----------------------> environmental + socioeconomic context
      |
      +--> Boavizta ----------------------> hardware footprint
      |
      +--> IM3 projected -----------------> future scenarios
```

## Final Project Goal

Use historical/current data to:

1.  Clean and integrate compatible datasets.
2.  Analyze missing values and outliers.
3.  Perform univariate, bivariate and multivariate EDA.
4.  Study temporal and geographic patterns.
5.  Analyze relationships between data-center expansion and
    environmental/resource indicators.
6.  Engineer useful features.
7.  Apply appropriate ML/predictive methods.
8.  Estimate future resource demand or environmental pressure.
9.  Explore future growth/mitigation scenarios.

**Important:** The analysis should investigate relationships in the data
rather than assume beforehand that data centers or AI data centers cause
a specific environmental outcome.

## Next Step

**Dataset inspection → schema comparison → compatible datasets → data
integration → cleaning → EDA → feature engineering → ML →
future/scenario analysis.**
