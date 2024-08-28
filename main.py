import plotly.graph_objects as go
import numpy as np


def plot_it(x, y, outfile: str):
    fig = go.Figure(go.Histogram2dContour(
        x=x,
        y=y
    ))

    fig.write_html(outfile, include_plotlyjs='cdn')


if __name__ == "__main__":
    np.random.seed(1)
    x = np.random.uniform(-1, 1, size=500)
    y = np.random.uniform(-1, 1, size=500)

    plot_it(x, y, "index.html")
