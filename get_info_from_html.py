from bs4 import BeautifulSoup
import pandas as pd

# Load the HTML file
file_path = 'path/to/your/Best Engineering Colleges in USA_ Fees, Scholarships, Eligibility, Courses and Salaries.html'
with open(file_path, 'r', encoding='utf-8') as file:
    page_content = file.read()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(page_content, 'html.parser')

# Extract data
universities = []

# Define the patterns to search for university data
university_data_patterns = [
    "University of California",
    "Cornell University"
]

# Loop through the patterns to extract the relevant details
for pattern in university_data_patterns:
    for data in soup.find_all(string=lambda text: text and pattern in text):
        # Extract the text content
        text = data.strip()
        # Parse the text content
        parts = text.split("\r\n")
        if len(parts) >= 4:  # Ensure there are enough parts to unpack
            university_data = {
                'University Name': parts[0].strip(),
                'Program Name': parts[3].strip(),
                'Location': parts[1].strip(),
                'Tuition Fees': parts[2].strip(),
                'Living Costs': 'N/A',  # Adjust this if living costs are available in the text
                'Application Deadlines': 'N/A',  # Adjust this if deadlines are available in the text
                'Application Fees': 'N/A',  # Adjust this if fees are available in the text
                'Acceptance Rate': 'N/A',  # Adjust this if acceptance rates are available in the text
                'Average Salary Post-Graduation': 'N/A'  # Adjust this if salary is available in the text
            }
            universities.append(university_data)

# Create a DataFrame
df = pd.DataFrame(universities)

# Save to Excel
df.to_excel('Engineering_Universities_in_USA.xlsx', index=False)

# Display the DataFrame
print(df)
