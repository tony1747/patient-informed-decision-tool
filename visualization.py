import graphviz

def create_graph(df):
    g = graphviz.Digraph(engine='neato', filename="graph.gv", format="png")

    # Create a node for each day
    for i in range(df["days"].sum()):
        # Find the current strike and dose
        current_strike = df[df["days"].cumsum() > i]["strike"].iloc[0]
        current_dose = df[df["days"].cumsum() > i]["dose"].iloc[0]

        # Add the node to the graph
        g.node(
            str(i), 
            label=f"Day {i}\nStrike: {current_strike}\nDose: {current_dose}",
            pos=f"{i // 7},-{i % 7}!",
            fontsize ="8",
            shape="square",
            margin="0.01",
        )

        # Create edges between consecutive days
        if i > 0:
            g.edge(str(i - 1), str(i))

    return g