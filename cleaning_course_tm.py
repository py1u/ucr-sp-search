import pandas as pd

# Read the Excel file
course_info_df = pd.read_excel('UCR_courses_only.xlsx')

# Define a function to convert words to lowercase if they are capitalized initially (not all uppercase)
def convert_detail_to_lowercase(detail):
    words = detail.split()
    new_words = []
    for word in words:
        # Check if the word is title-cased, meaning the first letter is uppercase and the rest are lowercase
        if word.istitle():
            new_words.append(word.lower())
        else:
            new_words.append(word)
    return ' '.join(new_words)

# Apply the function to the 'course_text_narrative' column
course_info_df['course_text_narrative'] = course_info_df['course_text_narrative'].apply(lambda x: convert_detail_to_lowercase(str(x)))

# Save the results to a new Excel file
course_info_df.to_excel('UCR_course_clean.xlsx', index=False)

print("Processed and saved to 'UCR_course_clean.xlsx'.")
