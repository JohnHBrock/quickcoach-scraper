# QuickCoach Data Export

Export your workout history from QuickCoach to CSV files.

## Installation

1. **Install uv** (Python package manager):
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. **Install Chrome** (if not already installed):
   - Download from https://www.google.com/chrome/

3. **Clone or download this repository**

That's it! Dependencies (Selenium and ChromeDriver) are installed automatically when you run the script.

## Usage

Run the scraper with your QuickCoach client URL:

```bash
uv run python quickcoach_scrape.py --slug pt/fitcojohn
```

Replace `pt/fitcojohn` with your actual client path (the part after `app.quickcoach.fit/` in your QuickCoach URL).

### What it does

- Opens QuickCoach in an automated browser
- Extracts all workout history across all your plans
- Creates two CSV files:
  - `quickcoach-{slug}.csv` - Long format (one row per exercise/date)
  - `quickcoach-pivot-{slug}.csv` - Wide format (exercises as rows, dates as columns)

### Options

- `--delay 0.2` - Add delay between exercises (default: 0.15 seconds)
- `--headful` - Show browser window while running (useful for debugging)
- `--skip-pivot` - Only create the long-format CSV

### Example

```bash
# Basic usage
uv run python quickcoach_scrape.py --slug pt/fitcojohn

# With custom delay and visible browser
uv run python quickcoach_scrape.py --slug pt/fitcojohn --delay 0.3 --headful
```

## Troubleshooting

- **"No plan URLs found"**: Make sure you're logged into QuickCoach in your default Chrome profile
- **Chrome not found**: Make sure Chrome is installed in the default location
