#include <unordered_set>
#include<vector>
#include<stdio.h>
#include<iostream>
#include<string>
#include<unordered_map>
#include<utility>

using namespace std;
int main() {
	vector<vector<char>> mat;
	string line;

	int i = 0;
	while (getline(cin, line)){
		mat.push_back(vector<char>());
		for (char c: line){
			mat[i].push_back(c);
		}
		i++;
	}
	int r = mat.size();
	int c = mat[0].size();
	unordered_map<char, vector<pair<int, int>>> locs;
	unordered_set<char> nodes;

	for (int i = 0; i < r; i ++){
		for (int j = 0; j < c; j ++) {
			if (mat[i][j] != '.') {
				if (locs.find(mat[i][j]) == locs.end()) {
					locs[mat[i][j]] = vector<pair<int, int>>(); 
					nodes.insert(mat[i][j]);
				}
				locs.at(mat[i][j]).push_back(make_pair(i, j));
			}
		}
	}

	vector<pair<int, int>> anodes;

	for (char t: nodes) {
		vector<pair<int, int>>
		for (int i = 0; i < )

		for (pair<int, int>& p: locs.at(t)) {	
			for (pair<int, int>& q: locs.at(t)) {
				int dx = p.first - q.first;
				int dy = p.second - q.second;

				
			}
		}
	}
	


}
