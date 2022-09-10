import pandas
import os
import sys
import psycopg2

clean_filenames_list = ['lime_question_attributes_clean.csv', 'lime_questions_clean.csv', 'lime_survey_916481_clean.csv', 'lime_survey_916481_timings_clean.csv']
table_names = ['lime_question_attributes', 'lime_questions', 'lime_survey_916481', 'lime_survey_916481_timings']

# Connect to MariaDB Platform
try:
    conn = psycopg2.connect(
        user=os.environ["COOLIFY_USER"],
        password=os.environ["COOLIFY_PASSWORD"],
        host=os.environ["COOLIFY_HOST"],
        port=os.environ["COOLIFY_PORT"],
        database=["cl7swkr4f002e0omrf9m3c974"]
    )
except mariadb.Error as e:
    print(f"Error connecting to PostGreSQL Platform: {e}")
    sys.exit(1)


for clean_filename,table  in zip(filename_list, clean_filenames_list):
	df = pd.read_csv(clean_filename)
	df.to_sql(table, conn, if_exists='append')

dbConnection.close()