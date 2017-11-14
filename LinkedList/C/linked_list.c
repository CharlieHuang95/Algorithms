#include "stdafx.h"
#include <stdlib.h>
#include <stdio.h>

struct Node {
	struct Node* next;
	int data;
};

void append_to_tail(struct Node* head, int data) {
	if (head == NULL) {
		return;
	}
	struct Node* cur = head;
	while (cur->next != NULL) {
		cur = cur->next;
	}
	struct Node* new_node = (struct Node*) malloc(sizeof(struct Node));
	new_node->next = NULL;
	new_node->data = data;
	cur->next = new_node;
}

struct Node* append_to_head(struct Node* head, int data) {
	struct Node* new_node = (struct Node*) malloc(sizeof(struct Node));
	new_node->next = head;
	new_node->data = data;
	return new_node;
}

void print_linked_list(struct Node* head) {
	struct Node* cur = head;
	while (cur != NULL) {
		printf("%d->", cur->data);
		cur = cur->next;
	}
}

void free_linked_list(struct Node* head) {
	struct Node* cur = head;
	struct Node* temp;
	while (cur != NULL) {
		temp = cur->next;
		free(cur);
		cur = temp;
	}
}

struct Node* reverse_linked_list(struct Node* head) {
	struct Node* cur = head;
	struct Node* prev = NULL;
	struct Node* temp;
	while (cur != NULL) {
		temp = cur->next;
		cur->next = prev;
		prev = cur;
		cur = temp;
	}
	return prev;
}

int test_linked_list()
{
	struct Node* head = (struct Node*) malloc(sizeof(struct Node));
	head->next = NULL;
	head->data = 0;
	append_to_tail(head, 1);
	append_to_tail(head, 2);
	head = append_to_head(head, 3);
	print_linked_list(head);
	head = reverse_linked_list(head);
	print_linked_list(head);
	free_linked_list(head);
    return 0;
}

