#include "stdafx.h"
#include <stdlib.h>
#include <iostream>

class Node {
private:
	int data;
	Node* left_child;
	Node* right_child;
public:
	Node(data): data(data), left_child(NULL), right_child(NULL) {}
};

class BinaryTree {
private:
	Node* root;
public:
	BinaryTree() {
		root = new Node(0);
	}
	
};