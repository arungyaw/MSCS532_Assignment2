import pandas as pd
import matplotlib.pyplot as plt

# Read the results file
data = pd.read_csv("results.csv")

# Create a new column to make the x-axis easier to read
data["Test Case"] = data["Dataset"] + " - " + data["Size"].astype(str)

# Plot execution time for each algorithm
plt.figure(figsize=(12, 6))

for algorithm in data["Algorithm"].unique():
    subset = data[data["Algorithm"] == algorithm]
    plt.plot(
        subset["Test Case"],
        subset["Execution Time (seconds)"],
        marker = "o",
        label=algorithm
    )

plt.xlabel("Dataset Type and Input Size")
plt.ylabel("Execution Time (seconds)")
plt.title("Execution Time Comparison: Merge Sort Vs Quick Sort")
plt.xticks(rotation=45, ha="right")
plt.legend()
plt.tight_layout()

# Save the graph as an image
plt.savefig("execution_time_graph.png")

# Show the graph
plt.show()
    