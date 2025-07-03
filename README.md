# DataAgentTest

This repository contains a sample GA4 export (`RunSensible_Acquisition_Table.csv`).

A script `ga4_analysis.py` is provided to load, inspect, analyze and visualize the CSV data.

## Usage

```bash
pip install -r requirements.txt  # installs pandas, matplotlib and seaborn
python ga4_analysis.py
```

The script prints dataset information and generates two PNG plots:

- `top_sources_by_views.png` – bar chart of the top 10 sources by views.
- `bounce_vs_duration.png` – scatter plot of bounce rate vs average session duration.

These images are created when you run the script and are not stored in the repository.

