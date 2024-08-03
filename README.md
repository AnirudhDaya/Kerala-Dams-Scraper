# Dam Data Scraper

This project is a Python script designed to scrape data from [KSEB DAM website](https://dams.kseb.in/?page_id=45) and save the data into a JSON file. The data pertains to dam reservoirs and includes various attributes such as water levels, storage capacities, and inflow/outflow measurements.

## Prerequisites

- Python 3.x
- `requests` library
- `beautifulsoup4` library

## Installation

1. Clone the repository or download the script.

2. Install the required libraries using `pip`:
    ```bash
    pip install requests beautifulsoup4
    ```

## Usage

1. Ensure you have the necessary dependencies installed.

2. Run the script:
    ```bash
    python dam_data_scraper.py
    ```

3. The script will scrape the dam data from the specified webpage and save it to a JSON file in the current directory. The filename will follow the format `dam_data_<date>.json`.

## Error Handling

In case of an error during the scraping process, the script will return a JSON object containing the current date and the error message. The structure of the JSON object will be:
```json
{
  "date": "dd.mm.yyyy",
  "error": "Error message"
}
```

## Example Output

The script will output a JSON file with the following structure:

```json
{
  "date": "03.08.2024",
  "data": [
    {
      "Sl. No.": "1",
      "Name of Dam / Reservoir": "IDUKKI",
      "District": "IDK",
      "MWL (metre)": "2408.5 ft",
      "FRL (metre)": "2403 ft",
      "Spillway Crest Level (metre)": "2373 ft",
      "Live Storage at FRL (MCM)": "1459.49",
      "Rule level(metre)": "2383.53 ft",
      "Blue level(metre)": "2375.53",
      "Orange level(metre)": "2381.53",
      "Red Level(metre)": "2382.53",
      "Todays Water level (metre)": "2366.90Ft",
      "Todays Live Storage(MCM)": "890.136",
      "% Storage w.r.t Live Storage at FRL": "60.99%",
      "Same day previous year Water level (metre)": "2332.76",
      "Same day previous year Live Storage (MCM)": "469.161",
      "Inflow (cumecs)": "207.96",
      "Power House Discharge(cumecs)": "98.13",
      "Spillway release (cumecs)": "0.00",
      "Total Outflow (cumecs)": "98.13",
      "Rainfall (mm)": "11.00",
      "Remarks": ""
    },
    ...
  ]
}
```

## License

This project is licensed under the MIT License.

## Acknowledgements

This project uses the following libraries:
- `requests` for making HTTP requests.
- `beautifulsoup4` for parsing HTML content.
