#include <iostream>
#include <vector>

using namespace std;

//H = 가로, V = 세로, D = 대각선
enum state
{
  H,
  V,
  D
};

pair<pair<int, int>, state> pipe;
int arr[17][17];

int n;
int ans;

void find()
{
  if (pipe.first.first == n && pipe.first.second == n) // (n, n) 좌표에 도달할 경우
  {
    ans++; //ans를 1 증가
    return;
  }

  pair<int, int> curpos = pipe.first;
  state curstate = pipe.second;

  switch (curstate)
  {
  case H: //가로인 경우
    if (curpos.second + 1 <= n)
    {
      if (arr[curpos.first][curpos.second + 1] == 0) //가로로 직진
      {
        pipe.first = make_pair(curpos.first, curpos.second + 1);
        find();
        pipe.first = curpos;
      }

      if (curpos.second + 1 <= n) //대각선으로 직진
      {
        if (arr[curpos.first][curpos.second + 1] == 0 && arr[curpos.first + 1][curpos.second] == 0 && arr[curpos.first + 1][curpos.second + 1] == 0)
        {
          pipe.first = make_pair(curpos.first + 1, curpos.second + 1);
          pipe.second = D;
          find();
          pipe.first = curpos;
          pipe.second = H;
        }
      }
    }
    break;
  case V: //세로인 경우
    if (curpos.first + 1 <= n)
    {
      if (arr[curpos.first + 1][curpos.second] == 0) //세로로 직진
      {
        pipe.first = make_pair(curpos.first + 1, curpos.second);
        find();
        pipe.first = curpos;
      }

      if (curpos.second + 1 <= n) //대각선으로 직진
      {
        if (arr[curpos.first][curpos.second + 1] == 0 && arr[curpos.first + 1][curpos.second] == 0 && arr[curpos.first + 1][curpos.second + 1] == 0)
        {
          pipe.first = make_pair(curpos.first + 1, curpos.second + 1);
          pipe.second = D;
          find();
          pipe.first = curpos;
          pipe.second = V;
        }
      }
    }
    break;
  case D:                       //대각선인 경우
    if (curpos.second + 1 <= n) //가로로 직진
    {
      if (arr[curpos.first][curpos.second + 1] == 0)
      {
        pipe.first = make_pair(curpos.first, curpos.second + 1);
        pipe.second = H;
        find();
        pipe.first = curpos;
        pipe.second = D;
      }
    }
    if (curpos.first + 1 <= n) //세로로 직진
    {
      if (arr[curpos.first + 1][curpos.second] == 0)
      {
        pipe.first = make_pair(curpos.first + 1, curpos.second);
        pipe.second = V;
        find();
        pipe.first = curpos;
        pipe.second = D;
      }
    }
    if (curpos.first + 1 <= n && curpos.second + 1 <= n) //대각선으로 직진
    {
      if (arr[curpos.first][curpos.second + 1] == 0 && arr[curpos.first + 1][curpos.second] == 0 && arr[curpos.first + 1][curpos.second + 1] == 0)
      {
        pipe.first = make_pair(curpos.first + 1, curpos.second + 1);
        find();
        pipe.first = curpos;
      }
    }
    //가로로 직진
    //세로로 직진
    //대각선으로 직진
    break;
  default:
    cout << "응 잘못 넣었어~" << endl;
    break;
  }
}

int main()
{

  cin >> n;

  for (int i = 1; i <= n; i++)
  {
    for (int j = 1; j <= n; j++)
    {
      cin >> arr[i][j];
    }
  }

  pipe.first = make_pair(1, 2);
  pipe.second = H;

  find();

  cout << ans << endl;

  return 0;
}