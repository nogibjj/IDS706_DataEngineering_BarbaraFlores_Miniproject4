"""
Calculations library
"""
# imports
import pandas as pd

def mean_variable(path, variable):
    df = pd.read_csv(path)
    return df[variable].mean()

def median_variable(path, variable):
    df = pd.read_csv(path)
    return df[variable].median()

def count_variable(path, variable):
    df = pd.read_csv(path)
    return df[variable].sum() / df[variable].mean() 

if __name__ == "__main__":

    path = 'data/LinkedInTechJobsDataset.csv'
    variable_list = ["Total_applicants", "Employee_count", "LinkedIn_Followers"]

    results = dict()
    for i in variable_list:
        results[i] = { 
            "mean" : mean_variable(path, i) ,
            "median" : median_variable(path, i) , 
            "count" : count_variable(path, i) }
    print(results)