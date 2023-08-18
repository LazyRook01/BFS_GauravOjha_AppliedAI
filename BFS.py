import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import json
import time

# Streamlit app title
st.title("BFS Visualization on an Undirected Graph")

# Define the visualize_graph function
def visualize_graph(graph, pos, visited, current_node=None, parent=None, highlight_node=None, queue=None):
    plt.figure(figsize=(10, 6))
    node_colors = ["green" if node == current_node else "blue" if node in visited else "gray" for node in graph.nodes]
    edge_colors = ["blue" if (node, neighbor) == (parent, current_node) else "gray" for node, neighbor in graph.edges]
    
    nx.draw(
        graph,
        pos,
        with_labels=True,
        node_color=node_colors,
        edge_color=edge_colors,
        font_color='black',
        font_weight='bold',
        node_size=1000,
    )

    if queue:
        queue_text = "\n".join(str(node) for node in queue)
        plt.text(1.1, 0.5, f"Queue:\n{queue_text}", fontsize=10, ha="left", va="center")

    plt.title("BFS Visualization")
    st.pyplot(plt)
    plt.close()

# Rest of your Streamlit app code
st.write("Upload a text file that contains JSON-like adjacency list format.")
uploaded_file = st.file_uploader("Upload a text file", type=["txt"])

def bfs_queue(graph, start_node):
    queue = [start_node]
    visited = set()
    traversal_order = []

    while queue:
        current_node = queue.pop(0)

        if current_node not in visited:
            visited.add(current_node)
            traversal_order.append(current_node)
            neighbors = graph[current_node]
            visualize_graph(graph, pos, visited, current_node, None, current_node, queue)
            time.sleep(1)

            for neighbor in neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)
        else:
            visualize_graph(graph, pos, visited, current_node, None, current_node, queue)
            time.sleep(1)

    return traversal_order

if uploaded_file is not None:
    file_contents = uploaded_file.read().decode("utf-8")
    adjacency_list = json.loads(file_contents)
    G = nx.Graph()

    # Process the adjacency list and add nodes and edges to the graph
    for node, neighbors in adjacency_list.items():
        G.add_node(node)
        for neighbor in neighbors:
            G.add_edge(node, neighbor)
        
    # Draw the initial graph
    pos = nx.spring_layout(G)
    visualize_graph(G, pos, set())

    start_node = st.selectbox("Enter the starting node for BFS:", list(G.nodes) if G.nodes else "")

    if st.button("Start BFS"):
        traversal_order = bfs_queue(G, start_node)
        st.write("BFS traversal completed.")
        
        st.subheader("Visited Order")
        for node in traversal_order:
            st.write(f"Node: {node}")
