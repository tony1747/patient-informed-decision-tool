import graphviz

def create_graph(df):
    g = graphviz.Digraph(engine='neato', filename="graph.gv", format="png")
    # rgb values for each strike, in the range from blue to red
    colors = ['#FF6EC7', '#FFB4BF', '#FFD9BB', '#FFF3B7', '#FFF8D2']  



    # Create a node for each day
    for i in range(0, df["days"].sum() // 7):
        # Find the current strike and dose
        current_strike = df[df["days"].cumsum() // 7 > i]["strike"].iloc[0]
        current_dose = df[df["days"].cumsum() // 7 > i]["dose"].iloc[0]

        # Add the node to the graph
        g.node(
            str(i), 
            label=f"Week {i}\nStrike: {current_strike}\nDose: {current_dose}",
            pos=f"{i % 4},-{i // 4}!",
            fontsize ="10",
            shape="square",
            margin="0.05",
            style="filled",
            fillcolor=colors[current_strike - 1] 
        )

        # Create edges between consecutive days
        if i > 0:
            g.edge(str(i - 1), str(i))

    return g