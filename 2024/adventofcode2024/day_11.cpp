#include<stdio.h>
#include<iostream>
#include<vector>
#include<string>
#include <bits/stdc++.h>

using namespace std;
int main() {
	
	string line;
	cin >> line;
	
	vector<long long> nums;
	stringstream check1(line);
	string inter;

	while (getline(check1, inter, ' '))
		nums.push_back(stoll(inter));
	
	cout << nums[0] << ", " << nums[1] << endl;
	int cycles = 25;

	
}
