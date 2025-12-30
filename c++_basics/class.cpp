#include <iostream>
#include <string>
using namespace std;

class customer{
    public:
        int age;
        double amount;
        string name;
        void output(){
            cout<< name<<endl;
        }
   
};

int main(){
    customer cus1;
    cus1.name = "Taylor";
    cus1.output();


    return 0;
}