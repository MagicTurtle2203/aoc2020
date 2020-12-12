#include <fstream>
#include <iostream>
#include <string>
#include <set>
#include <vector>

int main()
{
    std::vector<int> v;
    std::ifstream input("input.txt");

    int n;

    while (input >> n)
    {
        v.push_back(n);
    }

    for (int i = 0; i < v.size(); i++)
    {
        std::set<int> s;
        int curr_sum = 2020 - v[i];
        for (int j = i + 1; j < v.size(); j++)
        {
            if (s.count(curr_sum - v[j]) > 0)
            {
                std::cout << v[i] * v[j] * (curr_sum - v[j]) << std::endl;
                return 0;
            }
            s.insert(v[j]);
        }
    }
}