#include<stdio.h>
#include<stdlib.h>

void start();
int question();
void trophy();
void highest_score();
void reset_hscore();
void help();
int quit();

struct game
{
    char name[50];
}game;

void options(int p)
{
    printf("\nGame options :-");
    printf("\nPress :-\n\t1---Start\n\t2---View highest score\n\t3---Help\n\t4---Reset Highest scores\n\t0---Quit\n");
    int choice;
    printf("\nEnter your choice : ");
    scanf("%d",&choice);
    switch (choice)
    {
    case 1:
        printf("\nEnter name(the playing person) : ");
        scanf("%s",game.name);
        printf("\n\t\t\t\t Let's begin!!\n");
        printf("\n\n---------------------------------------------------------------------------\n");
        start(1);
        break;
    case 2:
        highest_score();
        break;
    case 3:
        help(1);
        break;
    case 4:
        reset_hscore();
        break;
    case 0:
        quit(0);
        break;
    default:
        printf("\t\t\t\t    You entered wrong choice!\n\t\t\t\t    Enter your choice again!");
            printf("\n\n\t\t---------------------------------------------------------------------\n");
        options(1);
        break;
    }
}

void start(int data)
{
    for (int i = data; i < 11; i++)
    {
        printf("\n\t\t--- Level %d ---\n",i);
        question(i);
    }
}

int question(int level)
{
    int answer,sum=0;
    switch (level)
    {
    case 1:
        printf("What is the driver of the train called??\n");
        printf("1. Pilot\t\t2. Train Driver\n3. Captian\t\t4. Locopilot\n");
        printf("Your answer(option) : ");
        scanf("%d",&answer);
        if (answer==4)
        {
            printf("\nBINGO!! You are a genius.\n");
            sum+=5;
            printf("Earned points : %d",sum);
            printf("\nTotal score : 5\n\n");
            start(2);
        }
        else
        {
            printf("\n\n-------------------------------------------------------------------------\n");
            printf("\n\tSorry!! You are wrong..return to the beginning.\n");
            start(1);
        }
        break;
    
    case 2:
        printf("How many flavours of jelly bean exist?\n");
        printf("1. 50\t\t2. 9\n3. 65\t\t4. 43\n");
        printf("Your answer(option) : ");
        scanf("%d",&answer);
        if (answer==1)
        {
            printf("\nBINGO!! You are a genius.\n");
            sum+=5;
            printf("Earned points : %d",sum);
            printf("\nTotal score : 10\n\n");
            start(3);
        }
        else
        {
            printf("\n\n-------------------------------------------------------------------------\n");
            printf("\n\tSorry!! You are wrong..return to the beginning.\n");
            start(1);
        }
        break;
    
    case 3:
        printf("What planet are Transformers from?\n");
        printf("1. MM31\t\t\t2. Cybertron\n3. Wormir\t\t4. Qwiebt\n");
        printf("Your answer(option) : ");
        scanf("%d",&answer);
        if (answer==2)
        {
            printf("\nBINGO!! You are a genius.\n");
            sum+=5;
            printf("Earned points : %d",sum);
            printf("\nTotal score : 15\n\n");
            start(4);
        }
        else
        {
            printf("\n\n-------------------------------------------------------------------------\n");
            printf("\n\tSorry!! You are wrong..return to the beginning.\n");
            start(1);
        }
        break;
    
    case 4:
        printf("What is the person who compiles a dictonary called??\n");
        printf("1. Optencigrapher\t\t2. Burosict\n3. Lexicographer\t\t4. Director\n");
        printf("Your answer(option) : ");
        scanf("%d",&answer);
        if (answer==3)
        {
            printf("\nBINGO!! You are a genius.\n");
            sum+=5;
            printf("Earned points : %d",sum);
            printf("\nTotal score : 20\n\n");
            start(5);
        }
        else
        {
            printf("\n\n-------------------------------------------------------------------------\n");
            printf("\n\tSorry!! You are wrong..Return to the Beginning.\n");
            start(1);
        }
        break;
    
    case 5:
        printf(" CTRL, ALT and SHIFT are called _________ keys.\n");
        printf("1. Function\t\t2. Modifier\n3. Adjustment\t\t4. Alpha\n");
        printf("Your answer(option) : ");
        scanf("%d",&answer);
        if (answer==2)
        {
            printf("\nBINGO!! You are a genius.\n");
            sum+=5;
            printf("Earned points : %d",sum);
            printf("\nTotal score : 25\n\n");
            start(6);
        }
        else
        {
            printf("\n\n-------------------------------------------------------------------------\n");
            printf("\n\tSorry!! You are wrong..return to the beginning.\n");
            start(1);
        }
        break;
    
    case 6:
        printf("What is the dot in alphabet 'i' called??\n");
        printf("1. tittle\t\t2. little mittle\n3. fiffle\t\t4. miselle\n");
        printf("Your answer(option) : ");
        scanf("%d",&answer);
        if (answer==1)
        {
            printf("\nBINGO!! You are a genius.\n");
            sum+=5;
            printf("Earned points : %d",sum);
            printf("\nTotal score : 30\n\n");
            start(7);
        }
        else
        {
            printf("\n\n-------------------------------------------------------------------------\n");
            printf("\n\tSorry!! You are wrong..return to the beginning.\n");
            start(1);
        }
        break;
    
    case 7:
        printf("Before the 19th Century, the 'Living Room' was originally called the...\n");
        printf("1. Bakery\t\t2. Resting salon\n3. Mage Room\t\t4. Parlor\n");
        printf("Your answer(option) : ");
        scanf("%d",&answer);
        if (answer==4)
        {
            printf("\nBINGO!! You are a genius.\n");
            sum+=5;
            printf("Earned points : %d",sum);
            printf("\nTotal score : 40\n\n");
            start(8);
        }
        else
        {
            printf("\n\n-------------------------------------------------------------------------\n");
            printf("\n\tSorry!! You are wrong..return to the beginning.\n");
            start(1);
        }
        break;
    
    case 8:
        printf("What is the Olympic sport in which athletes cross the finish line backwards?\n");
        printf("1. Back fleet\t\t2. Rowing\n3. White run\t\t4. Milestone running\n");
        printf("Your answer(option) : ");
        scanf("%d",&answer);
        if (answer==2)
        {
            printf("\nBINGO!! You are a genius.\n");
            sum+=5;
            printf("Earned points : %d",sum);
            printf("\nTotal score : 35\n\n");
            start(9);
        }
        else
        {
            printf("\n\n-------------------------------------------------------------------------\n");
            printf("\n\tSorry!! You are wrong..return to the beginning.\n");
            start(1);
        }
        break;
    
    case 9:
        printf("In Harry Potter, where does Vernon Dursley work??\n");
        printf("1. Ministry of Magic\t\t\t\t2. Ephiltom - A constructor\n3. Grunnings - A drill manufacturer\t\t4. Gringotts Wizarding Bank\n");
        printf("Your answer(option) : ");
        scanf("%d",&answer);
        if (answer==3)
        {
            printf("\nBINGO!! You are a genius.\n");
            sum+=5;
            printf("Earned points : %d",sum);
            printf("\nTotal score : 45\n\n");
            start(10);
        }
        else
        {
            printf("\n\n-------------------------------------------------------------------------\n");
            printf("\n\tSorry!! You are wrong..return to the beginning.\n");
            start(1);
        }
        break;
    
    case 10:
        printf("What is the colour of mirror??\n");
        printf("1. Green\t\t2. White/silver\n3. No colour\t\t4. Voilet\n");
        printf("Your answer(option) : ");
        scanf("%d",&answer);
        if (answer==1)
        {
            printf("\nYou are the WINNER!!! Yahoooooo...\n");
            sum+=5;
            printf("\nEarned points : %d",sum);
            printf("\nTotal score : 50\n");
            printf("\nWinner Cup :-\n");
            trophy(5);
            FILE *fp; 
            fp=fopen("C:/Users/shamb/Desktop/Roo/ds/highest_score.txt","a+");
            fprintf(fp,"%s\t\t50\n", game.name); 
            fclose(fp);
            printf("\n\n-------------------------------------------------------------------------\n");
            options(1);
        }
        else
        {
            printf("\n\n-------------------------------------------------------------------------\n");
            printf("\n\tSorry!! You are wrong..return to the beginning.\n");
            start(1);
        }
        break;
    
    }
}

