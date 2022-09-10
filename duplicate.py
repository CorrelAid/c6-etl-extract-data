import pandas as pd
import numpy as np


filename_list = ['lime_question_attributes.csv', 'lime_questions.csv', 'lime_survey_916481.csv', 'lime_survey_916481_timings.csv']

clean_filenames_list = ['lime_question_attributes_clean.csv', 'lime_questions_clean.csv', 'lime_survey_916481_clean.csv', 'lime_survey_916481_timings_clean.csv']

for rawfile,clean_filename in zip(filename_list, clean_filenames_list):
    pd.read_csv(f"data/raw_data/{rawfile}")
    df.drop_duplicates(keep='first', inplace=True)
    df.to_csv(f"data/clean_data/{clean_filename}", index=False)