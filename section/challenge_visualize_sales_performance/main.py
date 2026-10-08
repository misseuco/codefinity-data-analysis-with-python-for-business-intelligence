import matplotlib.pyplot as plt

def plot_sales_performance(summary_dict):
    products = list(summary_dict.keys())
    Revenue = list(summary_dict.values())
    plt.bar(products, Revenue)
    plt.title('Sales performance')
    plt.xlabel('products')
    plt.ylabel('Revenue')
    for k, v in enumerate(Revenue):
        plt.text(k,v+500, f"{v}", ha='center', fontweight = 'bold')

    plt.tight_layout()
    plt.show()

# Sample usage
summary_dict = {"Widget": 15000, "Gadget": 12000, "Doohickey": 9000}
plot_sales_performance(summary_dict)
