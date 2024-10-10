import pandas as pd

# Load the CSV files
CUSTOMERS_PATH = 'rvo03_lab-2/bakery/customers.csv'
GOODS_PATH = 'rvo03_lab-2/bakery/goods.csv'
ITEMS_PATH = 'rvo03_lab-2/bakery/items.csv'
RECEIPTS_PATH = 'rvo03_lab-2/bakery/receipts.csv'

# Read the CSV files into DataFrames
customers_df = pd.read_csv(CUSTOMERS_PATH)
goods_df = pd.read_csv(GOODS_PATH)
items_df = pd.read_csv(ITEMS_PATH)
receipts_df = pd.read_csv(RECEIPTS_PATH)


def generate_insert_statements(df, table_name):
    """
    Generates INSERT statements from a pandas DataFrame for the given table name.
    """
    insert_statements = []

    for _, row in df.iterrows():
        columns = ', '.join(row.index)
        # Replace single quotes in string values to escape them for SQL
        values = []
        for v in row.values:
            if isinstance(v, str):
                # Escape single quotes by doubling them up
                escaped_value = v.replace("'", "''").strip()
                values.append(f"'{escaped_value}'")
            else:
                values.append(str(v))

        # Join the processed values into a single string for SQL statement
        values_str = ', '.join(values)
        insert_statement = f"INSERT INTO {table_name} ({columns}) VALUES ({values_str});"
        insert_statements.append(insert_statement)

    return insert_statements


# Generate insert statements for Airlines, Airports, and Flights tables
customers_inserts = generate_insert_statements(customers_df, 'customers')
goods_inserts = generate_insert_statements(goods_df, 'goods')
items_inserts = generate_insert_statements(items_df, 'items')
receipts_inserts = generate_insert_statements(receipts_df, 'receipts')

# Combine all insert statements
all_inserts = customers_inserts + goods_inserts + items_inserts + receipts_inserts

# Save all INSERT statements to a text file
with open('insert_statements_bakery.sql', 'w') as f:
    for statement in all_inserts:
        f.write(statement + '\n')

print("INSERT statements have been generated and saved to 'insert_statements_bakery.sql'.")
