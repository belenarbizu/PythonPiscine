from load_csv import load
import matplotlib.pyplot as plt

def population_info(path: str) -> None:
    dataset = load(path)

    df_spain = dataset[dataset["country"] == "Spain"].iloc[0] #filter spain row
    df_germany = dataset[dataset["country"] == "Germany"].iloc[0] #filter germany row

    years = df_spain.index[1:252] #all index values except country

    values_spain = df_spain.values[1:252] #all values except spain
    values_germany = df_germany.values[1:252] #all values except germany
    print(values_germany)

    plt.plot(years, values_spain, label = "Spain")
    plt.plot(years, values_germany, label = "Germany")
    plt.yticks(["20M", "40M", "60M"]) #y values slicing in step of 20M
    plt.xticks(years[::40]) #x values slicing in step of 50
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.title("Population Projections")
    plt.legend()

    plt.show()

def main():
    population_info("population_total.csv")


if __name__ == "__main__":
    main()