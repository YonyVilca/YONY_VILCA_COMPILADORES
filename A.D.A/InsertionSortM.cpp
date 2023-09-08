#include <iostream>
using namespace std;
void insertion_sort(int A[], int n) {
  for (int j = 2; j < n; j++) {
    int key = A[j];
    int i = j - 1;
    while (i > 0 && A[i] > key) {
      A[i + 1] = A[i];
      i = i - 1;
    }
  }
}
int main() {
  int A[] = {1, 2, 3, 4, 5};
  int n = sizeof(A) / sizeof(A[0]);
  insertion_sort(A, n);
  for (int i = 0; i < n; i++) {
    cout << A[i] << " ";
  }
  cout << endl;
  return 0;
}
