import matplotlib.pyplot as plt

def plot_monthly_sales(sales_list):
    import calendar
    lenght_months = len(sales_list)
    months_list = list(calendar.month_abbr[1:lenght_months+1])
    plt.plot(months_list, sales_list, marker='o')
    plt.xlabel('Month')
    plt.ylabel('Sales')
    plt.title('Plot Monthly Sales Trend')
    plt.xticks(rotation=90)
    plt.show()

sample_sales = [1200, 1500, 1700, 1600, 1800, 2000, 2200, 2100, 2300, 2500, 2400, 2600]
plot_monthly_sales(sample_sales)