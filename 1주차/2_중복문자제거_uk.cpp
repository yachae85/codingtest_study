class Solution {
public:
    string result;
    int alp[26];
    
    string removeDuplicateLetters(string s) {
        
        vector<queue<int>> arr(26);
        int count = 0;
        
        for(int i = 0; i < s.length(); i++)
        {
            if(arr[(int)s[i] - (int)'a'].size() == 0)
            {
                count++;
            }
            
            arr[(int)s[i] - (int)'a'].push(i);
        }
        
        int alpnum=-1;
        int sindex;
        for(int i = 0; i < 26; i++)
        {
            if(!arr[i].empty())
            {
                if(alpnum == -1)
                {
                    if(arr[i].front() <= (s.length() - count))
                    {
                        alpnum = i;
                        sindex = arr[i].front();
                    }
                }
                else
                {
                    if(arr[i].back() < sindex)
                    {
                        alpnum = i;
                        sindex = arr[i].front();
                    }
                }
                
            }
        }
        
        result += (char)((int)'a' + alpnum);
        
        printf("%d %d\n", alpnum, sindex);
        
        vector<pair<int, int>> ar;
        
        for(int i = 0; i < 26; i++)
        {
            if(!arr[i].empty() && i != alpnum)
            {
                while(1)
                {
                    if(arr[i].front() < sindex)
                        arr[i].pop();
                    else
                    {
                        ar.push_back(make_pair(arr[i].front() ,i));
                        break;
                    }
                }
            }
        }
        
        sort(ar.begin(), ar.end());
        
        for(int i= 0; i < ar.size(); i++)
        {
            result += (char)((int)'a' + ar[i].second);
        }
        
        return result;
    }
};