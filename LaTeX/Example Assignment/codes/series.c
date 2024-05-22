#include<stdio.h>

int main(){
    FILE *ptr=fopen("series.dat", "w"); //opening the file to store values
    int x_0=-32, d=7; //Giving the parameters of the sequence
    
    //printing the terms of the sequence
    for(int i=0; i<32; i++) fprintf(ptr, "%d ", (x_0+7*i)); 
    
    //last term outseide the for loop to avoid space at EOF.
    fprintf(ptr, "%d", x_0+7*32);

    return 0;
}