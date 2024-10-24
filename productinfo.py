from build_graph import build_graph

edges = [
    ("Electronics", "Computers"),
    ("Electronics", "TVs"),
    ("Computers", "Laptops"),
    ("Computers", "Desktops"),
    ("TVs", "Smart TVs"),
    ("TVs", "LED TVs")
]

weights = {
    "Electronics": 10,
    "Computers": 15,
    "TVs": 8,
    "Laptops": 7,
    "Desktops": 5,
    "Smart TVs": 12,
    "LED TVs": 6
}

budget = 30

input = build_graph(edges)

