import pandas as pd
import numpy
df=pd.read_excel('cc_Details_temp.xlsx')
df["Add on card fee"] = pd.to_numeric(df["Add on card fee"], errors='coerce')
df["Interest Rates (pm)"]=pd.to_numeric(df["Interest Rates (pm)"], errors='coerce')
df["International lounge access"] = df["International lounge access"].apply(lambda x: [x] if len(str(x)) == 1 else list(x))
print(df["Bank"])
bank=int(input("Enter the bank number: "))

bank_name = df.iloc[bank]["Bank"]
print(bank_name)
selected_rows=[]
selected_rows = df.loc[df["Bank"] == bank_name, "Variant"].tolist()
print(selected_rows)


variants=[]
for variant in df["Variant"]:
    for selected in selected_rows:
        if variant.find(selected) == 0:
            variants.append(variant)
for i, variant in enumerate(variants):
    print(f'{i} - {variant}')

selectV=int(input("Enter the variant number: "))

cardVariant = variants[selectV]
jf = df.loc[df["Variant"] == cardVariant, "Joining Fee"].iloc[0]
df = df.dropna(subset=['Joining Fee'])
lesser_fee_cards = df[df['Joining Fee'].astype(int) < jf]
print(f'Selected card variant: {cardVariant}, Joining fee: {jf}')

lesser_fee_cards = df[df['Joining Fee'] < jf]

if not lesser_fee_cards.empty:
    print("Cards with lesser joining fee:")
    for i, row in lesser_fee_cards.iterrows():
        print(f'Variant: {row["Variant"]}, Joining fee: {row["Joining Fee"]}')
else:
    print("No cards found with lesser joining fee")
