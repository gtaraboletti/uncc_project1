"""
A script for creating a state summary CSV file from the districts.csv file.
Should be run after "create_districts_csv.py".
"""

import pandas as pd
import sqlite3

INPUT_FILENAME = 'districts.csv'
OUTPUT_FILENAME = 'states.csv'

SCHEMA = ['STATE',
          'ENROLL',
          'NAME',
          'YRDATA',
          'TOTALREV',
          'TFEDREV',
          'TSTREV',
          'TLOCREV',
          'TOTALEXP',
          'TCURINST',
          'TCURSSVC',
          'TCURONON',
          'TCAPOUT']

query = \
    '''
    SELECT STATE,
    YRDATA AS YEAR,
    SUM(ENROLL) AS ENROLL,
    SUM(TOTALREV) AS TOTAL_REVENUE,
    SUM(TFEDREV) AS FEDERAL_REVENUE,
    SUM(TSTREV) AS STATE_REVENUE,
    SUM(TLOCREV) AS LOCAL_REVENUE,
    SUM(TOTALEXP) AS TOTAL_EXPENDITURE,
    SUM(TCURINST) AS INSTRUCTION_EXPENDITURE,
    SUM(TCURSSVC) AS SUPPORT_SERVICES_EXPENDITURE,
    SUM(TCURONON) AS OTHER_EXPENDITURE,
    SUM(TCAPOUT) AS CAPITAL_OUTLAY_EXPENDITURE
    FROM school_money
    GROUP BY STATE, YRDATA
    ORDER BY YRDATA;
    '''


def main():
    # Notify user
    print('Parsing ' + str(INPUT_FILENAME) + '...')

    # Create a temporary SQL database populated with district data
    con = sqlite3.connect(':memory:')
    cur = con.cursor()
    df = pd.read_csv(INPUT_FILENAME)
    df.to_sql(name='school_money', con=con, if_exists='replace')
    con.commit()

    # Run a query to aggregate data by state
    output = pd.read_sql(sql=query, con=con)
    output.to_csv(OUTPUT_FILENAME, index=False)


if __name__ == '__main__':
    print('Beginning data conversion...')
    print('')
    main()
    print('')
    print('Finished.')
