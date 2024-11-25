import pandas as pd
from repositories.airport_repository import AirportRepository

# Mock data for testing
mock_data = pd.DataFrame({
    "id": [1, 2, 3],
    "name": ["Airport A", "Airport B", "Airport C"],
    "city": ["City A", "City B", "City C"],
    "country": ["Country A", "Country B", "Country C"],
    "IATA": ["AAA", "BBB", "CCC"],
    "ICAO": ["AAAA", "BBBB", "CCCC"],
    "latitude": [45.0, 46.0, 47.0],
    "longitude": [12.0, 13.0, 14.0],
    "altitude": [1000, 2000, 3000],
    "timezone": [1, 2, 3],
    "DST": ["E", "E", "E"],
    "tz": ["UTC+1", "UTC+2", "UTC+3"],
    "type": ["large_airport", "medium_airport", "small_airport"],
    "source": ["Our Source", "Our Source", "Our Source"]
})

# Initialize the repository
repo = AirportRepository()

# Insert data into the database
repo.insert_airports(mock_data)
print("Inserted mock data into the database.")

# Retrieve data from the database
retrieved_data = repo.get_airports()
print("Retrieved data:")
print(retrieved_data)
