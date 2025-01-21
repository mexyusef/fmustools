import plotly.graph_objects as go
import humanize


background_image = 'https://rajaampat.direktoripariwisata.id/wp-content/uploads/2020/10/MER.Tobias.Zimmer.Shark_.Lagoon.jpg'


def angka_singkat(nilai):
	return nilai.replace(' trillion','T').replace(' billion','B').replace(' million', 'M').replace(' thousand', 'K')

def plot_gdp(starting_year = 2021, starting_gdp = 1.186 * 10**12, starting_pop = 273.8 * 10**6, population_growth_rate = 0.007, ending_year = 2045, gdp_growth_rates = [0.03, 0.04, 0.05, 0.055, 0.06, 0.065, 0.07], country='Indonesia'):
	# Define the variables
	# starting_gdp_per_capita = 4333
	starting_gdp_per_capita = starting_gdp/starting_pop

	# Create empty lists to store the data points
	years = []
	gdp_per_capita = []
	gdp_total = []
	pop_total = []

	# Calculate GDP per capita and total GDP for each year with different growth rates
	#for year in range(starting_year, ending_year + 1):
	for counter, year in enumerate(range(starting_year, ending_year + 1)):
		years.append(year)
		if isinstance(population_growth_rate, list):
			population_growth = (1 + population_growth_rate[counter]) ** (year - starting_year)
		else:
			population_growth = (1 + population_growth_rate) ** (year - starting_year)
		# population_growth = (1 + population_growth_rate) ** (year - starting_year)
		gdp_per_capita.append(starting_gdp_per_capita * population_growth)
		gdp_total.append(starting_gdp * population_growth)

	# Create the plotly figure
	fig = go.Figure()

	# Add lines for each GDP growth rate
	for growth_rate in gdp_growth_rates:
		gdp_per_capita_growth = [starting_gdp_per_capita]
		gdp_total_growth = [starting_gdp]
		pop_total = [starting_pop]

		# for year in range(starting_year + 1, ending_year + 1):
		for counter,year in enumerate(range(starting_year + 1, ending_year + 1)):
			# ini masih salah rumusnya
			# harusnya: (gdp now - gdp prev)/gdp prev
			GDP = int(gdp_total_growth[-1] * (1 + growth_rate))
			gdp_total_growth.append(GDP)
			if isinstance(population_growth_rate, list):
				POP = pop_total[-1] * (1 + population_growth_rate[counter])
			else:
				POP = pop_total[-1] * (1 + population_growth_rate)
			# POP = pop_total[-1] * (1 + population_growth_rate)
			pop_total.append(POP)
			# gdp_per_capita_growth.append(gdp_per_capita_growth[-1] * (1 + growth_rate))
			gdp_per_capita_growth.append(GDP/POP)

			current_gdp = angka_singkat(humanize.intword(gdp_total_growth[-1]))
			current_gdp_capita = angka_singkat(humanize.intword(gdp_per_capita_growth[-1]))
			current_pop = angka_singkat(humanize.intword(pop_total[-1]))
				
			if year % 10 == 0:  # Add label at every 5-year interval
				if year>2035:
					fig.add_annotation(x=year, y=gdp_per_capita_growth[-1], text=f'GDP: {current_gdp}<br>per capita: {current_gdp_capita}<br>Pop: {current_pop}', showarrow=False, font=dict(size=10))
				else:
					fig.add_annotation(x=year, y=gdp_per_capita_growth[-1], text=f'{current_gdp}/{current_gdp_capita}/{current_pop}', showarrow=False, font=dict(size=10))
				#fig.add_annotation(x=year, y=gdp_per_capita_growth[-1], text=f'GDP per Capita: <br>{humanize.intcomma(gdp_per_capita_growth[-1])}', showarrow=False, font=dict(size=10))
				#fig.add_annotation(x=year, y=gdp_total_growth[-1], text=f'Total GDP: <br>{humanize.intword(gdp_total_growth[-1])}', showarrow=False, font=dict(size=10))


		# ini utk hover
		# fig.add_trace(go.Scatter(x=years, y=gdp_per_capita_growth, mode='lines+markers', name=f'{growth_rate*100:.1f}%,{pop_total[-1]}'))
		fig.add_trace(go.Scatter(x=years, y=gdp_per_capita_growth, mode='lines+markers', name=f'{growth_rate*100:.1f}%'))
		#fig.add_trace(go.Scatter(x=years, y=gdp_total_growth, mode='lines+markers', name=f'Total GDP Growth Rate: {growth_rate*100:.1f}%'))


		last_gdp = angka_singkat(humanize.intword(gdp_total_growth[-1]))
		last_gdp_capita = angka_singkat(humanize.intword(gdp_per_capita_growth[-1]))
		last_pop = angka_singkat(humanize.intword(pop_total[-1]))

		# Add labels at the end of each line
		fig.add_annotation(x=ending_year, y=gdp_per_capita_growth[-1], text=f'GDP: {last_gdp}<br>per capita: {last_gdp_capita}<br>Pop: {last_pop}', showarrow=False, font=dict(size=10))
		#fig.add_annotation(x=ending_year, y=gdp_total_growth[-1], text=f'Total GDP: <br>{gdp_total_growth[-1]:,.2f}', showarrow=False, font=dict(size=10))

	# Set plot and axis titles
	fig.update_layout(title=f'{country} GDP/capita projection ({starting_year}-{ending_year})',
		xaxis_title='Year',
		yaxis_title='GDP/capita',
		xaxis=dict(dtick=1),
		# ["plotly", "plotly_white", "plotly_dark", "ggplot2", "seaborn", "simple_white", "none"]:
		# template='plotly_dark', # https://plotly.com/python/templates/
		# template='seaborn',
		template='plotly_white',
		legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01),
		# images=[dict(
		#     source=background_image,
		#     xref="paper", yref="paper",
		#     x=0, y=0,
		#     sizex=1, sizey=1,
		#     opacity=0.5,
		#     layer="below"
		# )],
	)
	# Adjust legend position and format

	# Show the plot
	fig.show()


