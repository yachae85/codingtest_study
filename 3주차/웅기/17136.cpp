#include <iostream>
#include <vector>

using namespace std;

int ans = 99999;

int cp[6];

int arr[10][10];

void reverse_number(int i, int j, int d)
{
  for (int y = i; y < i + d; y++)
  {
    for (int x = j; x < j + d; x++)
    {
      if (arr[y][x] == 0)
        arr[y][x] = 1;
      else
        arr[y][x] = 0;
    }
  }
}

int size_of_one(int i, int j, int d)
{
  for (int y = i; y < i + d; y++)
  {
    for (int x = j; x < j + d; x++)
    {
      if (y >= 10 || x >= 10 || arr[y][x] == 0)
        return 0;
    }
  }
  return 1;
}

int is_complete()
{
  for (int i = 0; i < 10; i++)
  {
    for (int j = 0; j < 10; j++)
      if (arr[i][j] != 0)
        return 0;
  }
  return 1;
}

void find(int i, int j, int tcount)
{
  if (tcount > ans)
    return;

  int x, y, c = 0;
  for (y = i; y < 10; y++)
  {
    for (y == i ? x = j : x = 0; x < 10; x++)
    {
      if (arr[y][x])
      {
        c = 1;
        break;
      }
    }
    if (c)
      break;
  }

  for (int d = 5; d >= 1; d--)
  {
    int check_size = size_of_one(y, x, d);
    if (check_size)
    {
      if (cp[d] + 1 > 5)
      {
        return;
      }
      cp[d]++;
      reverse_number(y, x, d);
      find(y, x, tcount + 1);
      reverse_number(y, x, d);
      cp[d]--;
    }
  }

  if (y == 10 && x == 10)
  {
    if (tcount < ans)
      ans = tcount;
  }
}

int main()
{
  int total = 0;
  for (int i = 0; i < 10; i++)
  {
    for (int j = 0; j < 10; j++)
    {
      cin >> arr[i][j];
      if (arr[i][j])
        total++;
    }
  }

  if (total == 100)
  {
    cout << 4 << endl;
    return 0;
  }

  if (total == 0)
  {
    cout << 0 << endl;
    return 0;
  }

  find(0, 0, 0);

  if (ans != 99999)
    cout << ans << endl;
  else
  {
    for (int i = 0; i < 10; i++)
    {
      for (int j = 0; j < 10; j++)
      {
        if (arr[i][j] == 1)
        {
          cout << -1 << endl;
          return 0;
        }
      }
    }
    cout << 0 << endl;
  }

  return 0;
}