<Query Kind="Statements" />



string Finct1(string arg) =>$"F1 {arg}";
string Finct2(string arg) =>$"F2 {arg}";



myMethodDelegate operation1 = Finct1;      // делегат указывает на метод Finct1
myMethodDelegate operation2 = Finct2;      // делегат указывает на метод Finct1
var act = new Queue<myMethodDelegate>();
act.Enqueue(operation1);
act.Enqueue(operation2);
act.Dump();
var a1=act.Dequeue();
a1.Dump();
act.Dump();

delegate string myMethodDelegate( string myInt );