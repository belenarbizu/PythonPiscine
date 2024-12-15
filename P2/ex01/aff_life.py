from load_csv import load
import matplotlib.pyplot as plt

def country_info(path: str) -> None:
    dataset = load(path)
    
    df_spain = dataset[dataset["country"] == "Spain"].iloc[0] #filter spain row

    years = df_spain.index[1:] #all index values except country
    values = df_spain.values[1:] #all values except spain

    plt.plot(years, values)
    plt.xticks(years[::40]) #x values slicing in step of 50
    plt.xlabel("Year")
    plt.ylabel("life expectancy")
    plt.title("Spain Life expectancy Projections")

    plt.show()