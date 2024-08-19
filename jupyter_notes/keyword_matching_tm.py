import pandas as pd
import re

# read course excel
courses_df = pd.read_excel('GoldLabelsBinaryDirty_Clean.xlsx')

# read keywords excel
keywords_df = pd.read_excel('final_cleaned_BestKeywordSoFar.xlsx')

# read keywords
keywords = keywords_df['Keyword'].tolist()

# define matching
def match_keyword(description, keyword):
    # Convert description to string to handle NaN values
    description = str(description)
    sub_words = keyword.split()
    for sub_word in sub_words:
        # replace '?' by any char
        if '?' in sub_word:
            sub_word = sub_word.replace('?', '[a-zA-Z]')
        if '*' in sub_word:
            # deal with *
            pattern = re.compile(re.escape(sub_word).replace('\\*', '.*'))
            if not pattern.search(description):
                return False
        else:
            # deal with non*
            pattern = re.compile(r'\b' + re.escape(sub_word) + r'\b')
            if not pattern.search(description):
                return False
    return True

# create columns
courses_df['Matched Keywords'] = ''
courses_df['matched?'] = False
courses_df['matched number'] = 0

# search for matching
for index, row in courses_df.iterrows():
    description = row['Description Clean']
    matched_keywords = [keyword for keyword in keywords if match_keyword(description, keyword)]
    courses_df.at[index, 'Matched Keywords'] = ', '.join(matched_keywords)
    if len(matched_keywords) >= 1:  # Change here to require at least 1 matches
        courses_df.at[index, 'matched?'] = True
        courses_df.at[index, 'matched number'] = len(matched_keywords)

# cal total matches
total_matches = courses_df['matched?'].sum()

# assign matches
courses_df['total matches'] = total_matches

# save results
courses_df.to_excel('matched_courses_withClean.xlsx', index=False)

print("Matching complete. Results saved to 'matched_courses_withClean.xlsx'.")
