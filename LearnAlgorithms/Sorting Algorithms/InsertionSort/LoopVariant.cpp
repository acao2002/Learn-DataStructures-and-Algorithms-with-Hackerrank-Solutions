//include a loop variant to check the condition 


#include<iostream>
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include <assert.h>

bool isSroted(int arr[], int index) {
    for (int i = 0; i < index; i++) {
        if (arr[i] > arr[i + 1]) {
            return false;
        }
    }
    return true;
}

void insertionSort(int N, int arr[]) {
    int i,j;
    int value;
    for(i=1;i<N;i++)
    {
        value=arr[i];
        j=i-1;
        while(j>=0 && value<arr[j])
        {
            arr[j+1]=arr[j];
            j=j-1;
        }
        arr[j+1]=value;
        if (!isSroted(arr, i - 1))
        {
            printf("Sorting failed at index: %d", i - 1);
            printf("\n");
            for(j=0;j<N;j++)
            {
                printf("%d",arr[j]);
                printf(" ");
            }
            printf("\n");
        }
    }
    for(j=0;j<N;j++)
    {
        printf("%d",arr[j]);
        printf(" ");
    }
    printf("\n");
}
