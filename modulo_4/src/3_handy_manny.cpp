#include <iostream>
#include <vector>
#include <tuple>
#include <algorithm>

using namespace std;

int min_fine(uint N, vector<uint> times, vector<uint> fines)
{

    vector<tuple<float, uint>> weights(N);

    for (uint i = 0; i < N; i++)
    {
        float weight = static_cast<float>(fines[i]) / times[i];
        weights[i] = make_tuple(weight, i);
    }

    sort(weights.begin(), weights.end(), greater<tuple<float, uint>>());

    uint time = 0;
    uint delay = 0;
    uint fine = 0;

    for (uint i = 0; i < N; i++)
    {
        time = time + times[get<1>(weights[i])];
        delay = time - times[get<1>(weights[i])];
        fine = fine + delay * fines[get<1>(weights[i])];
    }

    return fine;
}

int main()
{
    uint C;
    cin >> C;

    for (uint i = 0; i < C; i++)
    {
        uint N;
        cin >> N;

        vector<uint> times(N);
        vector<uint> fines(N);

        for (uint j = 0; j < N; j++)
        {
            cin >> times[j];
            cin >> fines[j];
        }
        cout << min_fine(N, times, fines) << endl;
    }

    return 0;
}