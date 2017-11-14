#include "stdafx.h"
#include <stdlib.h>
#include <iostream>

class Node {
private:
	int data;
	Node* next;
public:
	Node(int data): data(data), next(NULL) {}
	void set_data(int data) {
		this->data = data;
	}
	void set_next(Node* next) {
		this->next = next;
	}
	int get_data() {
		return data;
	}
	Node* get_next() {
		return next;
	}
};

class LinkedList {
private:
	Node* head;
public:
	LinkedList() {
		head = new Node(0);
	}
	void append_to_tail(int data) {
		Node* cur = head;
		while (cur->get_next() != NULL) {
			cur = cur->get_next();
		}
		Node* new_node = new Node(data);
		cur->set_next(new_node);
	}
	void print() {
		Node* cur = head;
		while (cur != NULL) {
			std::cout << cur->get_data() << "->";
			cur = cur->get_next();
		}
	}
};

int test_linked_list()
{
	LinkedList ll;
	ll.append_to_tail(1);
	ll.print();

    return 0;
}

