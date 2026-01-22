import marimo

__generated_with = "0.19.4"

app = marimo.App()


@app.cell
def _():
    import marimo as mo
    import numpy as np
    import plotly.graph_objects as go

    return go, mo, np


@app.cell
def _(mo):
    x_min = mo.ui.slider(
        -5.0,
        5.0,
        value=-2.0,
        step=0.5,
        label="x min",
    )
    x_max = mo.ui.slider(
        -5.0,
        5.0,
        value=2.0,
        step=0.5,
        label="x max",
    )
    n_points = mo.ui.slider(
        100,
        800,
        value=400,
        step=50,
        label="points",
    )

    mo.vstack([x_min, x_max, n_points])
    return n_points, x_max, x_min


@app.cell
def _(np, n_points, x_max, x_min):
    xmin = float(x_min.value)
    xmax = float(x_max.value)
    if xmin > xmax:
        xmin, xmax = xmax, xmin
    x = np.linspace(xmin, xmax, n_points.value)
    h = np.exp(x)
    g = np.where(x >= 0, -np.sqrt(x), np.nan)
    f = -np.sqrt(h)
    return f, g, h, x


@app.cell
def _(f, g, go, h, x):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=h, mode="lines", name="h(x)=e^x"))
    fig.add_trace(go.Scatter(x=x, y=g, mode="lines", name="g(x)=-sqrt(x)"))
    fig.add_trace(go.Scatter(x=x, y=f, mode="lines", name="f(x)=g(h(x))"))
    fig.update_layout(
        title="Functions h(x), g(x), and f(x)=g(h(x))",
        xaxis_title="x",
        yaxis_title="value",
        width=800,
        height=500,
        margin=dict(l=40, r=20, b=40, t=50),
    )
    fig


if __name__ == "__main__":
    app.run()
