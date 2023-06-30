import random

def generate_lotto_numbers(count):
    lotto_numbers = []
    for _ in range(count):
        numbers = random.sample(range(1, 46), 6)
        numbers.sort()
        lotto_numbers.append(numbers)
    return lotto_numbers

def save_lotto_numbers(numbers):
    with open('lotto.txt', 'w') as file:
        for number_set in numbers:
            line = ' '.join(str(number) for number in number_set)
            file.write(line + '\n')

count = int(input("로또 번호를 몇 개 생성할까요? "))

lotto_numbers = generate_lotto_numbers(count)

save_lotto_numbers(lotto_numbers)

print(f"{count}개의 로또 번호를 생성하고 lotto.txt 파일에 저장했습니다.")