# plot_gdp(
	# starting_year = 2021, 
	# starting_gdp = 1.186 * 10**12, 
	# starting_pop = 273.8 * 10**6, 
	# population_growth_rate = 0.007, 
	# ending_year = 2045, 
	# gdp_growth_rates = [0.03, 0.04, 0.05, 0.055, 0.06, 0.065, 0.07])

# data from 2021
# plot_gdp()

# data from 2023
# plot_gdp(2023,starting_gdp=1.39*(10**12),starting_pop=282_093_113, gdp_growth_rates = [0.05, 0.055, 0.056, 0.057, 0.058, 0.059, 0.06])

# ini asumsikan pop growth 0.1% sampai 2045
# china, 2021
# plot_gdp(2021,starting_gdp=17.73*(10**12),starting_pop=1_412_000_000, population_growth_rate=0.1/100, gdp_growth_rates = [0.04, 0.05, 0.055], country='China')


# plot_gdp(2021,starting_gdp=3.176*(10**12),starting_pop=1_408_000_000, population_growth_rate=0.8/100, gdp_growth_rates = [0.04, 0.05, 0.06, 0.07], country='India')
# https://www.statista.com/statistics/271308/population-growth-in-india/
# Year	Population Growth Rate (%)
# 2011	1.36
# 2012	1.33
# 2013	1.3
# 2014	1.24
# 2015	1.19
# 2016	1.19
# 2017	1.16
# 2018	1.09
# 2019	1.03
# 2020	0.96
# 2021	0.8
predicted_growth_rates = [
	0.8, # 2021
    0.74, 0.67, 0.61, 0.55, 0.50, 0.46, 0.42, 0.39, 0.36, 0.34, 0.32, 0.30,
    0.28, 0.26, 0.24, 0.23, 0.21, 0.20, 0.19, 0.18, 0.17, 0.16, 0.15, 0.14,
    0.14, 0.13, 0.12, 0.12, 0.11
]
plot_gdp(2021,starting_gdp=3.176*(10**12),starting_pop=1_408_000_000, population_growth_rate=[i/100 for i in predicted_growth_rates], gdp_growth_rates = [0.04, 0.05, 0.06, 0.07, 0.08], country='India')
# plot_gdp(2021,starting_gdp=3.176*(10**12),starting_pop=1_408_000_000, population_growth_rate=0.8/100, gdp_growth_rates = [0.04, 0.05, 0.06, 0.07], country='India')
