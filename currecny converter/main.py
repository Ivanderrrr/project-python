def main():
    print("This program converts US dollars to Rupiah \n")
    
    dollars = int(input("Enter amount in dollars: "))
    rupiah = convert_to_rupiah(dollars)
    
    print("That is", rupiah, "rupiah")
    
convert_to_rupiah = lambda dollars: dollars * 15515.00

main()