from load_csv import load
import matplotlib.pyplot as plt

def population_life(life_path: str, income_path: str) -> None:
    life_df = load(life_path)
    income_df = load(income_path)


    plt.xlabel("Gross domestic product")
    plt.ylabel("Life Expectancy")
    plt.title("1900")

    plt.show()

def main():
    population_life("life_expectancy_years.csv", "income_per_person_gdppercapita_ppp_inflation_adjusted.csv")


if __name__ == "__main__":
    main()