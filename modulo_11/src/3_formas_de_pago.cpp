#include <iostream>
#include <array>

using namespace std;

array<long, 7> monedas = {1, 2, 5, 10, 20, 50, 100};
array<array<long, 7>, 50001> m({0});

void cache_coin_change()
{
    for (uint i = 0; i < 7; i++)
    {
        m[0][i] = 1;
    }
    for (long i = 1; i < 50001; i++)
    {
        for (long j = 0; j < 7; j++)
        {
            ulong x = 0;
            ulong y = 0;

            if (i - monedas[j] >= 0)
            {
                m[i][j] += m[i - monedas[j]][j];
            }
            if (j >= 1)
            {
                m[i][j] += m[i][j - 1];
            }
        }
    }
}

ulong get_coin_change(uint N)
{
    uint aux;
    for (int i = 6; i >= 0; i--)
    {
        if (N >= monedas[i])
        {
            aux = i;
            break;
        }
    }
    return m[N][aux];
}

int main()
{
    cache_coin_change();
    uint N;
    cin >> N;
    while (N != 0)
    {
        cout << get_coin_change(N) << endl;
        cin >> N;
    }
}