def main():
    item_price = -2.99
    # Setting this to negative causes a ValueError: Price cannot be negative. 
    # This error occurs on line 19, where the "if" block catched the error.
    quantity = -3
    # Making this negative also results in a ValueError: Quantities cannot be negative.
    # Making BOTH of these quantities negative only results in a ValueError for the item price, but does not show the quantity is negative as well.
    print(f"{quantity} items at ${item_price} each is:")
    print(f"${calc_subtotal(item_price, quantity)}")

def calc_subtotal(price: float, quantity: int) -> float:
    """Calculate the subtotal for a single item in a cart.
    
    Args:
        price: The price of a single item.
        quantity: Number of a particular item in the cart.

    Returns:
        The subtotal
    """
    if price < 0:
        raise ValueError("Price cannot be negative.")
    elif quantity < 0:
        raise ValueError("Quantities cannot be negative.")

    return price * quantity

if __name__ == "__main__":
    main()
