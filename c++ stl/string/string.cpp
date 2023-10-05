// char array is static and string is dynamic;
#include<bits/stdc++.h>
using namespace std;
int main()
{
    // declare string --> string s_name;
    string s;

    // string concanation --> string1 = string2/char + string 3/char
    s=s+'a';
    s+='b';
    string p="hello";
    string p2="hello";
    char v=' ';
    s=p+v+p2;

    // print string --> cout<<s_name
    cout<<s<<endl;

    // assign value when declare
    string s1="hello world";

    // string size --> s_name.size()
    cout<<"size and value : \n";
    cout<<s1.size()<<endl;
    cout<<s1<<endl;

    // we can traverse string as array --> s_name[index]

    // to delete the whole string --> s_name.clear()
    // to copy a string --> s1=s2
    // check if string is empty or not --> s_name.empty()

    // string iterator
    cout<<"iterator\n";
    string::iterator it;
    for ( it = s1.begin(); it != s1.end(); it++)
    {
        cout<<*it;
    }
    cout<<endl;
    cout<<"for each loop\n";
    for(auto u:s1) cout<<u;
    cout<<endl;

    // compare two string --> if(s1==s2)  else   / if(s1>s2) else 
    cout<<"compare two string\n";
    if(s1==s) cout<<"equal\n";
    else cout<<"not equal\n";

    // reverse function --> reverse(s_name.begin(),s_name.end())
    cout<<"reverse : \n";
    
    cout<<s1<<endl;
    reverse(s1.begin(),s1.end());
    cout<<s1<<endl;

    //palindrom -> first reverse then compare
    cout<<"palindrom :\n";
    s1="madam";
    string ss1=s1;
    reverse(ss1.begin(),ss1.end());
    if(s1==ss1) cout<<"palindrome\n";
    else cout<<"not palindrome\n";

    // to input a whole line --> getline(cin,s_name)
    cout<<"input a whole line : ";
    getline(cin,s1);
    cout<<s1<<endl;

    // getline problem :
    cout<<"getline problem\n";
    int t;
    cin>>t;
    while(t--)
    {
        string s;
        char c;
        cin>>c;
        getline(cin,s);
        s=c+s;
        cout<<"Case "<<t<<": "<<s<<endl;
    }

    // sorting --> sort(s.begin(),s.end()); // it will sort (increasing) according to ascii value  
    // sorting --> sort(s.rbegin(),s.rend()); // it will sort (decreasing) according to ascii value  
    // unique --> int u = unique(s.begin(),s.end())-s.begin();
    // max element --> *max_element(s.begin(),s.end())
    // min element --> *min_element(s.begin(),s.end())
    // erase a char from a string --> s.erase(s.begin()+index) 
    // erase the last char from a string --> s.erase(s.end()-1)

    // string er vector
    vector<string> i;
    i.push_back("world"); 
    i.push_back("worl"); 
    i.push_back("wor"); 
    i.push_back("war"); 

    // remove a specific char from the whole string --> s.erase(remove(s.begin(),s.end(),'char'),s.end())
    // remove a specific char from some part of the string --> s.erase(remove(s.begin(),s.end(),'char'),s.begin()+index)
    // to remove the last char of a string --> s.pop_back();
    // to access the first char of a string --> s.front();
    // to access the last char of a string --> s.back();


}