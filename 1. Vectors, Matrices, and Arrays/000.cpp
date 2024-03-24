#include <iostream>
using namespace std;
int main() {
    int num1, num2;
    std::cout << "hh: ";
    std::cin >> num1;
    std::cout << "jj: ";
    std::cin >> num2;

    int sum = num1 + num2;
    int difference = num1 - num2;
    int product = num1 * num2;
    double quotient = static_cast<double>(num1) / num2; // 使用 static_cast<double> 避免整数除法

    std::cout << "hh: " << sum << std::endl;
    std::cout << "hh: " << difference << std::endl;
    std::cout << "hh: " << product << std::endl;
    std::cout << "hh: " << quotient << std::endl;

    return 0;
}