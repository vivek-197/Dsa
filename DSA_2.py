class SetADT:
    def _init_(self):
        self.set_a = set([])
        self.set_b = set([])

    def add_element(self, set_name, ele):
        if set_name == 'a':
           self.set_a.add(ele)
        elif set_name == 'b':
           self.set_b.add(ele)

    def remove_element(self, set_name, ele):
        if set_name == 'a' and ele in self.set_a:
           self.set_a.remove(ele)
        elif set_name == 'b' and ele in self.set_b:
           self.set_b.remove(ele)

    def display_set(self,set_name):
        if set_name == 'a':
           for i in self.set_a:
              print(i)
                 
        elif set_name == 'b':
           for j in self.set_b:
              print(j)
                  
    def check_element(self,set_name,ele):
        if set_name == 'a':
           if ele in self_set_a:
              print("element is present")
           else:
              print("element is not present ")
        if set_name == 'b':
           if ele in self_set_b:
              print("element is present")
           else:
              print("element is not present ")

    def size_set(self):
        print("Size of Set A:", len(self.set_a))
        print("Size of Set B:", len(self.set_b))

    def union_set(self):
        print("Union:", self.set_a.union(self.set_b))

    def difference_set(self):
        print("Difference (A - B):", self.set_a.difference(self.set_b))

    def intersection_set(self):
        print("Intersection:", self.set_a.intersection(self.set_b))

    def subset_set_a(self):
        print("Is Set A a subset of Set B?", self.set_a.issubset(self.set_b))

    def subset_set_b(self):
        print("Is Set B a subset of Set A?", self.set_b.issubset(self.set_a))


def menu():
    set_adt = SetADT()
    while True:
        print("\n==== MENU ====")
        print("1. Add element to Set A")
        print("2. Add element to Set B")
        print("3. Remove element from Set A")
        print("4. Remove element from Set B")
        print("5. Display Set A")
        print("6. Display Set B")
        print("7. Display size of both sets")
        print("8. Union of Set A and Set B")
        print("9. Difference (Set A - Set B)")
        print("10. Intersection of Set A and Set B")
        print("11. check if element is present in A")
        print("12. check if element is present in b")
        print("13. Check if Set A is a subset of Set B")
        print("14. Check if Set B is a subset of Set A")
        print("15. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
           ele = int(input("Enter element to add to Set A: "))
           set_adt.add_element('a', ele)
        elif choice == 2:
           ele = int(input("Enter element to add to Set B: "))
           set_adt.add_element('b', ele)
        elif choice == 3:
           ele = int(input("Enter element to remove from Set A: "))
           set_adt.remove_element('a', ele)
        elif choice == 4:
           ele = int(input("Enter element to remove from Set B: "))
           set_adt.remove_element('b', ele)
        elif choice == 5:
           set_adt.display_set('a')
        elif choice == 6:
           set_adt.display_set('b')
        elif choice == 7:
           set_adt.size_set()
        elif choice == 8:
           set_adt.union_set()
        elif choice == 9:
           set_adt.difference_set()
        elif choice == 10:
           set_adt.intersection_set()
        elif choice == 11:
           ele = int(input("Enter element to check in Set A: ")
           set_adt.check_element('a',ele)
        elif choice == 12:
           ele = int(input("Enter element to check in Set b: ")
           set_adt.check_element('b',ele)
        elif choice == 13:
           set_adt.subset_set_a()
        elif choice == 14:
           set_adt.subset_set_b()
        elif choice == 15:
           print("Exiting program")
           break
        else:
           print("Invalid choice. Please try again.")

menu()
