#include <iostream>
#include <tuple>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

bool check_diags(vector<ushort> squares)
{
    for (ushort i = 0; i < squares.size() - 1; i++)
    {
        ushort p = 1;
        for (ushort j = i + 1; j < squares.size(); j++)
        {
            if (squares[j] == squares[i] + p || squares[j] == squares[i] - p)
            {
                return false;
            }
            p++;
        }
    }
    return true;
}

int queens_dist(ushort N, tuple<int, int> first_miss, tuple<int, int> second_miss)
{
    ushort cont = 0;
    vector<ushort> squares;
    for (ushort i = 0; i < N; i++)
    {
        if (i != get<1>(first_miss) && i != get<1>(second_miss))
        {
            squares.push_back(i);
        }
    }

    do
    {
        vector<ushort> validCols;
        ushort pos = 0;

        for (ushort i = 0; i < N; i++)
        {
            if (i == get<0>(first_miss))
            {
                validCols.push_back(get<1>(first_miss));
                pos++;
            }
            else if (i == get<0>(second_miss))
            {
                validCols.push_back(get<1>(second_miss));
                pos++;
            }
            else
            {
                validCols.push_back(squares[i - pos]);
            }
        }

        if (check_diags(validCols))
        {
            cont++;
        }
    } while (next_permutation(squares.begin(), squares.end()));

    return cont;
}

int main()
{
    ushort C = 0;
    cin >> C;
    for (ushort i = 0; i < C; i++)
    {
        ushort N = 0;
        ushort first_x = 0;
        ushort first_y = 0;
        ushort second_x = 0;
        ushort second_y = 0;
        cin >> N;
        cin >> first_x;
        cin >> first_y;
        cin >> second_x;
        cin >> second_y;
        cout << queens_dist(N, make_tuple(first_x - 1, first_y - 1), make_tuple(second_x - 1, second_y - 1)) << endl;
    }

    return 0;
}