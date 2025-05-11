#include <iostream>
#include <string>
using namespace std;

int main() {
    string words;
    cin >> words;
    int len = words.length();

    words[1] = 'a';
    words[len-2] = 'a';

    cout << words;

    return 0;
}