#include<bits/stdc++.h>
using namespace std;

void pattern01(int n) {
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      cout << "* ";
    }
    cout << endl;
    }
}
void pattern02(int n) {
  for (int i = 1; i <= n; i++) {
    for (int j = 1; j <= i; j++) {
      cout << "* ";
    }
    cout << endl;
    }
}
void pattern03(int n) {
  for (int i = 1; i <= n; i++) {
    for (int j = 1; j <= i; j++) {
      cout << j << " ";
    }
    cout << endl;
  }
}
void pattern04(int n) {
  for (int i = n; i > 0; i--) {
    for (int j = i; j > 0; j--) {
      cout << "* ";
    }
    cout << endl;
  }
}

int main() {
  int n;
  cin >> n;
  pattern04(n);
}