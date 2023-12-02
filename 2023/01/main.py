def main():
    sum = 0

    with open("data.txt") as file:
        sum = 0
        for line in file.readlines():
            line = line.strip()

            left = None
            right = None

            for char in line:
                if char.isdigit():
                    if left is None:
                        left = char
                        continue
                    else:
                        right = char
            
            value = int(left + (right or left))
            sum += value

        print("Answer:", sum)

if __name__ == '__main__':
    main()