import pandas as pd

print("Cleaning 01_samples...")
df = pd.read_csv("01_samples.csv", sep=';', encoding='utf-8-sig', dtype=str)
df = df.loc[:, ~df.columns.str.contains('Unnamed')]
df['sample_price_before_vat'] = df['sample_price_before_vat'].str.replace(',', '', regex=False)
df.to_csv("01_samples_CLEANED.csv", index=False, encoding='utf-8-sig')

print("Cleaning finance...")
df = pd.read_csv("finance.csv", sep=';', encoding='utf-8-sig', dtype=str)
for col in ['unit_price','subtotal_before_vat','vat_amount','total_amount','paid_amount','outstanding_amount']:
    if col in df.columns:
        df[col] = df[col].str.replace(',', '', regex=False)
if 'student_discount_rate' in df.columns:
    df['student_discount_rate'] = df['student_discount_rate'].str.replace('%','', regex=False)
if 'vat_rate' in df.columns:
    df['vat_rate'] = df['vat_rate'].str.replace('%','', regex=False)
df.to_csv("finance_CLEANED.csv", index=False, encoding='utf-8-sig')

print("Cleaning results...")
df = pd.read_csv("results.csv", sep=';', encoding='utf-8-sig', dtype=str)
df.to_csv("results_CLEANED.csv", index=False, encoding='utf-8-sig')

print("All done!")