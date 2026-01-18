/*  This program will calculate the total score of series games, by entering -1 data entering would be finished. */

#include <iostream>
using namespace std;

int main()
{
  int game = 1;
  int score;
  int total;
  
  cout<<"Enter the number of points for game "<<game<<" : ";
  cin>>score;
  
  while (score != -1){
      total += score;
      game++;   
      cout<<"Enter the number of points for game "<<game<<" : ";
      cin>>score;
  }
    cout<<"\n The total would be: "<<total<<" points."<<endl;
    return 0;
}
