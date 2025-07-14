def calculate_perimeter(corners):
    edges = set()  # Track unique edges
    for x, y in corners:
        # Each square contributes these four edges
        square_edges = {
            ((x, y), (x + 1, y)),  # Left edge
            ((x + 1, y), (x + 1, y + 1)),  # Bottom edge
            ((x + 1, y + 1), (x, y + 1)),  # Right edge
            ((x, y + 1), (x, y)),  # Top edge
        }
        # Add edges, removing if they already exist
        for edge in square_edges:
            if edge in edges:
                edges.remove(edge)
            else:
                edges.add(edge)
    # The remaining edges form the perimeter
    return len(edges)

# Example usage
corners = [(0, 0), (0, 3)]
print(calculate_perimeter(corners))  # Output: 10
