<Query Kind="Statements">
  <Namespace>System.Collections.ObjectModel</Namespace>
</Query>

using System.Collections.ObjectModel;

ObservableCollection<string> collection =new ObservableCollection<string>();
collection.Add("\r\n");
collection.Add(" ");
collection.Add("ААА");
collection.Add("ААА");
collection.Add("БББ");
collection.Add("ВВВ");

			
string delimited = @"\w(.+)";
collection.Dump();
collection.Distinct().Where(c=>Regex.IsMatch(c, delimited)).Dump();

string[] arr=collection.ToArray();
arr.Dump();
arr=arr.Distinct().Where(c=>Regex.IsMatch(c, delimited)).ToArray().Dump();

string spliter="#@#";
string str=string.Join(spliter,arr);
str.Dump();
