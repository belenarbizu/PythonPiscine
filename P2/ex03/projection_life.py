from load_csv import load
import matplotlib.pyplot as plt

def population_life(life_path: str, income_path: str) -> None:
    life_df = load(life_path)
    income_df = load(income_path)

    life_1900 = life_df["1900"]
    print(life_1900)
    income_1900 = income_df["1900"]

    plt.plot(income_1900, life_1900, "ro", color="blue")
    plt.xscale('log')
    plt.xticks([300, 1000, 10000], ["300", "1k", "10k"])
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life Expectancy")
    plt.title("1900")

    plt.show()

def main():
    population_life("life_expectancy_years.csv", "income_per_person_gdppercapita_ppp_inflation_adjusted.csv")


if __name__ == "__main__":
    main()