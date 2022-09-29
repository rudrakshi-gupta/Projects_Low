// #include<stdio.h>
// #include<stdlib.h>
// #include<string.h>
// #include<conio.h>
// void choice();
// void quit();
// void help();
// void menu();
// void main()
// //char menu_choice;
// {
//     char name[50];
//     printf("\n\t\t\t\t\t*************************\n");
//     printf("\n\t\t\t\t\t\tCERVEAU - A QUIZ GAME\n");
//     printf("\n\t\t\t\t\t*************************\n");
//     printf("\n\n\t\t\t\t     Enter your name:\t");
//     scanf("%s",name);
//     menu();
//     choice();
// }
// void choice()
// {
//     int c;
//     printf("\n\n\t\t\t\t     Enter your choice:\t");
//     scanf("%d",&c);
//     switch(c)
//     {
//         case 1:
//             printf("\n\n\n\n\t\t------------------------------- LET'S BEGIN -----------------------------\n");
//             //start();
//             break;
//         case 2:
//             //highest_score();
//             break;
//         case 3:
//             //reset();
//             break;
//         case 4:
//         {
//             help();
//             menu();
//             choice();
//             break;
//         }
//         case 0:
//             quit();
//             break;
//         default:
//             printf("\t\t\t\t    You entered wrong choice!\n\t\t\t\t    Enter your choice again!");
//             choice();
//             break;
//     }
// }
// void quit()
// {
//     printf("\n\n\n\t\t\t\t\t         You Quit!");
//     printf("\n\t\t---------------------------------- EXIT ----------------------------------\n");
// }
// void help()
// {
//     printf("\n\n\n\t\t-------------------------------------------------------------------------\n");
//     printf("\t\t\t\t\t      Instructions");
//     printf("\n\t\t-------------------------------------------------------------------------\n");
//     printf("\n\t\t\t\t*This is a simple quiz game.\n\t\t\t\t*This game contains 15 levels.\n\t\t\t\t*Each level contains 5 questions of MCQ type.\n\t\t\t\t*Each question carries 5 points\n\t\t\t\t*Please answer only in A,B,C or D.");
//     printf("\n\n\t\t-------------------------------------------------------------------------\n");
// }
// void menu()
// {
//     printf("\n\n\t\t\t\t*Press 1 to start the game.\n\t\t\t\t*Press 2 to view highest score.\n\t\t\t\t*Press 3 to reset.\n\t\t\t\t*Press 4 to help.\n\t\t\t\t*Press 0 to quit.");
// }
// #include <stdio.h>
// #include <string.h>
// int main()
// {
//     char destination[] = "Hello ";
//     char source[] = "World!";
//     strcat(destination,source);
//     printf("Concatenated String: %s\n", destination);
//     return 0;
// }
// #include<stdio.h> 

// int main()
// {
//     int n=5,m=1;
//     for(int i=n;i>=1;i--)  
//     {  
//         printf("\t\t\t");
//        for(int j=1;j<m;j++)  
//        {  
//            printf(" ");  
//        }  
//        for(int k=1;k<=2*i-1;k++)  
//        {  
//            printf("*");  
//        }  
//        m++;  
    
//       printf("\n");  
//     }
//     m=n;  
//     for(int i=1;i<=n;i++)  
//     {  
//         printf("\t\t\t");
//        for(int j=1;j<=m-1;j++)  
//        {  
//             printf(" ");  
//        }  
//        for(int k=1;k<=2*i-1;k++)  
//        {  
//             printf("*");  
//        }  
//        m--;  
     
//       printf("\n");  
//     }  
//     printf("\t\t**************************\n");
//     return 0;
// }
#include<stdio.h> 

int main()
{
    int year=2016;
    int a=((year-1)*365+(((year-1)/4)-((year-1)/100)+((year-1)/400)+1)) % 7;
    printf("%d",a);
    return 0;
}