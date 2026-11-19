# Gigwell Venue Data Extractor

A Python and Selenium browser automation project that collects
venue information from Gigwell Discover and exports it to CSV.

Originally developed for a data collection project and now
being prepared for portfolio presentation.

## Features

- Logs in using credentials entered by the user.
- Applies keyword exclusions to the venue search.
- Clears the location filter.
- Collects venue details and up to seven directory contacts.
- Navigates through search result pages.
- Exports results to a structured CSV file.

## Collected Fields

Venue information:
- Name
- Address
- Email
- Phone
- Capacity
- Average ticket sales, when available

Directory contacts:
- Name
- Job title
- Phone
- Email

## Requirements

- Python 3
- Google Chrome
- An authorized Gigwell Discover account with access to the data
- Internet connection

## Installation

Download the repository and open a terminal in its folder.

Install the dependency:

```bash
python -m pip install -r requirements.txt
```

## Usage

Run:

```bash
python main.py
```

Enter your own Gigwell email and password when prompted.
The password is hidden while typing.

The script opens Chrome and starts the collection workflow.

## Output

Results are saved as `gigwell.csv` in the same folder as `main.py`.

Each run overwrites the existing output file.
Move or rename previous results before running again.

## Search Settings

The current keyword exclusions are:

- -nightclub
- -bar
- -restaurant
- -club

These can be changed in the `keywords` list in `main.py`.

The minimum-capacity filter is currently commented out.

## Project Files

- `main.py` — browser automation and CSV export
- `requirements.txt` — Python dependency
- `.gitignore` — excludes generated data and local files
- `README.md` — project documentation

## Current Status and Limitations

This is a historical project. The updated version has not been
retested against the current Gigwell website.

- Website layout changes may require XPath updates.
- Fixed delays may be insufficient on slower connections.
- Missing fields are generally left blank.
- If a directory contact field is missing, the entire contact
  may be skipped.
- Navigation can invalidate stored venue elements and cause
  listings to be skipped.
- Pagination errors may be reported as completion.
- Broad exception handling can result in incomplete output.

Review and test the script before relying on its results.

## Data and Credentials

Login credentials are entered at runtime rather than stored
in the current source code.

Client datasets and contact lists are not included.

Use only with an account and data access you are authorized
to use, following the service's applicable terms.

## Author

Fayez Mahmud
