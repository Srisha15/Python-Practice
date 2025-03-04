bidding_db = {}
def function_input():
    name = input("Enter your name:")
    bid = int(input("Enter the amount you want to bid:$"))
    # input takes in string as input so convert it into int


    # Storing into dictionary
    bidding_db[name] = bid


    choice = input("Are there any other bidders?: Type 'yes' or 'no' for an answer").strip().lower()

    # strip used to remove any spaces user maight have enteres accidently

    if choice == 'yes':
        function_input()
    else:
        # print("The winner is" + max(bidding_db.values()))
        # max compares key by deafult we need to make it to comapre values

        
        max_bidder = max(bidding_db, key=bidding_db.get)

        # max(iterable, key=function)
        # max() is a built-in Python function that returns the maximum value from an iterable.
        # The key argument specifies a function that will be used to extract a comparison value from each element in the iterable.

        # bidding_db.get(name) retrieves the bid amount for each bidder (name).
        # Example:
        # bidding_db.get("Alice") → 200
        # bidding_db.get("Bob") → 450
        # bidding_db.get("Charlie") → 300

        # max(bidding_db, key=bidding_db.get) will:
        # Look at each key in bidding_db ("Alice", "Bob", "Charlie").
        # Pass each key through bidding_db.get() to retrieve the bid amount.
        # Compare the values and return the key with the highest value.

        
        print("The winner is " + max_bidder )

# print(bidding_db)


function_input()


