

vector<int> find_top_k_frequent_elements(vector<int> &arr, int k)
{
    // Write your code here.
    // create an unordered map of int int

    if (arr.size() == k)
        return arr;

    unordered_map<int, int> map;

    for (int i = 0; i < arr.size(); i++)
    {
        if (map.find(arr[i]) != map.end())
        {
            // push the element to the map
            map[arr[i]]++;
        }
        else
        {
            map[arr[i]] = 1;
        }
    }
    // priority_queue< pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>> > minHeapPQ;

    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> mh;

    for (pair<int, int> itr : map)
    {
        mh.push({itr.second, itr.first});

        if (mh.size() > k)
        {
            mh.pop();
        }
    }
    vector<int> res;

    for (int i = 0; i < k; i++)
    {
        res.push_back(mh.top().second);
        mh.pop();
    }

    return res;
}
