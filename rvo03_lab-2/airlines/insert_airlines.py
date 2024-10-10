import pandas as pd

# Load the CSV files
AIRLINES_PATH = 'rvo03_lab-2/airlines/airlines.csv'
AIRPORTS_PATH = 'rvo03_lab-2/airlines/airports.csv'
FLIGHTS_PATH = 'rvo03_lab-2/airlines/flights.csv'

# Read the CSV files into DataFrames
airlines_df = pd.read_csv(AIRLINES_PATH)
airports_df = pd.read_csv(AIRPORTS_PATH)
flights_df = pd.read_csv(FLIGHTS_PATH)


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
airlines_inserts = generate_insert_statements(airlines_df, 'airlines')
airports_inserts = generate_insert_statements(airports_df, 'airports')
flights_inserts = generate_insert_statements(flights_df, 'flights')

# Combine all insert statements
all_inserts = airlines_inserts + airports_inserts + flights_inserts

# Save all INSERT statements to a text file
with open('insert_statements_airlines.sql', 'w') as f:
    for statement in all_inserts:
        f.write(statement + '\n')

print("INSERT statements have been generated and saved to 'insert_statements_airlines.sql'.")
