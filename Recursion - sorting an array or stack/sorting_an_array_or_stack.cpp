#include <iostream>
#include <vector>
#include <stack>
using namespace std;

// Recursive function to sort an array using
// insertion sort
void insert(stack<int> &st, int temp)
{
    // Base case: if the vector is empty or the last element is less than or equal to temp
    if (st.size() == 0 || st.top() <= temp)
    {
        st.push(temp);
        return;
    }
    int val = st.top();
    st.pop();
    insert(st, temp);
    st.push(val);
}

void insertionSortRecursive(stack<int> &st)
{
    // Base case
    if (st.size() == 1)
        return;

    int temp = st.top();
    st.pop();
    insertionSortRecursive(st);

    // Insert the last element in the right position in the sorted part of the array
    insert(st, temp);
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
    vector<int> v = {12, 11, 13, 5, 6};
    int n = v.size();
    stack<int> st;

    for (int i = 0; i < n; i++)
        st.push(v[i]);

    insertionSortRecursive(st);
    printArray(st, n);

    return 0;
}
