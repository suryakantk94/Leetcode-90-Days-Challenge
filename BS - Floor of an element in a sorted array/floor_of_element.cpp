// A C/C++ program to find floor
// of a given number in a sorted array
#include <bits/stdc++.h>
using namespace std;

/* Function to get index of floor of x in
   arr[low..high] */
int floorSearch(int arr[], int low, int high, int x)
{
    int floor = -1;

    while (low <= high)
    {

        int mid = low + (high - low) / 2;

        if (arr[mid] == x)
            return mid;
        else if (arr[mid] < x)
            floor = mid;

        if (x > arr[mid])
            low = mid + 1;
        else
            high = mid - 1;
    }
    return floor;
}

// Driver code
int main()
{
    int arr[] = {1, 2, 4, 6, 10, 10, 12, 14};
    int n = sizeof(arr) / sizeof(arr[0]);
    int x = 1;

    // Function call
    int index = floorSearch(arr, 0, n - 1, x);
    if (index == -1)
        cout << "Floor of " << x
             << " doesn't exist in array ";
    else
        cout << "Floor of " << x << " is " << arr[index];
    return 0;
}