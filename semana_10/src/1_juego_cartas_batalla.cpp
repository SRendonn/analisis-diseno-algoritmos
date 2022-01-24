#include <iostream>
#include <vector>
#include <tuple>
#include <bits/stdc++.h>
#include <math.h>

using namespace std;

uint get_divisores(uint n)
{

    uint factores = 0;
    uint sqrt_n = static_cast<int>(sqrt(n));
    for (uint i = 1; i < sqrt_n + 1; i++)
    {
        if (n % i == 0)
        {
            if (n / i == i)
            {
                factores++;
            }
            else
            {
                factores = factores + 2;
            }
        }
    }
    return factores;
}

uint get_best_card(vector<tuple<uint, uint>> cards)
{
    uint N = cards.size();
    vector<vector<uint>> m(N);

    for (uint i = 0; i < N; i++)
    {
        m[i] = vector<uint>(N, get<1>(cards[i]));
    }

    for (uint matrices = 1; matrices < N; matrices++)
    {
        for (uint i = 0; i < N - matrices; i++)
        {
            uint j = i + matrices;
            uint mayor = 0;
            for (uint k = i; k < j; k++)
            {
                uint S = m[i][k] + m[k + 1][j];
                mayor = max(mayor, S + get_divisores(S));
            }
            m[i][j] = mayor;
        }
    }
    return m[0][N - 1];
}

int main()
{
    ushort C;
    cin >> C;

    for (ushort i = 0; i < C; i++)
    {
        ushort N;
        cin >> N;

        vector<tuple<uint, uint>> card_set;

        for (ushort j = 0; j < N; j++)
        {
            uint id;
            uint power;
            cin >> id;
            cin >> power;
            card_set.push_back(make_tuple(id, power));
        }
        sort(card_set.begin(), card_set.end());

        cout << get_best_card(card_set) << endl;
    }

    return 0;
}