import matplotlib.pyplot as plt
from production_data import get_station_data

stations, units = get_station_data()

# Function to create a bar chart
def visualize_production():
    plt.bar(stations, units, color='skyblue')
    plt.xlabel('Production Station')
    plt.ylabel('Number of Units')
    plt.title('Units at Each Production Station')
    plt.show()

# Run the visualization
visualize_production()
