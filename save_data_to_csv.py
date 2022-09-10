import os
import mariadb
import sys
import pandas as pd

# list of table names
table_names = ["lime_question_attributes", "lime_questions", "lime_survey_916481", "lime_survey_916481_timings"]

# connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user=os.environ["LIMESURVEY_SSH_USER"],
        password=os.environ["LIMESURVEY_SQL_PASSWORD"],
        host=os.environ["LIMESURVEY_SSH_IP"],
        port=os.environ["LIMESURVEY_DATABASE_PORT"],
        database=["LIMESURVEY_DATABASE_NAME"]
    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# get Cursor to execute sql queries
cursor = conn.cursor()

# get tables to csv
for table in table_names:
    dataFrame = cursor.execute("select * from " + table)
    pd.to_csv(f"data/raw_data/{dataFrame}", index=False)

conn.close()
