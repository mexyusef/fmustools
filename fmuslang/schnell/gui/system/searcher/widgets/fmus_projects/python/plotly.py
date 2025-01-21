import plotly.graph_objects as go
import humanize


def plot_gdp(starting_year = 2021, starting_gdp = 1.186 * 10**12, starting_pop = 273.8 * 10**6):
    # Define the variables
    # starting_gdp_per_capita = 4333
    starting_gdp_per_capita = starting_gdp/starting_pop
    ending_year = 2045
    population_growth_rate = 0.007  # 0.7% expressed as a decimal
    gdp_growth_rates = [0.03, 0.04, 0.05, 0.055, 0.06, 0.065, 0.07]  # List of different GDP growth rates
    

    # Create empty lists to store the data points
    years = []
    gdp_per_capita = []
    gdp_total = []
    pop_total = []

    # Calculate GDP per capita and total GDP for each year with different growth rates
    for year in range(starting_year, ending_year + 1):
        years.append(year)
        population_growth = (1 + population_growth_rate) ** (year - starting_year)
        gdp_per_capita.append(starting_gdp_per_capita * population_growth)
        gdp_total.append(starting_gdp * population_growth)

    # Create the plotly figure
    fig = go.Figure()

    # Add lines for each GDP growth rate
    for growth_rate in gdp_growth_rates:
        gdp_per_capita_growth = [starting_gdp_per_capita]
        gdp_total_growth = [starting_gdp]
        pop_total = [starting_pop]

        for year in range(starting_year + 1, ending_year + 1):
            # ini masih salah rumusnya
            # harusnya: (gdp now - gdp prev)/gdp prev
            GDP = int(gdp_total_growth[-1] * (1 + growth_rate))
            gdp_total_growth.append(GDP)
            POP = pop_total[-1] * (1 + population_growth_rate)
            pop_total.append(POP)
            # gdp_per_capita_growth.append(gdp_per_capita_growth[-1] * (1 + growth_rate))
            gdp_per_capita_growth.append(GDP/POP)

            if year % 10 == 0:  # Add label at every 5-year interval
                if year>2035:
                    fig.add_annotation(x=year, y=gdp_per_capita_growth[-1], text=f'GDP: {humanize.intword(gdp_total_growth[-1])}<br>per Capita: {humanize.intword(gdp_per_capita_growth[-1])}<br>Pop: {humanize.intword(pop_total[-1])}', showarrow=False, font=dict(size=10))
                else:
                    fig.add_annotation(x=year, y=gdp_per_capita_growth[-1], text=f'{humanize.intword(gdp_total_growth[-1])}/{humanize.intword(gdp_per_capita_growth[-1])}/{humanize.intword(pop_total[-1])}', showarrow=False, font=dict(size=10))
                #fig.add_annotation(x=year, y=gdp_per_capita_growth[-1], text=f'GDP per Capita: <br>{humanize.intcomma(gdp_per_capita_growth[-1])}', showarrow=False, font=dict(size=10))
                #fig.add_annotation(x=year, y=gdp_total_growth[-1], text=f'Total GDP: <br>{humanize.intword(gdp_total_growth[-1])}', showarrow=False, font=dict(size=10))


        # ini utk hover
        fig.add_trace(go.Scatter(x=years, y=gdp_per_capita_growth, mode='lines+markers', name=f'{growth_rate*100:.1f}%'))
        #fig.add_trace(go.Scatter(x=years, y=gdp_total_growth, mode='lines+markers', name=f'Total GDP Growth Rate: {growth_rate*100:.1f}%'))

        # Add labels at the end of each line
        fig.add_annotation(x=ending_year, y=gdp_per_capita_growth[-1], text=f'GDP: {humanize.intword(gdp_total_growth[-1])}<br>per Capita: {humanize.intword(gdp_per_capita_growth[-1])}<br>Pop: {humanize.intword(pop_total[-1])}', showarrow=False, font=dict(size=10))
        #fig.add_annotation(x=ending_year, y=gdp_total_growth[-1], text=f'Total GDP: <br>{gdp_total_growth[-1]:,.2f}', showarrow=False, font=dict(size=10))

    # Set plot and axis titles
    fig.update_layout(title='Indonesia GDP (2021-2045)',
                    xaxis_title='Year',
                    yaxis_title='GDP',
                    xaxis=dict(dtick=1),
                    legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01))  # Adjust legend position and format

    # Show the plot
    fig.show()

plot_gdp(2023,starting_gdp=1.39*(10**12),starting_pop=282_093_113)
