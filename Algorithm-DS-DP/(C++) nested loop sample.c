

#include <iostream>
using namespace std;

int main() {
    int numOfStd  = 5;
    int numOfTest = 4;    
    
    // Determine the average for every single student
    for(int std = 1 ; std <= numOfStd; std++){
        
        int total = 0;  // initial the accumulator
        for(int test = 1; test <= numOfTest; test++){
            
            double score;
            cout<< "Enter score of test "<< test << "for student "<< std << " : ";
            cin>> score;
            total += score;
            
        }
        
        double avg = total / numOfTest;
        cout<<" \n The average score for student "<< std << " is: "<<avg<<" scores. \n\n " ;
    }
  
    return 0;
}


/*
Enter the score of test 1 for student 1: 2                                                                                                         
Enter the score of test 2 for student 1: 36                                                                                                        
Enter the score of test 3 for student 1: 69                                                                                                        
Enter the score of test 4 for student 1: 98 

The average score for student 1 is: 51 scores.

*/
