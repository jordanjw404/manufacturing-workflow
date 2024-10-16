import plotly.express as px
import pandas as pd

# Simulated Gantt chart data
df = pd.DataFrame([
    dict(Task="Cabinet 1", Start='2024-10-10', Finish='2024-10-11', Station="Sales"),
    dict(Task="Cabinet 1", Start='2024-10-11', Finish='2024-10-12', Station="Programming"),
    dict(Task="Cabinet 2", Start='2024-10-12', Finish='2024-10-13', Station="Sales"),
])

# Create the Gantt chart
fig = px.timeline(df, x_start="Start", x_end="Finish", y="Task", color="Station")
fig.update_layout(title='Production Timeline')
fig.show()
