def generate_even_numbers(n):
    """
    Generate a list of even numbers from 0 to n.
    
    Args:
        n (int): The upper limit for generating even numbers.
    
    Returns:
        list: A list of even numbers.
    """
    even_numbers = []
    for i in range(n + 1):
        if i % 2 == 0:
            even_numbers.append(i)
    return even_numbers

def main():
    # Define the upper limit for generating even numbers
    limit = 10
    
    # Generate even numbers
    even_numbers = generate_even_numbers(limit)
    
    # Print the generated even numbers
    print("Even numbers from 0 to {}:".format(limit))
    for num in even_numbers:
        print(num)

if __name__ == "__main__":
    main()
