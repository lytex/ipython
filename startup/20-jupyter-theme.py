import os

from jupyterthemes import jtplot
jtplot.style(theme='monokai', context='notebook', ticks=True, grid=False)

try:
    import plotly.io as pio
    import plotly.express as px

    pio.templates.default = "plotly_dark"
except ImportError:
    pass
