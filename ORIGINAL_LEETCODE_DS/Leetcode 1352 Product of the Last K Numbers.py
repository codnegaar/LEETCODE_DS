'''
Leetcode 1352 Product of the Last K Numbers
  
Design an algorithm that accepts a stream of integers and retrieves the product of the last k integers of the stream.
Implement the ProductOfNumbers class:
ProductOfNumbers() Initializes the object with an empty stream.
void add(int num) Appends the integer num to the stream.
int getProduct(int k) Returns the product of the last k numbers in the current list. You can assume that always the current list has at least k numbers.
The test cases are generated so that, at any time, the product of any contiguous sequence of numbers will fit into a single 32-bit integer without overflowing.

Example:        
        Input
                ["ProductOfNumbers","add","add","add","add","add","getProduct","getProduct","getProduct","add","getProduct"]
                [[],[3],[0],[2],[5],[4],[2],[3],[4],[8],[2]]
        
        Output
                [null,null,null,null,null,null,20,40,0,null,32]
        
        Explanation
                ProductOfNumbers productOfNumbers = new ProductOfNumbers();
                productOfNumbers.add(3);        // [3]
                productOfNumbers.add(0);        // [3,0]
                productOfNumbers.add(2);        // [3,0,2]
                productOfNumbers.add(5);        // [3,0,2,5]
                productOfNumbers.add(4);        // [3,0,2,5,4]
                productOfNumbers.getProduct(2); // return 20. The product of the last 2 numbers is 5 * 4 = 20
                productOfNumbers.getProduct(3); // return 40. The product of the last 3 numbers is 2 * 5 * 4 = 40
                productOfNumbers.getProduct(4); // return 0. The product of the last 4 numbers is 0 * 2 * 5 * 4 = 0
                productOfNumbers.add(8);        // [3,0,2,5,4,8]
                productOfNumbers.getProduct(2); // return 32. The product of the last 2 numbers is 4 * 8 = 32 
 
Constraints:
        0 <= num <= 100
        1 <= k <= 4 * 104
        At most 4 * 104 calls will be made to add and getProduct.
        The product of the stream at any point in time will fit in a 32-bit integer.

'''

class ProductOfNumbers:
    """
    A class that maintains a list of numbers and allows retrieval of the product
    of the last k numbers efficiently.
    """

    def __init__(self):
        """Initializes the prefix product list, starting with 1 for multiplication convenience."""
        self.prefix_product = [1]  # Stores cumulative product, reset on zero

    def add(self, num: int):
        """
        Adds a number to the sequence.
        
        Args:
            num (int): The number to be added.
        """
        if num == 0:
            # Reset the prefix product since any product including zero is zero
            self.prefix_product = [1]
        else:
            # Append the new cumulative product
            self.prefix_product.append(self.prefix_product[-1] * num)

    def getProduct(self, k: int) -> int:
        """
        Returns the product of the last k numbers added.
        
        Args:
            k (int): The number of last elements to consider.

        Returns:
            int: The product of the last k numbers or 0 if k exceeds stored numbers.
        """
        if k >= len(self.prefix_product):
            return 0  # If k is larger than stored numbers, it means a zero was encountered

        return self.prefix_product[-1] // self.prefix_product[-k - 1]  # Compute product efficiently


# Example usage
product_of_numbers = ProductOfNumbers()
product_of_numbers.add(3)
product_of_numbers.add(2)
product_of_numbers.add(5)
print(product_of_numbers.getProduct(2))  # Output: 10 (2 * 5)
product_of_numbers.add(0)
product_of_numbers.add(4)
print(product_of_numbers.getProduct(1))  # Output: 4
print(product_of_numbers.getProduct(2))  # Output: 4 (as 0 reset previous products)
