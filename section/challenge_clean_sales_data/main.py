def clean_sales_data(sales_records):
    import pandas as pd
    df = pd.DataFrame(sales_records)
    df["units_sold"] = df["units_sold"].fillna(0)
    df["revenue"]    = df["revenue"].fillna(0)
    df["product"]    = df["product"].str.title()
    return df.to_dict(orient="records")

sales_data = [
    {'date': '2024-06-01', 'product': 'laptop', 'units_sold': 10, 'revenue': 15000},
    {'date': '2024-06-02', 'product': 'Laptop', 'units_sold': None, 'revenue': 14500},
    {'date': '2024-06-03', 'product': 'tablet', 'units_sold': 5, 'revenue': None},
    {'date': '2024-06-04', 'product': 'SMARTphone', 'units_sold': None, 'revenue': None},
]

cleaned_sales = clean_sales_data(sales_data)
print(cleaned_sales)
