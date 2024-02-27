word = "regression_automated_cases"

new_list = ["all_regression_tests", "to_automate_tests", "all_automated_tests", "all_manual_tests", "archive_tests",
            "regression_automated_cases", "regression_manual_cases"]
list_of_suites = ["ALL REGRESSION TESTS", "TO AUTOMATE TESTS", "ALL AUTOMATED TESTS", "ALL MANUAL TESTS",
                  "ARCHIVE TESTS", "REGRESSION AUTOMATED CASES", "REGRESSION MANUAL CASES"]



upper_word = word.split("_")
upper_word_1 = word.replace("_", " ").upper()

for _ in new_list:
    print(_.replace("_", " ").upper())


my_dict = dict(zip(list_of_suites, new_list))
print(my_dict)