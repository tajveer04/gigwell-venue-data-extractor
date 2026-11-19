# gigwell-venue-data-extractor
Python Selenium automation for collecting venue information and exporting it to CSV.
# Gigwell Venue Data Extractor

A Python and Selenium project developed to collect venue
information from Gigwell Discover and export it to CSV.

## Features

- Applies search keywords and clears the location filter.
- Collects venue names, addresses, emails, and phone numbers.
- Extracts capacity and average ticket sales when available.
- Collects up to seven directory contacts per venue.
- Navigates through result pages.
- Exports collected information to CSV.

## Tools

- Python
- Selenium
- Google Chrome

## Installation

python -m pip install -r requirements.txt

## Current Status

This is an earlier project being prepared for portfolio use.
It has not been retested against the current website.

- Run the script from a terminal: python main.py
- Enter your own authorized Gigwell email and password when prompted.
- The password is hidden while typing.
- Output is saved as gigwell.csv beside main.py.
- Each run overwrites the existing gigwell.csv file.

The current script uses fixed delays and broad exception handling.
Missing fields or navigation failures may produce incomplete results.

## Data

Client datasets and contact lists are not included.
