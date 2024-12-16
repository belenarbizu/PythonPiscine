from load_csv import load
import matplotlib.pyplot as plt


def population_life() -> None:
    life_df = load("life_expectancy_years.csv")
    inm_df = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")

    life_1900 = life_df["1900"].to_numpy()
    income_1900 = inm_df["1900"].to_numpy()

    plt.plot(income_1900, life_1900, "bo")
    plt.xscale('log')
    plt.xticks([300, 1000, 10000], ["300", "1k", "10k"])
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life Expectancy")
    plt.title("1900")

    plt.show()


def main():
    population_life()


if __name__ == "__main__":
    main()
