from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

# Set up the web driver (Make sure the path to the driver is correct)
driver = webdriver.Chrome(executable_path= r"C:\Users\conta\anaconda3\Lib\site-packages\typings\selenium\webdriver\chrome\__init__.pyi")

# Open the website
url = "https://collegedunia.com/usa/engineering-universities?custom_params=[view:grid]"
driver.get(url)

# Extract data
universities = []

# Assuming the data is in a grid layout, loop through each university card
cards = driver.find_elements(By.CLASS_NAME, 'college_card_class_name')  # Replace with actual class name

for card in cards:
    name = card.find_element(By.CLASS_NAME, 'college_name_class').text.strip()  # Replace with actual class name
    program = card.find_element(By.CLASS_NAME, 'program_class').text.strip() if card.find_element(By.CLASS_NAME, 'program_class') else ''
    location = card.find_element(By.CLASS_NAME, 'location_class').text.strip() if card.find_element(By.CLASS_NAME, 'location_class') else ''
    tuition_fees = card.find_element(By.CLASS_NAME, 'fees_class').text.strip() if card.find_element(By.CLASS_NAME, 'fees_class') else ''
    living_costs = card.find_element(By.CLASS_NAME, 'living_costs_class').text.strip() if card.find_element(By.CLASS_NAME, 'living_costs_class') else ''
    application_deadlines = card.find_element(By.CLASS_NAME, 'deadlines_class').text.strip() if card.find_element(By.CLASS_NAME, 'deadlines_class') else ''
    application_fees = card.find_element(By.CLASS_NAME, 'app_fees_class').text.strip() if card.find_element(By.CLASS_NAME, 'app_fees_class') else ''
    acceptance_rate = card.find_element(By.CLASS_NAME, 'acceptance_rate_class').text.strip() if card.find_element(By.CLASS_NAME, 'acceptance_rate_class') else ''
    avg_salary = card.find_element(By.CLASS_NAME, 'avg_salary_class').text.strip() if card.find_element(By.CLASS_NAME, 'avg_salary_class') else ''
    
    universities.append({
        'University Name': name,
        'Program Name': program,
        'Location': location,
        'Tuition Fees': tuition_fees,
        'Living Costs': living_costs,
        'Application Deadlines': application_deadlines,
        'Application Fees': application_fees,
        'Acceptance Rate': acceptance_rate,
        'Average Salary Post-Graduation': avg_salary
    })

# Create a DataFrame
df = pd.DataFrame(universities)

# Save to Excel
df.to_excel('Engineering_Universities_in_USA.xlsx', index=False)

# Close the driver
driver.quit()
