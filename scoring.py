import pandas as pd

# Define the fields for each credit card
fields = ['Card Name', 'Welcome Bonus', 'Reward Rates', 'Travel Benefits', 'Insurance Benefits', 
          'Movie & Dining Benefits', 'Zero Liability Protection', 'Interest Rates', 'Cash Advance Fees']

# Create a dictionary to store the credit card data


# Define the weights for each field
weights = {''}

# Create a dataframe from the card data
df = pd.DataFrame(card_data, columns=fields)

# Add a new column to store the weighted score
df['Weighted Score'] = 0

# Calculate the weighted score for each card
for index, row in df.iterrows():
    weighted_score = 0
    for field in fields[1:]:
        weighted_score += row[field] * weights[field]
    df.at[index, 'Weighted Score'] = weighted_score

# Sort the dataframe by the weighted score in descending order
df.sort_values(by='Weighted Score', ascending=False, inplace=True)

# Display the result
print(df)
