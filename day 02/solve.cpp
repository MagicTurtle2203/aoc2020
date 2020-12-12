#include <fstream>
#include <iostream>
#include <string>

int main()
{
    int pos1, pos2;
    char c;
    char throwaway;
    std::string str;
    int counts = 0;

    std::ifstream input("input.txt");
    while (input >> pos1 >> pos2 >> c >> throwaway >> str)
    {
        pos2 = -1 * pos2;
        counts += (str[pos1 - 1] == c) ^ (str[pos2 - 1] == c);
    }
    std::cout << counts << std::endl;
}
