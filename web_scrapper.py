from bs4 import BeautifulSoup
import pandas as pd

# Load the HTML file
file_path = r'E:\timepass\AI-ART\Best Engineering Colleges in USA_ Fees, Scholarships, Eligibility, Courses and Salaries.html'
with open(file_path, 'r', encoding='utf-8') as file:
    page_content = file.read()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(page_content, 'html.parser')

# Extract data
universities = []

# Find all the relevant sections containing the college data
college_sections = soup.find_all('div', class_='jsx-3157505857 clg-head d-flex')

for section in college_sections:
    try:
        university_name = section.find('a').text.strip()
    except AttributeError:
        university_name = 'N/A'

    try:
        location = section.find('span', class_='jsx-3157505857 location-badge').text.strip()
    except AttributeError:
        location = 'N/A'

    # Find the sibling paragraphs for the program details
    next_sibling = section.find_next_sibling('div')
    if next_sibling:
        programs = next_sibling.find_all('p')
        for program in programs:
            details = program.get_text(separator='|').split('|')
            if len(details) >= 2:
                program_name = details[0].strip()
                tuition_fees = details[1].strip()

                university_data = {
                    'University Name': university_name,
                    'Program Name': program_name,
                    'Location': location,
                    'Tuition Fees': tuition_fees,
                    'Living Costs': 'N/A',  # Adjust this if living costs are available in the text
                    'Application Deadlines': 'N/A',  # Adjust this if deadlines are available in the text
                    'Application Fees': 'N/A',  # Adjust this if fees are available in the text
                    'Acceptance Rate': 'N/A',  # Adjust this if acceptance rates are available in the text
                    'Average Salary Post-Graduation': 'N/A'  # Adjust this if salary is available in the text
                }
                universities.append(university_data)
    else:
        print(f"Next sibling not found for university: {university_name}")

# Create a DataFrame
df = pd.DataFrame(universities)

# Save to Excel
df.to_excel('Engineering_Universities_in_USA2.xlsx', index=False)

# Display the DataFrame
print(df)
