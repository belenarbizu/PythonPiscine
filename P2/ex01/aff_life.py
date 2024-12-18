from load_csv import load
import matplotlib.pyplot as plt


def country_info(path: str) -> None:
    """
    Shows the graphic of Spain life expectancy years
    """
    dataset = load(path)

    # filter spain row
    df_spain = dataset[dataset["country"] == "Spain"].iloc[0]

    # all index values except country
    years = df_spain.index[1:].to_numpy(dtype=int)
    # all values except spain
    values = df_spain.values[1:]

    plt.plot(years, values)

    # x values slicing in step of 50
    plt.xticks(years[::40])
    plt.xlabel("Year")
    plt.ylabel("life expectancy")
    plt.title("Spain Life expectancy Projections")

    plt.show()


def main():
    country_info("life_expectancy_years.csv")


if __name__ == "__main__":
    main()
