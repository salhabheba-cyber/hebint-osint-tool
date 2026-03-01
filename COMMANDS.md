# 🚀 HEBINT - Complete Commands Guide

## All commands needed to install, run, and use HEBINT

---

## 📥 INSTALLATION COMMANDS

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/hebint.git
cd hebint

 Set Up Virtual Environment:
# Linux/macOS
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate

Install Dependencies:
pip install -r requirements.txt

Verify Installation:
pip list
# Should show: requests, colorama, tqdm

 RUNNING THE TOOL:
# Make sure you're in the hebint directory
cd ~/path/to/hebint

# Activate virtual environment (if not already)
source venv/bin/activate  # Linux/macOS
# or
venv\Scripts\activate     # Windows

# Run the tool
python modules/hebint_username.py

Using the Launcher Script (Linux/macOS):
# Make launcher executable
chmod +x hebint

# Run it
./hebint

Example 1: Search a simple username
python modules/hebint_username.py
# When prompted, enter: johndoe

Example 2: Search with underscore
python modules/hebint_username.py
# Enter: john_doe

Example 3: Search with spaces
python modules/hebint_username.py
# Enter: john doe
# The tool automatically tries variations


Search Arabic username
python modules/hebint_username.py
# Enter: أحمد_خليل

Check Saved JSON Files
# Go to data folder
cd data

# List all saved results
ls -la

# View the latest result
cat username_latest.json

# View specific result
cat username_20240301_123456.json

# Pretty print JSON (easier to read)
python -m json.tool username_20240301_123456.json

Count Results
# Count how many platforms found
grep -c '"exists": true' data/username_*.json

Update Dependencies
pip install --upgrade -r requirements.txt

Recreate Virtual Environment (if issues)
# Linux/macOS
deactivate
rm -rf venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Windows
deactivate
rmdir /s venv
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

Check Python Version
python --version
# Should be 3.8 or higher

Linux/macOS - Method 1: Alias (Easiest)
# Add to bashrc
echo "alias hebint='cd ~/path/to/hebint && source venv/bin/activate && python modules/hebint_username.py'" >> ~/.bashrc

# Reload bashrc
source ~/.bashrc

# Now use from anywhere
hebint

Linux/macOS - Method 2: Symbolic Link
# Make launcher executable
chmod +x ~/path/to/hebint/hebint

# Create symlink
sudo ln -s ~/path/to/hebint/hebint /usr/local/bin/hebint

# Now use from anywhere
hebint

Windows - Create Batch File:
@echo off
cd C:\path\to\hebint
call venv\Scripts\activate
python modules\hebint_username.py
pause

Search JSON for Facebook Results
grep -A 5 -B 5 "Facebook" data/username_*.json

Search for Instagram
grep -A 5 -B 5 "Instagram" data/username_*.json

Search for GitHub
grep -A 5 -B 5 "GitHub" data/username_*.json

Extract All Found URLs
grep -o '"url": "[^"]*"' data/username_*.json | cut -d '"' -f 4


If you get "ModuleNotFoundError"
pip install -r requirements.txt --upgrade

If colors don't work
pip install colorama --upgrade

If you get "Permission denied"
chmod +x modules/hebint_username.py
chmod +x hebint

If you get "No such file or directory"
# Check your current directory
pwd
# Should be in hebint folder

# List files
ls -la
# Should see modules/, hebint, requirements.txt

If virtual environment won't activate
# Linux/macOS
source venv/bin/activate

# If that fails, recreate venv
rm -rf venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

 QUICK REFERENCE - ALL COMMANDS IN ONE PLACE
# Installation
git clone https://github.com/YOUR_USERNAME/hebint.git
cd hebint
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
pip install -r requirements.txt

# Run
python modules/hebint_username.py

# View results
ls data/
cat data/username_latest.json

# Global command (alias)
echo "alias hebint='cd ~/path/to/hebint && source venv/bin/activate && python modules/hebint_username.py'" >> ~/.bashrc
source ~/.bashrc
hebint

# Update
git pull
pip install -r requirements.txt --upgrade

Save Output to File
python modules/hebint_username.py | tee output.txt

Run in Background
nohup python modules/hebint_username.py &

Schedule Regular Scans (Linux/macOS)
# Add to crontab (runs daily at 2am)
0 2 * * * cd /path/to/hebint && source venv/bin/activate && python modules/hebint_username.py < username.txt


Batch Process Multiple Usernames
Create usernames.txt:
johndoe
janedoe
bobsmith

Then run:
while read username; do
    echo "Searching: $username"
    echo "$username" | python modules/hebint_username.py
done < usernames.txt

📞 NEED HELP?
Open an issue on GitHub: https://github.com/YOUR_USERNAME/hebint/issues

Check the README.md for more details

Contact the author

<div align="center">
🚀 Happy Investigating with HEBINT! 🕵️

</div> ```
