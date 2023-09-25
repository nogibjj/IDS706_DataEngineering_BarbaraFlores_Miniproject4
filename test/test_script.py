from script import aggregate_statistics


def test_aggregate_statistics():

     results = aggregate_statistics(
        'LinkedInTechJobsDataset.csv', 
        ["Total_applicants", "Employee_count", "LinkedIn_Followers"]
        )
     assert results['Total_applicants']["count"] == 811
     assert results['Employee_count']["count"] == 811
     assert results['LinkedIn_Followers']["count"] == 811


if __name__ == "__main__":
    test_aggregate_statistics()
