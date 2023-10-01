# Your name:
# Your student id:
# Your email:
# List who you have worked with on this project:

import csv
import unittest



def load_csv(filename):

    """

    Load employee data from a CSV file.



    Args:

        filename (str): The name of the CSV file containing employee data.



    Returns:

        dict: A dictionary where each key is an employee ID and each value is another dictionary

        containing demographic categories ('gender', 'race', and 'hire_year') as keys and their corresponding data as values.

        The 'hire_year' is converted into an integer.



    """

    pass

    



def split_by_hire_year(employees, hire_year):

    """

    Split employee data into two dictionaries based on hire year.



    Args:

        employees (dict): A dictionary where each key is an employee ID and each value is a dictionary

        containing employee data, including 'hire_year'.

        hire_year (int): An integer to designate the selected year used to divide the employees dict



    Returns:

        tuple: A tuple containing two dictionaries:

        1. A dictionary with employees hired before 1964.

        2. A dictionary with employees hired in 1964 or later.



    """

    pass

    



def count_race_or_gender(employees):

    """

    Count the number of employees belonging to each race and gender category.



    Args:

        employees (dict): A dictionary where each key is an employee ID and each value is a dictionary

        containing employee data, including 'race' and 'gender'.



    Returns:

        dict: A dictionary containing two keys: 'race' and 'gender'. Each key maps to a sub-dictionary

        with race or gender categories as keys and their corresponding counts as values.



    """

    pass





def count_race_and_gender(employees):

    """

    Count the number of employees within each combination of race and gender.



    Args:

        employees (dict): A dictionary where each key is an employee ID and each value is a dictionary

        containing employee data, including 'race' and 'gender'.



    Returns:

        dict: A dictionary where keys represent combinations of race and gender in the format "Race_Gender",

        and values represent the count of employees within each combination.



    """

    pass





def write_csv(data, filename):

    """

    Write data to a CSV file.



    Args:

        data (dict): A dictionary containing data to be written to the CSV file.

        filename (str): The name of the CSV file to be created.



    """

    pass


#EXTRA CREDIT
def count_employees_by_year(employees):

    """

    Count the number of employees who were hired each year of each gender of each race.



    Args:

        employees (dict): A dictionary where each key is an employee ID and each value is a dictionary

        containing employee data, including 'race' and 'gender'.

    Returns:

        dict: A collection of nested dictionaries where the sequential keys are a hiring year, a race, and a gender in that order

        and the innermost values represent the count of employees whose information matches the hiring year, race, and gender keys.



    """

    pass




class TestEmployeeDataAnalysis(unittest.TestCase):

    def setUp(self):
        
        #Set up any variables you will need for your test cases

        #Feel free to use smaller_dataset.csv for your test cases so that you can verify the correct output

        pass



    def test_load_csv(self):

        # Your test code for load_csv goes here

        # Write a test case that checks for the length of the dictionary.

        
        # Write a test case that checks for the length of the inner dictionary value of the first (key, value) pair.

        pass



    def test_split_by_hire_year(self):

        # Your test code for split_by_hire_year goes here

        #Test that the function correctly separates employees hired before 1964 from those hired in 1964 or later.

        pass



    def test_count_race_or_gender(self):

        # Your test code for count_race_or_gender goes here

        #Test that there are only two keys in the returned dictionary
        
        
        #Test that the function accurately counts the number of employees belonging to each race and gender category.

        pass



    def test_count_race_and_gender(self):

        # Your test code for count_race_and_gender goes here

        #Test that there are the correct number of keys in the dictionary representing each combination of race and gender in this dataset.
         
        
        # Test that the function correctly counts the number of employees within each combination of race and gender.
        
        pass






#You do not need to change anything in the main() function

def main():

    # Load employee data from the CSV file

    employee_data = load_csv('GM_employee_data.csv')



    # Task 1: Split employees by hire year

    employees_before_1964, employees_after_1964 = split_by_hire_year(employee_data, 1964)



    # Task 2: Count employees by race or gender before and after layoffs

    race_gender_counts_total = count_race_or_gender(employee_data)

    race_gender_counts_after_layoffs = count_race_or_gender(employees_before_1964)



    # Task 3: Count employees by race and gender combinations before and after layoffs

    gendered_race_counts_total = count_race_and_gender(employee_data)

    gendered_race_counts_after_layoffs = count_race_and_gender(employees_before_1964)



    # Print and interpret the results

    print("Analysis Results:")

    print("--------------------------------------------------------")



    # Task 1: Splitting employees

    print("Task 1: Split Employees by Hire Year")

    print(f"Number of employees hired total: {len(employee_data)}")

    print(f"Number of employees after layoffs: {len(employees_before_1964)}")

    print("--------------------------------------------------------")



    # Task 2: Comparing race or gender of all employees before and after layoffs

    print("Task 2: Comparing Race and Gender Before and After Layoffs")

    print("Category: Before Layoffs ---> After Layoffs")

    print("Race:")

    for category, count_before in race_gender_counts_total['race'].items():

        count_after = race_gender_counts_after_layoffs['race'].get(category, 0)

        print(f"\t{category}: {count_before} ---> {count_after}")



    print("Gender:")

    for category, count_before in race_gender_counts_total['gender'].items():

        count_after = race_gender_counts_after_layoffs['gender'].get(category, 0)

        print(f"\t{category}: {count_before} ---> {count_after}")



    print("--------------------------------------------------------")



    # Task 3: Comparing race and gender combinations before and after layoffs

    print("Task 3: Comparing Gendered Race Combinations Before and After Layoffs")

    print("Category: Before Layoffs ---> After Layoffs")

    print("Gendered races:")

    for category, count_before in gendered_race_counts_total.items():

        count_after = gendered_race_counts_after_layoffs.get(category, 0)

        print(f"\t{category}: {count_before} ---> {count_after}")



    print("--------------------------------------------------------")



    write_csv(gendered_race_counts_total, "GM_employee_data_before_layoffs.csv")

    write_csv(gendered_race_counts_after_layoffs, "GM_employee_data_after_layoffs.csv")







if __name__ == "__main__":

    unittest.main(verbosity=2)

    main()



