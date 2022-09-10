# Get raw data
python get_raw_data.py

# Save the raw data from limesurvey server to coolify server as a backup
scp -r ls_test@116.203.20.255:/data/raw_data coolify@116.203.20.255:/data/raw_data

# Deduplicate the data
python deduplicate_data.py

# Save the clean data from limesurvey server to coolify server as a backup
scp -r ls_test@116.203.20.255:/data/clean_data coolify@116.203.20.255:/data/clean_data

# Append clean data to Coolify Database
python append_coolify_db.pythonpython append_coolify_db.py
