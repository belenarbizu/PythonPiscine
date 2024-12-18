from load_csv import load
import matplotlib.pyplot as plt


def change_format_data(value) -> float:
    """
    Changes csv values with M and k format
    """
    if isinstance(value, str):
        if value.endswith("M"):
            return float(value[:-1]) * 1e6
        if value.endswith("k"):
            return float(value[:-1]) * 1e3
    return float(value)


def population_info(path: str) -> None:
    """
    Shows the graphic of Spain and France population
    """
    dataset = load(path)

    df_spain = dataset[dataset["country"] == "Spain"].iloc[0]
    df_france = dataset[dataset["country"] == "France"].iloc[0]

    years = df_spain.index[1:252].to_numpy(dtype=int)

    values_spain = df_spain.values[1:252]
    values_france = df_france.values[1:252]

    values_spain = [change_format_data(value) for value in values_spain]
    values_france = [change_format_data(value) for value in values_france]

    plt.plot(years, values_spain, label="Spain")
    plt.plot(years, values_france, label="France")
    plt.yticks([20e6, 40e6, 60e6], ["20M", "40M", "60M"])
    plt.xticks(years[::40])
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.title("Population Projections")
    plt.legend()

    plt.show()


def main():
    population_info("population_total.csv")


if __name__ == "__main__":
    main()
