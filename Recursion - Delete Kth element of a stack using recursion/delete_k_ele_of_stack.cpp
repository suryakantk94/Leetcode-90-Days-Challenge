#include <iostream>
#include <vector>
#include <stack>
using namespace std;

// Recursive function to sort an array using
// insertion sort

void deleteKthelement(stack<int> &st, int k, int n)
{
    // Base case
    if (k == 1)
    {
        st.pop();
        return;
    }

    int temp = st.top();
    st.pop();
    deleteKthelement(st, k - 1, n);

    // Insert the last element in the right position in the sorted part of the array
    st.push(temp);
}

// A utility function to print an array
void printArray(stack<int> &st, int n)
{
    while (!st.empty())
    {
        cout << st.top();
        st.pop();
        cout << endl;
    }
}

/* Driver program to test insertion sort */
int main()
{
    vector<int> v = {1, 2, 3, 4, 5, 6};
    int n = v.size();
    int k = n / 2 + 1;

    stack<int> st;

    for (int i = 0; i < n; i++)
        st.push(v[i]);

    deleteKthelement(st, k, n);
    printArray(st, n);

    return 0;
}