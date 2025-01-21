
import plotly.graph_objects as go

countries = ['China', 'United States', 'India', 'Russia', 'Japan', 'Brazil', 'Canada', 'Korea, South', 'Germany', 'France',
             'Saudi Arabia', 'Indonesia', 'United Kingdom', 'Italy', 'Mexico', 'Iran', 'Turkey', 'Spain', 'Australia', 'Taiwan']
consumptions = [947.53, 455.13, 181.97, 110.20, 103.03, 68.15, 62.72, 60.07, 59.77, 51.29, 36.81, 35.08, 34.29, 36.39, 30.57,
                28.99, 28.65, 27.56, 27.51, 27.10]

fig = go.Figure(data=go.Bar(
    x=consumptions,
    y=countries,
    orientation='h',
    text=[f'{c:.2f} GW' for c in consumptions],
    textposition='auto',
))

fig.update_layout(
    title='Electricity Consumption by Country',
    xaxis=dict(title='Electricity Consumption (GW)'),
    yaxis=dict(title='Country'),
)

fig.show()
