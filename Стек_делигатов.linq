<Query Kind="Statements" />


string Finct1(string arg) =>$"F1 {arg}";
string Finct2(string arg) =>$"F2 {arg}";



myMethodDelegate operation1 = Finct1;      // делегат указывает на метод Finct1
myMethodDelegate operation2 = Finct2;      // делегат указывает на метод Finct1
var act = new Stack<myMethodDelegate>();
act.Push(operation1);
act.Push(operation2);

myMethodDelegate headPerson = act.Peek();
string s1=headPerson("aaa");
s1.Dump();
act.Dump();

delegate string myMethodDelegate( string myInt );