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
	void append_to_head(int data) {
		Node* new_node = new Node(data);
		new_node->set_next(head);
		head = new_node;
	}
	void reverse() {
		Node* cur = head;
		Node* prev = NULL;
		while (cur != NULL) {
			Node* temp = cur->get_next();
			cur->set_next(prev);
			prev = cur;
			cur = temp;
		}
		head = prev;
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
	ll.append_to_tail(2);
	ll.append_to_tail(3);
	ll.append_to_head(-1);
	ll.print();
	ll.reverse();
	ll.print();

    return 0;
}

