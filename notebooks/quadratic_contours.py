"""title: Quadratic Contours
description: Contour plot of f(x1, x2)=1/2 (x1^2 + gamma x2^2) with adjustable gamma.
"""

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
    # UI controls for the quadratic parameters and plotting grid.
    gamma = mo.ui.slider(
        0.1,
        10.0,
        value=1.0,
        step=0.1,
        label="gamma",
    )
    x_range = mo.ui.slider(
        1.0,
        6.0,
        value=3.0,
        step=0.5,
        label="coordinate range (absolute value)",
    )
    n_points = mo.ui.slider(
        50,
        300,
        value=160,
        step=10,
        label="grid points per axis",
    )

    mo.vstack([gamma, x_range, n_points])
    return gamma, n_points, x_range


@app.cell
def _(gamma, np, n_points, x_range):
    # Build the grid and evaluate the quadratic form.
    x1 = np.linspace(-x_range.value, x_range.value, n_points.value)
    x2 = np.linspace(-x_range.value, x_range.value, n_points.value)
    X1, X2 = np.meshgrid(x1, x2)
    Z = 0.5 * (X1**2 + float(gamma.value) * X2**2)
    return X1, X2, Z


@app.cell
def _(X1, X2, Z, gamma, go):
    # Render the contour plot.
    fig = go.Figure(
        data=[
            go.Contour(
                x=X1[0],
                y=X2[:, 0],
                z=Z,
                contours=dict(showlabels=True, labelfont=dict(size=10, color="white")),
                colorscale="Viridis",
            )
        ]
    )
    fig.update_layout(
        title=f"Contour of f(x1, x2)=0.5 (x1^2 + {gamma.value:.2f} x2^2)",
        xaxis_title="x1",
        yaxis_title="x2",
        width=800,
        height=600,
        margin=dict(l=50, r=20, b=50, t=60),
    )
    fig.update_yaxes(scaleanchor="x", scaleratio=1)
    fig


if __name__ == "__main__":
    app.run()
