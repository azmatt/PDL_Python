import json
from pprint import pprint
from peopledatalabs import PDLPY

# Create a client, specifying your API key
client = PDLPY(
    api_key="###################"  # Replace with your actual API key
)

# Create an SQL query
telephone_number = '+15305551212'
SQL_QUERY = f"SELECT * FROM person WHERE (mobile_phone = '{telephone_number}')"

# Create a parameters JSON object
PARAMS = {
  'dataset': 'all',
  'sql': SQL_QUERY,
  'size': 10,
  'pretty': True
}

# Pass the parameters object to the Person Search API
response = client.person.search(**PARAMS).json()

# Check for successful response
if response["status"] == 200:
    data = response['data']
    print(f"Successfully grabbed {len(data)} records from PDL.")
    print(f"{response['total']} total PDL records exist matching this query.")

    # Pretty print each record
    for record in data:
        pprint(record)
else:
    print("NOTE. The carrier pigeons lost motivation in flight. See error and try again.")
    print("Error:", response)
