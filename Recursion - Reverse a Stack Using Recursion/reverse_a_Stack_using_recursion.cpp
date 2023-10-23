#include <iostream>
#include <vector>
#include <stack>
using namespace std;

// Recursive function to sort an array using
// insertion sort

void insertAtBottom(stack<int> &st, int temp)
{

    if (st.empty())
    {
        st.push(temp);
        return;
    }
    int top = st.top();
    st.pop();
    insertAtBottom(st, temp);
    st.push(top);
}
void reverseStackRec(stack<int> &st)
{
    // Base case
    if (st.empty())
    {
        return;
    }

    int temp = st.top();
    st.pop();
    reverseStackRec(st);
    insertAtBottom(st, temp);
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

    reverseStackRec(st);
    printArray(st, n);

    return 0;
}