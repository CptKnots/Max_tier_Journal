from make_list import update_kingdom


def main():
    species1 = input("Enter species 1: ")
    kingdom1 = update_kingdom(species1)
    print(f"Kingdom for {species1}: {kingdom1}")

    species2 = input("Enter species 2: ")
    kingdom2 = update_kingdom(species2)
    print(f"Kingdom for {species2}: {kingdom2}")

if __name__ == "__main__":
    main()
    
