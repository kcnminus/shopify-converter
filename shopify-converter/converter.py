import pandas as pd
import sys

def read_squarespace_csv(input_path):
  """Read the Squarespace CSV file into a Pandas dataframe."""
  return pd.read_csv(input_path)

def transform_data(df):
  """Transform data into Shopify format"""
  df.rename(columns=
        {'ID': 'Customer: ID',
        'Email': 'Customer: Email',
        'First Name': 'Customer: First Name',
        'Last Name': 'Customer: Last Name',
        'Order Count': 'Customer: Orders Count',
        'Shipping Province': 'Customer: State',
        'Total Spent': 'Customer: Total Spent',
        'Email Marketing: Status': 'Customer: Email Marketing Status',
        """billing info here"""
        'Billing Name': 'Billing: Name',
        'Billing Phone Number': 'Billing: Phone',
        'Billing Address 1': 'Billing: Address 1',
        'Billing Address 2': 'Billing: Address 2',
        'Billing Zip': 'Billing: Zip',
        'Billing City': 'Billing: City',
        'Billing Province/State': 'Billing: Province',
        'Billing Country': 'Billing: Country',
        """shipping info here"""
        'Shipping Name': 'Shipping: Name',
        'Shipping Phone Number': 'Shipping: Phone',
        'Shipping Address 1': 'Shipping: Address 1',
        'Shipping Address 2': 'Shipping: Address 2',
        'Shipping Zip': 'Shipping: Zip',
        'Shipping City': 'Shipping: City',
        'Shipping Province/State': 'Shipping: Province',
        'Shipping Country': 'Shipping: Country',

        }, inplace=True)
  return df
    
def write_shopify_csv(df, output_path):
  df.to_csv(output_path, index=False)

def main(input_path, output_path):
  df = read_squarespace_csv(input_path)
  transformed_df = transform_data(df)
  write_shopify_csv(transformed_df, output_path)
  print(f"Converted file saved to {output_path}")

if __name__ == "__main__":
  if len(sys.argv) != 3:
    print("Usage: python converter.py <input_path> <output_path>")
    sys.exit(1)

  input_path, output_path = sys.argv[1], sys.argv[2]
  main(input_path, output_path)
