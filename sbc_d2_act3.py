import random

def result():
    return [random.randint(1, 10) for _ in range(3)]

def check_win(bet, result):
    return "You win!" if bet == result else "You partially win!" if set(bet) == set(result) else "You lose!"

def main():
    try:
        bet = list(map(int, input("Enter your bet (e.g., 1 2 3): ").split()))
        result = result()
        print(f"Result: {result} {check_win(bet, result)}")
    except ValueError:
        print("Invalid input. Please enter three space-separated numbers.")

if __name__ == "__main__":
    main()
