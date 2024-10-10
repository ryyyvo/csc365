import pandas as pd

# Load the CSV files
ALBUMS_PATH = 'rvo03_lab-2/katzenjammer/Albums.csv'
BAND_PATH = 'rvo03_lab-2/katzenjammer/Band.csv'
INSTRUMENTS_PATH = 'rvo03_lab-2/katzenjammer/Instruments.csv'
PERFORMANCE_PATH = 'rvo03_lab-2/katzenjammer/Performance.csv'
SONGS_PATH = 'rvo03_lab-2/katzenjammer/Songs.csv'
TRACKLISTS_PATH = 'rvo03_lab-2/katzenjammer/Tracklists.csv'
VOCALS_PATH = 'rvo03_lab-2/katzenjammer/Vocals.csv'

# Read the CSV files into DataFrames
band_df = pd.read_csv(BAND_PATH)
vocals_df = pd.read_csv(VOCALS_PATH)
instruments_df = pd.read_csv(INSTRUMENTS_PATH)
songs_df = pd.read_csv(SONGS_PATH)
performance_df = pd.read_csv(PERFORMANCE_PATH)
albums_df = pd.read_csv(ALBUMS_PATH)
tracklists_df = pd.read_csv(TRACKLISTS_PATH)


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


# Generate insert statements for each table
albums_inserts = generate_insert_statements(albums_df, 'Albums')
songs_inserts = generate_insert_statements(songs_df, 'Songs')
band_inserts = generate_insert_statements(band_df, 'Band')
instruments_inserts = generate_insert_statements(instruments_df, 'Instruments')
performance_inserts = generate_insert_statements(performance_df, 'Performance')
tracklists_inserts = generate_insert_statements(tracklists_df, 'Tracklists')
vocals_inserts = generate_insert_statements(vocals_df, 'Vocals')

# Combine all insert statements
all_inserts = (
    albums_inserts + songs_inserts + band_inserts +
    instruments_inserts + performance_inserts +
    tracklists_inserts + vocals_inserts
)

# Save all INSERT statements to a text file
with open('insert_statements_katzenjammer.sql', 'w') as f:
    for statement in all_inserts:
        f.write(statement + '\n')

print("INSERT statements have been generated and saved to 'insert_statements_katzenjammer.sql'.")
