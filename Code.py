import csv
import sys
import os
import statsmodels.api as sm
import plotly.graph_objects as go

def option(choice):
    file_dict = {
        1: "big_data_canada.csv",
        2: "dl_canada.csv",
        3: "ml_canada.csv",
        4: "py_canada.csv",
        5: "sql_canada.csv"
    }
    if choice in file_dict:
        return file_dict[choice]
    elif choice == 6:
        print("Thanks for using")
        sys.exit()
    else:
        print("Invalid Choice! Try Again.")
        return None

def convert(file_path):
    csv_data = []
    try:
        with open(file_path, 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if len(row) != 2:
                    print(f"Invalid data format in file {file_path}")
                    return None
                try:
                    for row in csv_reader:
                        # Append each row to the 2D list
                        csv_data.append(row)
                except ValueError:
                    print(f"Invalid data types in file {file_path}")
                    return None
    except FileNotFoundError:
        print(f"File {file_path} not found")
        return None
    return csv_data

def trend(tech_data):
    if not tech_data:
        print("No valid data to plot.")
        return
    
    years, adoption_rates = zip(*tech_data)
    
    # Plotting with Plotly
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=years, y=adoption_rates, mode='lines+markers', name='Adoption Rate'))

    fig.update_layout(
        title='Tech Adoption Trends',
        xaxis_title='Year',
        yaxis_title='Adoption Rate (%)',
        template='plotly_white'
    )
    
    fig.show()

def forecast(tech_data):
    if not tech_data:
        print("No valid data for forecasting.")
        return
    
    years, adoption_rates = zip(*tech_data)
    adoption_rates = list(adoption_rates)
    
    try:
        # Fit the time series model 
        model = sm.tsa.ARIMA(adoption_rates, order=(1, 1, 1))
        fit = model.fit()
        # Forecast the next 5 years
        forecast_steps = 5
        forecast = fit.forecast(steps=forecast_steps)
        
        forecast_years = [years[-1] + i for i in range(1, forecast_steps + 1)]
        forecast_rates = forecast[0]
        
        return forecast_years, forecast_rates
    except:
        pass
def main():
    while True:
        print("CHOOSE THE TECHNOLOGY:\n1. Big Data\n2. Deep Learning\n3. Machine Learning\n4. Python\n5. SQL\n6. Quit\n")
        try:
            choice = int(input("Enter: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        file_path = option(choice)
        if file_path:
            tech_data = convert(file_path)
            trend(tech_data)
            try:
                forecast_years, forecast_rates = forecast(tech_data)
                if forecast_years and forecast_rates:
                    # Plotting the forecast
                    fig = go.Figure()
                    fig.add_trace(go.Scatter(x=[year for year, _ in tech_data], y=[rate for _, rate in tech_data], mode='lines+markers', name='Actual'))
                    fig.add_trace(go.Scatter(x=forecast_years, y=forecast_rates, mode='lines+markers', name='Forecast'))

                    fig.update_layout(
                        title='Tech Adoption Trends with Forecast',
                        xaxis_title='Year',
                        yaxis_title='Adoption Rate (%)',
                        template='plotly_white'
                    )
                    
                    fig.show()
            except:
                pass

if __name__ == "__main__":
    main()