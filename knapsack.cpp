#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct Item {
    int cost, value;
    double ratio;
};

bool compare(Item a, Item b) {
    return a.ratio > b.ratio;
}

int main() {
    int n, budget;
    cin >> n;

    vector<Item> items(n);

    for (int i = 0; i < n; i++) {
        cin >> items[i].cost >> items[i].value;
        items[i].ratio = (double)items[i].value / items[i].cost;
    }

    cin >> budget;

    sort(items.begin(), items.end(), compare);

    double totalValue = 0.0;

    for (int i = 0; i < n; i++) {
        if (budget >= items[i].cost) {
            totalValue += items[i].value;
            budget -= items[i].cost;
        } else {
            totalValue += items[i].ratio * budget;
            break;
        }
    }

    cout << totalValue;
    return 0;
}