void trophy(int n)
{ 
    int m=1;
    for(int i=n;i>=1;i--)  
    {
        printf("\t\t\t");
        for(int j=1;j<m;j++)  
        {  
            printf(" ");  
        }  
        for(int k=1;k<=2*i-1;k++)  
        {  
            printf("*");  
        }  
        m++;  
     
        printf("\n");  
    }
    m=n;  
    for(int i=1;i<=n;i++)  
    {
        printf("\t\t\t");
        for(int j=1;j<=m-1;j++)  
        {  
            printf(" ");  
        }  
        for(int k=1;k<=2*i-1;k++)  
        {  
            printf("*");  
        }  
        m--;  
     
        printf("\n");  
    }  
    printf("\t\t**************************");
}

void highest_score()
{
    FILE *fp;
    printf("\n\n-------------------------------------------------------------------------\n");
    if((fp=fopen("C:/Users/shamb/Desktop/Roo/ds/highest_score.txt", "r"))==NULL)  
        {   
            printf("\n\n\t\t\tNo games played yet!\n");
            printf("\n\n-------------------------------------------------------------------------\n");
        }  
    else  
    {  
    printf("\nHighest Scores :-\n\n");  
    printf("NAME\t\tPOINTS\n");  
    while(fscanf(fp,"%s\t\t50",game.name) !=EOF)  
    {  
        printf("____________________________\n");  
        printf("%s\t\t50\n",game.name);
    }  
    printf("\n\n-------------------------------------------------------------------------\n");
  
    fclose(fp);  
    }
    options(1);

}

void reset_hscore()
{
    // fclose(fopen("C:/Users/shamb/Desktop/Roo/ds/highest_score.txt","w"));//clear content
    remove("C:/Users/shamb/Desktop/Roo/ds/highest_score.txt");
    printf("\n\t\t------Highest score has been cleared.------\n");
    printf("\n\n-------------------------------------------------------------------------\n");
    options(1);
}

void help(int y)
{
    printf("\n\n-------------------------------------------------------------------------\n");
    printf("HELP :-\n");
    printf("\n*This is a quiz game.\n*You have to pass through 10 levels.\n*Please answer only in 1,2,3 or 4.\n*Correct answers will make you the WINNER!!.\n*Correct answer --- 5 points.\n*Wrong answer---Start the Game again.\n");
    printf("\n-------------------------------------------------------------------------\n");
    options(1);
}

int quit(int e)
{
    printf("\n\t\t\tThank you for playing.....\n\t\t\tYou have QUITTED the Game.\n\n\t\t\t    Visit again!!BYE..");
    printf("\n\n---------------------------------- EXIT -----------------------------------\n");
    exit(1);
}

int main()
{
    printf("\n\t\t\t\t\t***********************\n");
    printf("\n\t\t\t\t\t CERVEAU - A QUIZ GAME\n");
    printf("\n\t\t\t\t\t***********************\n");
    printf("\n\t\t\t\t\t       WELCOME!!\n");
    char login_name;
    printf("\nLogin name : ");
    scanf("%s",&login_name);
    options(1);

    return 0;
}