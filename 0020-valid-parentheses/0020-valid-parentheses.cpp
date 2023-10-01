class Solution {
public:
    bool isValid(string s) {
        stack<char> st;

        for (int i = 0; i < s.length(); i++){
            if(!st.empty()){

                if(st.top () == '(' && s[i] == ')')
                    {
                cout<<"S"<<st.top()<<endl;
                    st.pop();
                    }
                else if (st.top () == '{' && s[i] == '}')
                    st.pop();
                else if (st.top () == '[' && s[i] == ']')
                    st.pop();
                else
                    st.push(s[i]);

            }
            else{
                cout<<s[i]<<endl;
                st.push(s[i]);
            }
        }
        // cout<<"T"<<st.top()<<endl;
        return st.empty();
    }
};