import seaborn as sns
import matplotlib.pyplot as plt

# Define the data
# countries = ['Malaysia (35)', 'Viet Nam (43)', 'Thailand (54)', 'Indonesia (55)', 'Singapore (70)', 'Lao PDR (83)', 'Cambodia (84)', 'Philippines (94)', 'Brunei Darussalam (105)']
countries = ['Sweden (1)','France (7)','Germany (11)','US (12)','UK (13)','Brazil (14)','China (17)','New Zealand (22)','Australia (24)','Japan (27)','South Korea (31)','Saudi Arabia (57)','ASEAN', 'India (67)','South Africa (82)'] # + countries
# eti_scores = [61.7, 58.9, 55.9, 55.8, 53.7, 52.1, 52.1, 50.2, 47.3]
eti_scores = [78.5,70.6,67.5,66.3,66.2,65.9,64.9,63.7,63.6,63.3,62.3,55.3,54.6,54.3,52.2] # + eti_scores

theme = [
"viridis",
"magma",
"plasma",
"inferno",
"cividis",
"coolwarm",
"twilight",
"BuGn",
"BuPu",
"RdPu",
"PuBuGn",
]

# Create a bar plot
sns.set(style="whitegrid")
plt.figure(figsize=(10, 8))
ax = sns.barplot(x=countries, y=eti_scores, palette=theme[5])

# Add labels and title
plt.xlabel('Countries (Rank)')
plt.ylabel('ETI Scores')
#plt.title('ASEAN Energy Transition Index (ETI) 2023')
plt.title('Energy Transition Index (ETI) 2023')

# Rotate x-axis labels if needed
plt.xticks(rotation=45)

# Add values on top of each bar
for i, score in enumerate(eti_scores):
    ax.text(i, score + 0.5, str(score), ha='center', va='bottom')

# Set y-axis limits
# plt.ylim(30, max(eti_scores) + 5)  # Set the lower limit to 30
# Set y-axis limits
plt.ylim(30, 80)  # Set the lower limit to 30 and upper limit to 80

# Adjust the margins
plt.subplots_adjust(bottom=0.5)  # Increase the bottom margin

# Show the plot
plt.show()

