#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int main()
{
    ushort P;
    cin >> P;

    for (ushort i = 0; i < P; i++)
    {
        ushort C;
        cin >> C;
        vector<vector<_Float32>> dist_matrix;

        for (ushort j = 0; j < C; j++)
        {
            vector<_Float32> row;
            dist_matrix.push_back(row);
            for (ushort k = 0; k < C; k++)
            {
                _Float32 path;
                cin >> path;
                if (cin.fail())
                {
                    cin.clear();
                    path = nanf32("");
                    cin.ignore();
                }
                dist_matrix[j].push_back(path);
            }
        }
        cout << "------------" << endl;
        for (ushort j = 0; j < C; j++)
        {
            for (ushort k = 0; k < C; k++)
            {
                cout << dist_matrix[j][k] << " ";
            }
            cout << endl;
        }
    }
    return 0;
}