#include <iostream>
using namespace std;

int main() {
  int x = 5;
  int y = 3;
  cout << (!(x < 3 && x > 10)); // returns true (1) because ! (not) is used to reverse the result
  return 0;
}

