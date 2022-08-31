# Python3 implementation to build a
# graph using Dictionaries

from collections import defaultdict

# Function to build the graph
def build_graph():
	edges = [
		["A", "B"], ["A", "E"],
		["A", "C"], ["B", "D"],
		["B", "E"], ["C", "F"],
		["C", "G"], ["D", "E"]
	]
	graph = defaultdict(list)
	
	# Loop to iterate over every
	# edge of the graph
if __name__ == "__main__":
	graph = build_graph()
	print(graph)

print('Tuan')
