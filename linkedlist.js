class Node {
  constructor(data) {
      this.data = data;
      this.next = null;
  }
}

// Appends a new node at the end 
// and returns the head.
function append(head, newData) {

  // Create a new node
  const newNode = new Node(newData);

  // If the Linked List is empty,
  // make the new node as the head
  if (head === null) {
      return newNode;
  }

  // Store the head reference in a 
  // temporary variable
  let last = head;

  // Traverse till the last node
  while (last.next !== null) {
      last = last.next;
  }

  // Change the next pointer of the 
  // last node to point to the new node
  last.next = newNode;

  // Return the head of the list
  return head;
}

// Prints the contents of the linked
// list starting from the head
function printList(node) {
  while (node !== null) {
      console.log(node.data + " ");
      node = node.next;
  }
}

// Create a hard-coded linked list:
// 2 -> 3 -> 4 -> 5 -> 6
let head = new Node(2);
head.next = new Node(3);
head.next.next = new Node(4);
head.next.next.next = new Node(5);
head.next.next.next.next = new Node(6);

console.log("Created Linked list is:");
printList(head);

// Example of appending a node 
// at the end
head = append(head, 1);

console.log("\nAfter inserting 1 at the end:");
printList(head);
