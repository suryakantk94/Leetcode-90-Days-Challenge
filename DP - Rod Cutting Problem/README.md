Problem
  
Cut The Rod To Maximize Profit
Given the prices for rod pieces of every size between 1 inch and n inches, find the maximum total profit that can be made by cutting an n inches long rod inch into pieces.

Example
{
"price ": [1, 5, 8, 9]
}
Output:

10
The rod can be cut in the ways given below:

1 + 1 + 1 + 1 inches will cost price[0] + price[0] + price[0] + price[0] = 4
1 + 1 + 2 inches will cost price[0] + price[0] + price[1] = 7
1 + 3 inches will cost price[0] + price[2] = 9
2 + 2 inches will cost price[1] + price[1] = 10
One piece of 4 inches will cost price[3] = 9
The maximum profit is obtained by cutting it into two pieces 2 inches each.

Notes
Constraints:

1 <= n <= 103
1 <= price of any sized piece of the rod <= 105
