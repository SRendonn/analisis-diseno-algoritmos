#include <iostream>
#include <array>
#include <bits/stdc++.h>

using namespace std;

int is_n_muda(array<unsigned short, 9> a, unsigned short n)
{
  if (a[0] + a[1] + a[2] + a[3] == n && a[3] + a[4] + a[5] + a[6] == n && a[6] + a[7] + a[8] + a[0] == n)
  {
    return 1;
  }
  return 0;
}

int main()
{
  ushort C;
  cin >> C;

  for (ushort i = 0; i < C; i++)
  {
    ushort n;
    cin >> n;
    array<ushort, 9> mudas;
    uint n_mudas = 0;

    for (ushort j = 0; j < 9; j++)
    {
      ushort muda_aux;
      cin >> muda_aux;
      mudas[j] = muda_aux;
    }

    sort(mudas.begin(), mudas.end());

    do
    {
      n_mudas = n_mudas + is_n_muda(mudas, n);
    } while (next_permutation(mudas.begin(), mudas.end()));

    cout << n_mudas << endl;
  }
  return 0;
}