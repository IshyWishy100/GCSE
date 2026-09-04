#include <iostream>
using namespace std;

string password = "oak123";
int count = 0;
string guess = "";
bool correct = false;

int main() {
  while (count < 3) {
    cout << "Enter guess.\n> ";
    cin >> guess;
    if (guess == password) {
      cout << "Correct!";
      break;
    }
    else {
      cout << "Incorrect!\n\n";
      count++;
      if (count == 3) {
        cout << "Too many incorrect attempts. Access denied!";
      }
    }
  }
}
