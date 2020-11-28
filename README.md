# BlockedIPsFinalProject

#### Richard Glennon and Shane Houghton

Program to visualize the attempts to enter the Moravian College Firewall from around the world.

## Required Libraries:

- Flask
- Redis
- IP2GeoTools
- Pytest
- Requests
- MatplotLib

## How to Use: 

1. In a terminal window, run `redis-server`
2. Run the `MockCollector.py` file
3. Run the `App.py` file
4. Run the `Client.py` file, a python window should open with a map plotting the attempts


## Testing:

To run the tests in the test file, a redis-server must be running in the background. Run with a pytest configuration
