#include <iostream>
#include <string>
using namespace std;
struct Node
{
 string label;
 int child_count;
 struct Node *child[10];
};
class BookTree
{
public:
 Node *root;
 BookTree()
 {
 root = NULL;
 }
 void create_tree();
 void display(Node *r1);
};
void BookTree::create_tree()
{
 int num_chapters, num_sections;
 root = new Node;
 cout << "Enter name of the book: ";
 cin.ignore();
 getline(cin, root->label);
 cout << "Enter number of chapters in the book: ";
 cin >> num_chapters;
 root->child_count = num_chapters;
 for (int i = 0; i < num_chapters; i++)
 {
 root->child[i] = new Node;
 cout << "Enter the name of Chapter " << i + 1 << ": ";
 cin.ignore();
 getline(cin, root->child[i]->label);
 cout << "Enter number of sections in Chapter " << root->child[i]->label
<< ": ";
 cin >> num_sections;
 root->child[i]->child_count = num_sections;
 for (int j = 0; j < num_sections; j++)
 {
 root->child[i]->child[j] = new Node;
 cout << "Enter Name of Section " << j + 1 << ": ";
 cin.ignore();
 getline(cin, root->child[i]->child[j]->label);
 }
 }
}
void BookTree::display(Node *r1)
{
 if (r1 == NULL)
 {
 cout << "No book data available. Please create a book first.\n";
 return;
 }
 cout << "\n----- Book Hierarchy -----";
 cout << "\nBook Title: " << r1->label;
 for (int i = 0; i < r1->child_count; i++)
 {
 cout << "\n\nChapter " << i + 1 << ": " << r1->child[i]->label;
 cout << "\nSections:";
 for (int j = 0; j < r1->child[i]->child_count; j++)
 {
 cout << "\n - " << r1->child[i]->child[j]->label;
 }
 }
 cout << endl;
}
int main()
{
 int choice;
 BookTree book;
 while (true)
 {
 cout << "\n-----------------" << endl;
 cout << "Book Tree Creation" << endl;
 cout << "-----------------" << endl;
 cout << "1. Create Book Tree" << endl;
 cout << "2. Display Book Tree" << endl;
 cout << "3. Quit" << endl;
 cout << "Enter your choice: ";
 cin >> choice;
 switch (choice)
 {
 case 1:
 book.create_tree();
 break;
 case 2:
 book.display(book.root);
 break;
 case 3:
 cout << "Thanks for using this program!" << endl;
 return 0;
 default:
 cout << "Invalid choice! Please try again." << endl;
 }
 }
Return 0;
}
