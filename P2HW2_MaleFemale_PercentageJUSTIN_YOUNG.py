# CHAP 2 HW 2
# 09 OCT 18
# CTI-110 P2HW2 - Male Female Percentage 
# YOUNG, JUSTIN

# Get the total of males
males = float(input('How many males are in the class? : '))

# Get the total of females
females = float(input('How many females are in the class? : '))

# Total in class males+females 
total = males + females

# Display percentage of males
pmales = males / total
# Display percentage of females
pfemales = females / total
print('The percentage of males in the class is', (format(pmales, '.0%')))
print('The percentage of females in the class is', (format(pfemales, '.0%')))
