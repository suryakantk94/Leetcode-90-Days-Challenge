#include <iostream>
#include <array>
using namespace std;

class BinarySearchNearlySortedArray
{

public:
    static int binarySearchNearlySorted(int a[], int n, int target)
    {
        int start = 0;
        int end = sizeof(a) - 1;

        while (start <= end)
        {

            int mid = start + (end - start) / 2;

            if (a[mid] == target)
                return mid;
            else if (a[mid - 1] == target && mid >= start)
                return mid - 1;
            else if (a[mid + 1] == target && mid <= end)
                return mid + 1;

            if (a[mid] < target)
                start = mid + 2;
            else if (a[mid] > target)
                end = mid - 2;
        }
        return -1;
    }
};

int main()
{
    int arr[] = {15, 20, 30, 25, 35};
    int target;
    int n = sizeof(arr) / sizeof(arr[0]);

    cout << "Enter the target value: ";
    cin >> target;

    int index = BinarySearchNearlySortedArray::binarySearchNearlySorted(arr, n, target);
    if (index == -1)
        cout << target << " not found in the array" << endl;
    else
        cout << target << " found at index " << index << endl;

    return 0;
}
