from faker import Faker
import pandas as pd
from datetime import datetime
import sys
import argparse
import uuid

argParser = argparse.ArgumentParser()
argParser.add_argument("-r", "--records", help="number of records", default=100000)
argParser.add_argument("-f", "--files", help="number of number of files",default=1)
args = argParser.parse_args()

def data_generator(out_file,number_of_records):
    fake = Faker()
    data_list = []
    columns_list = ['customer_id','FirstName', 'LastName','Gender','PhoneNumber','Occupation','Company','PersonalEmail','OfficialEmail','ingestion_date']
    for val in range(number_of_records):
        fake_date = fake.date_between_dates(date_start=datetime(2024,1,1))
        data_list.append([str(uuid.uuid4()),fake.first_name(), fake.last_name(), fake.profile()['sex'],fake.phone_number(), fake.job(), fake.company(), fake.email(), fake.company_email(),fake_date])
        sys.stdout.write("\n")
        sys.stdout.write("\033[F")
        sys.stdout.write(str(val+1)+' rows has been generated.')
        sys.stdout.flush()
        fake.unique.clear()
    df = pd.DataFrame(data_list,columns=columns_list)
    df.to_csv(out_file, mode='w',index = False)
    del df

number_of_files = int(args.files)
rnum = int(args.records)

i=1
while i <= number_of_files:
    data_generator(out_file= 'sample_data.csv', number_of_records=rnum)
    i += 1

    