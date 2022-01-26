#include <iostream>
#include <vector>
#include <limits>

using namespace std;

string parentizacion(uint i, uint j, vector<vector<uint>> S)
{
    if (i == j)
    {
        return "M" + to_string(i);
    }
    else
    {
        string res = "";
        res += "(";
        res += parentizacion(i, S[i][j], S);
        res += " x ";
        res += parentizacion(1 + S[i][j], j, S);
        res += ")";
        return res;
    }
}

void get_matrix(vector<uint> p)
{
    uint N = p.size();
    vector<vector<uint>> m(N, vector<uint>(N, 0));
    vector<vector<uint>> S(N, vector<uint>(N, 0));

    for (uint matrices = 1; matrices < N; matrices++)
    {
        for (uint i = 0; i < N - matrices; i++)
        {
            uint j = i + matrices;
            uint menor = numeric_limits<uint>().max();
            for (uint k = i; k < j; k++)
            {
                uint Q;
                if (i == 0)
                {
                    Q = m[i][k] + m[k + 1][j] + p[k] * p[j];
                }
                else
                {
                    Q = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j];
                }

                if (Q < menor)
                {
                    menor = Q;
                    S[i][j] = k;
                }
            }
            m[i][j] = menor;
        }
    }

    cout << parentizacion(1, N - 1, S) << endl;
}

int main()
{
    ushort C;
    cin >> C;
    for (ushort i = 0; i < C; i++)
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