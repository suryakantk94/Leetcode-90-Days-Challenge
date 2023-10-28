void helper(int n, int s, int d, int h, vector<vector<int>> &slate)
{

    if (n == 1)
    {
        cout << "Plate moved from " << s << " to " << d << endl;
        slate.push_back({s, d});
        return;
    }
    helper(n - 1, s, h, d, slate);
    cout << "Plate moved from " << s << " to " << d << endl;
    slate.push_back({s, d});

    helper(n - 1, h, d, s, slate);
}

vector<vector<int>> tower_of_hanoi(int n)
{
    // Write your code here.
    int s = 1, d = 3, h = 2;
    vector<vector<int>> slate;

    helper(n, s, d, h, slate);

    return slate;
}
