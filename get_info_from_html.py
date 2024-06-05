from bs4 import BeautifulSoup
import pandas as pd

# Load the HTML file
file_path = '/mnt/data/Best Engineering Colleges in USA_ Fees, Scholarships, Eligibility, Courses and Salaries.html'
with open(file_path, 'r', encoding='utf-8') as file:
    page_content = file.read()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(page_content, 'html.parser')

# Extract data
universities = []

# Find the sections that contain university data
sections = soup.find_all(string=lambda text: isinstance(text, str) and "Engineering Colleges in USA" in text)

# Loop through each section to extract the relevant details
for section in sections:
    content = section.find_next('div')
    if content:
        paragraphs = content.find_all('p')
        for paragraph in paragraphs:
            text = paragraph.get_text(separator='|').strip()
            parts = text.split('|')
            if len(parts) >= 5:  # Ensure there are enough parts to unpack
                university_data = {
                    'University Name': parts[0],
                    'Program Name': parts[1],
                    'Location': parts[2],
                    'Tuition Fees': parts[3],
                    'Living Costs': 'N/A',  # Adjust this if living costs are available in the text
                    'Application Deadlines': 'N/A',  # Adjust this if deadlines are available in the text
                    'Application Fees': 'N/A',  # Adjust this if fees are available in the text
                    'Acceptance Rate': 'N/A',  # Adjust this if acceptance rates are available in the text
                    'Average Salary Post-Graduation': 'N/A'  # Adjust this if salary is available in the text
                }
                universities.append(university_data)

# Create a DataFrame
df = pd.DataFrame(universities)

import ace_tools as tools; tools.display_dataframe_to_user(name="Engineering Universities in USA", dataframe=df)

# Save to Excel
df.to_excel('/mnt/data/Engineering_Universities_in_USA.xlsx', index=False)
