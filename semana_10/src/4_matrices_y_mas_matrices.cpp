#include <iostream>
#include <vector>
#include <limits>

using namespace std;

void parentizacion(uint i, uint j, vector<vector<uint>> S)
{
}

void get_matrix(vector<uint> p)
{
    uint N = p.size();
    vector<vector<uint>> m(N, vector<uint>(N, 0));
    vector<vector<uint>> S(N, vector<uint>(N));

    for (uint matrices = 1; matrices < N; matrices++)
    {
        for (uint i = 0; i < N - matrices; i++)
        {
            uint j = i + matrices;
            uint menor = numeric_limits<uint>().max();
            for (uint k = i; k < j; k++)
            {
                uint Q = m[i][k] + m[k + 1][j] + p[i] * p[k] * p[j];
                if (Q < menor)
                {
                    menor = Q;
                    S[i][j] = k;
                }
            }
            m[i][j] = menor;
        }
    }
    parentizacion(0, N - 1, S);
}

int main()
{
    ushort C;
    cin >> C;
    for (ushort i; i < C; i++)
    {
        vector<uint> p;

        uint N;
        cin >> N;
        p.push_back(N);

        while (cin.peek() != '\n' && cin >> N)
        {
            p.push_back(N);
        }
        get_matrix(p);
    }
    return 0;
}