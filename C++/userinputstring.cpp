#include <iostream>
#include <string>

int main() {
  std::string fullName;
  std::cout << "Type your full name: ";
  getline (cin, fullName);
  std::cout << "Your name is: " << fullName;
  return 0;
}

