# QuickCoach Data Export

Export your workout history from QuickCoach to CSV files.

## Usage

### Run directly with uvx

```bash
uvx quickcoach-export --slug pt/fitcojohn
```

Replace `pt/fitcojohn` with your actual client path (the part after `app.quickcoach.fit/` in your QuickCoach URL).

**Requirements:**
- [uv](https://docs.astral.sh/uv/getting-started/installation/) installed: `curl -LsSf https://astral.sh/uv/install.sh | sh`
- Chrome browser installed

### Run from local repository (for development)

1. **Install uv** (if not already installed):
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. **Install Chrome** (if not already installed):
   - Download from https://www.google.com/chrome/

3. **Clone this repository and navigate to it**

4. **Run the script:**
   ```bash
   uv run quickcoach-export --slug pt/fitcojohn
   ```

Dependencies (Selenium and ChromeDriver) are installed automatically.

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
uvx quickcoach-export --slug pt/fitcojohn

# With custom delay and visible browser
uvx quickcoach-export --slug pt/fitcojohn --delay 0.3 --headful

# From local repo
uv run quickcoach-export --slug pt/fitcojohn
```

## Troubleshooting

- **"No plan URLs found"**: Make sure you're logged into QuickCoach in your default Chrome profile
- **Chrome not found**: Make sure Chrome is installed in the default location
