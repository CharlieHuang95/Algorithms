#include "stdafx.h"

#include <stdlib.h>


struct Node {
	struct Node* left;
	struct Node* right;
	int val;
};

struct Node* root;

void set_root(int data) {
	struct Node* new_node = (struct Node*)malloc(sizeof(struct Node));
	new_node->left = NULL;
	new_node->right = NULL;
	new_node->val = data;
	root = new_node;
}

void add_left_child(struct Node* node, int data) {
	struct Node* new_left = (struct Node*)malloc(sizeof(struct Node));
	new_left->left = NULL;
	new_left->right = NULL;
	new_left->val = data;
	node->left = new_left;
}

void add_right_child(struct Node* node, int data) {
	struct Node* new_right = (struct Node*)malloc(sizeof(struct Node));
	new_right->left = NULL;
	new_right->right = NULL;
	new_right->val = data;
	node->right = new_right;
}

void print_binary_tree(struct Node* node) {
	if (node == NULL) {
		return;
	}
	printf("%d", node->val);
	print_binary_tree(node->left);
	print_binary_tree(node->right);
}

int main()
{
	set_root(0);
	add_left_child(root, 1);
	add_right_child(root, 2);
	print_binary_tree(root);
	while (true) {}
    return 0;
}

