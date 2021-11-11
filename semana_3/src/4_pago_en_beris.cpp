#include <iostream>

using namespace std;

uint BERIS[9] = {10000, 5000, 1000, 500, 100, 50, 10, 5, 1};

uint change(uint num)
{
    uint cambio = 0;
    for (uint i = 0; i < 9; i++)
    {
        if (num >= BERIS[i])
        {
            cambio = cambio + num / BERIS[i];
            num = num % BERIS[i];
        }
    }
    return cambio;
}

int main()
{
    uint N;
    cin >> N;
    for (uint i = 0; i < N; i++)
    {
        uint num;
        cin >> num;
        cout << change(num) << endl;
    }

    return 0;
}