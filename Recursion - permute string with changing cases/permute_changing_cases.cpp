#include <iostream>
#include <vector>
#include <string>

using namespace std;

void helper(string &s, int idx, string slate, vector<string> &result)
{
    if (s.size() == idx)
    {
        result.push_back(slate);
        return;
    }

    // Inclusion
    //  cout<<"UP"<<up;
    char down = tolower(s[idx]);
    helper(s, idx + 1, slate + down, result);

    // Exclusion
    char up = toupper(s[idx]);
    helper(s, idx + 1, slate + up, result);
}

int main()
{
    string s = "ab";
    int idx = 0;
    string slate;
    vector<string> result;

    helper(s, idx, slate, result);

    // Print the results
    for (const string &str : result)
    {
        cout << str << endl;
    }

    return 0;
}
