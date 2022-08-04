<Query Kind="Statements" />

var people = new Stack<string>();
people.Push("Tom");
// people = { Tom }
people.Push("Sam");
// people = { Sam, Tom }
people.Push("Bob");
// people = { Bob, Sam, Tom }
 
// получаем первый элемент стека без его удаления 
string headPerson = people.Peek();
headPerson.Dump();  // Bob
people.Dump(); 
string person1 = people.Pop();
// people = { Sam, Tom }
person1.Dump();  // Bob
people.Dump();  
string person2 = people.Pop();
// people = { Tom }
person2.Dump();  // Sam
people.Dump();  
string person3 = people.Pop();
// people = { }
person3.Dump();  // Tom
people.Dump(); 