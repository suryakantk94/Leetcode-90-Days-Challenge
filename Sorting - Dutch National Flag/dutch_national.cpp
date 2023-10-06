// swap()
vector<char> dutch_flag_sort(vector<char> &balls)
{
    // Write your code here.
    // three pointers approach.. two cannot make it

    int n = balls.size();
    int low = 0, mid = 0;
    int high = n - 1;

    while (mid <= high)
    {
        if (balls[mid] == 'R')
        {
            char temp = balls[low];
            balls[low] = balls[mid];
            balls[mid] = temp;
            // swap(low, mid);
            low++;
            mid++;
        }
        else if (balls[mid] == 'B')
        {
            // swap(mid, high);
            char temp = balls[high];
            balls[high] = balls[mid];
            balls[mid] = temp;
            high--;
            // mid++;
        }
        else
        {
            mid++;
        }
    }

    return balls;
}
