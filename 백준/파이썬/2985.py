def three_numbers(numbers):
    answer = ""

    if numbers[0] + numbers[1] == numbers[2]:
        answer = f"{numbers[0]}+{numbers[1]}={numbers[2]}"
    elif numbers[0] - numbers[1] == numbers[2]:
        answer = f"{numbers[0]}-{numbers[1]}={numbers[2]}"
    elif numbers[0] * numbers[1] == numbers[2]:
        answer = f"{numbers[0]}*{numbers[1]}={numbers[2]}"
    elif numbers[0] / numbers[1] == numbers[2]:
        answer = f"{numbers[0]}/{numbers[1]}={numbers[2]}"
    elif numbers[0] == numbers[1] + numbers[2]:
        answer = f"{numbers[0]}={numbers[1]}+{numbers[2]}"
    elif numbers[0] == numbers[1] - numbers[2]:
        answer = f"{numbers[0]}={numbers[1]}-{numbers[2]}"
    elif numbers[0] == numbers[1] * numbers[2]:
        answer = f"{numbers[0]}={numbers[1]}*{numbers[2]}"
    elif numbers[0] == numbers[1] / numbers[2]:
        answer = f"{numbers[0]}={numbers[1]}/{numbers[2]}"
            
    return answer

if __name__ == "__main__":
    numbers = list(map(int, input().split()))
    print(three_numbers(numbers))