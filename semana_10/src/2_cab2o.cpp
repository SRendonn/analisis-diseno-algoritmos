#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

uint get_best_tree(vector<uint> items)
{
    uint N = items.size();
    vector<vector<uint>> C(N, vector<uint>(N, 0));
    vector<vector<uint>> sumP(N, vector<uint>(N, 0));

    for (uint i = 0; i < N; i++)
    {
        uint suma = 0;
        for (uint j = i; j < N; j++)
        {
            suma = suma + items[j];
            sumP[i][j] = suma;
        }
    }

    for (uint i = 0; i < N; i++)
    {
        C[i][i] = items[i];
    }

    for (uint nodos = 1; nodos < N; nodos++)
    {
        for (uint i = 0; i < N - nodos; i++)
        {
            uint j = i + nodos;
            uint menor = 10000;
            for (uint r = i + 1; r < j; r++)
            {
                menor = min(menor, C[i][r - 1] + C[r + 1][j] + sumP[i][j]);
            }
            C[i][j] = menor;
        }
    }
    return C[0][N - 1];
}

int main()
{
    ushort C;
    cin >> C;

    for (ushort i = 0; i < C; i++)
    {
        vector<uint> items;

        uint N;
        cin >> N;
        items.push_back(N);

        while (cin.peek() != '\n' && cin >> N)
        {
            items.push_back(N);
        }

        cout << get_best_tree(items) << endl;
    }

    return 0;
}