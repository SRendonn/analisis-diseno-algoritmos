#include <iostream>
#include <sstream>
#include <bits/stdc++.h>

using namespace std;

bool check_heredero(uint num)
{
    string num_str = to_string(num);
    if (num_str.size() % 2 != 0)
    {
        return false;
    }

    do
    {
        string parent_number_1_str;
        string parent_number_2_str;

        for (uint i = 0; i < num_str.size(); i++)
        {
            if (i % 2 == 0)
            {
                parent_number_1_str = parent_number_1_str + num_str[i];
            }
            else
            {
                parent_number_2_str = parent_number_2_str + num_str[i];
            }
        }

        stringstream parent_number_1_ss(parent_number_1_str);
        stringstream parent_number_2_ss(parent_number_2_str);

        uint parent_number_1;
        uint parent_number_2;

        parent_number_1_ss >> parent_number_1;
        parent_number_2_ss >> parent_number_2;

        if (parent_number_1 * parent_number_2 == num)
        {
            return true;
        }

    } while (next_permutation(num_str.begin(), num_str.end()));

    return false;
}

int main()
{
    ushort C = 0;
    cin >> C;
    for (ushort i = 0; i < C; i++)
    {
        uint num = 0;
        cin >> num;
        cout << ((check_heredero(num)) ? "Heredero" : "No") << endl;
    }
    return 0;
}