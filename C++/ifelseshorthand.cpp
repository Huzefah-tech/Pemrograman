#include <iostream>
#include <string>
using namespace std;

int main() {
	int time = 20;
	string result = (time < 18) ? "Good day." : "Good Evening.";
	cout << result;
	return 0;
}
