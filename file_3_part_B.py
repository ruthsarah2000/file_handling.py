'''
Compile and analyze historical weather data from multiple files (weather_2020.txt, weather_2021.txt, etc.). Each file contains daily 
temperature data. Calculate the average temperature for each year and identify the year with the highest average.
'''
def compile_weather_data(file_list):
    
    yearly_temperatures = {}

   
    for file_name in file_list:
        
        year = file_name.split("_")[1].split(".")[0]

       
        total_temperature = 0
        day_count = 0

       
        with open(file_name, 'r') as file:
            for line in file:
               
                date, temp_str = line.strip().split(',')
                temperature = int(temp_str[:-2])  # Extract the temperature value
                total_temperature += temperature
                day_count += 1

       
        average_temperature = total_temperature / day_count

        
        yearly_temperatures[year] = average_temperature

   
    highest_avg_year = max(yearly_temperatures, key=yearly_temperatures.get)

    return yearly_temperatures, highest_avg_year


file_list = ["weather_2020.txt", "weather_2021.txt"]


yearly_temperatures, highest_avg_year = compile_weather_data(file_list)


print("Yearly Average Temperatures:")
for year, avg_temp in yearly_temperatures.items():
    print(f"{year}: {avg_temp:.2f}°C")
print(f"The year with the highest average temperature is {highest_avg_year} with an average of {yearly_temperatures[highest_avg_year]:.2f}°C.")
