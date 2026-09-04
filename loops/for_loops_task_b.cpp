#include <iostream>
using namespace std;

int timesTable = 1;

int main() {
  cout << "Enter times table.\n> ";
  cin >> timesTable;

  for (int i = 1; i < 13; i++) {
    cout << i << " times " << timesTable << " is " << timesTable*i << endl;
  }
}
