import marimo

__generated_with = "0.19.4"

app = marimo.App()


@app.cell
def _():
    # Core imports used across the notebook.
    import marimo as mo
    import numpy as np
    import plotly.graph_objects as go

    return go, mo, np


@app.cell
def _(mo):
    # UI controls for the plotting domain and grid resolution.
    x_range = mo.ui.slider(
        1,
        5,
        value=3,
        step=1,
        label="Coordinate range (absolute value)",
    )
    n_points = mo.ui.slider(
        20,
        200,
        value=120,
        step=10,
        label="Grid points per axis",
    )

    mo.vstack([x_range, n_points])
    return n_points, x_range


@app.cell
def _(np, n_points, x_range):
    # Build the grid and evaluate f(x1, x2) on it.
    x1 = np.linspace(-x_range.value, x_range.value, n_points.value)
    x2 = np.linspace(-x_range.value, x_range.value, n_points.value)
    X1, X2 = np.meshgrid(x1, x2)
    Z = X1**2 - X2**2
    return X1, X2, Z


@app.cell
def _(X1, X2, Z, go):
    # Render the 3D surface plot.
    fig = go.Figure(
        data=[
            go.Surface(
                x=X1,
                y=X2,
                z=Z,
                colorscale="Viridis",
                showscale=True,
            )
        ]
    )
    fig.update_layout(
        title="f(x1, x2) = x1^2 - x2^2",
        scene=dict(
            xaxis_title="x1",
            yaxis_title="x2",
            zaxis_title="f(x1, x2)",
        ),
        width=800,
        height=600,
        margin=dict(l=0, r=0, b=0, t=40),
    )
    fig


if __name__ == "__main__":
    app.run()
