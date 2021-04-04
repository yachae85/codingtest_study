#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>

using namespace std;

int n, k;
vector<int> s(101);
vector<int> r(101);
vector<int> p(101);

int main()
{
  cin >> n >> k;

  for (int i = 1; i <= k; i++)
  {
    int temp;
    cin >> temp;
    s[i] = temp;
    r[temp]++;
  }

  int ans = 0;
  int u = 0;

  for (int i = 1; i <= k; i++)
  {
    int t = s[i];
    if (u < n)
    {
      if (!p[t])
      {
        p[t] = 1;
        u++;
      }
      r[t]--;
      continue;
    }
    else if (u == n)
    {
      if (p[t] == 1)
      {
        r[t]--;
        continue;
      }
      else
      {
        int next = 0;
        for (int j = 1; j <= k; j++)
        {
          int k = s[j];
          if (r[k] == 0 && p[k] == 1)
          {
            next = k;
            break;
          }
        }
        if (next)
        {
          p[next] = 0;
          p[t] = 1;
          r[t]--;
          ans++;
          continue;
        }
        else
        {
          int next;
          vector<int> temp = p;
          int check = u;
          for (int j = i + 1; j <= k; j++)
          {
            if (temp[s[j]])
            {
              if (check == 1)
              {
                next = s[j];
                break;
              }
              else
              {
                temp[s[j]] = 0;
                check--;
              }
            }
          }
          p[next] = 0;
          p[t] = 1;
          r[t]--;
          ans++;
          continue;
        }
      }
    }
  }

  cout << ans << endl;
}