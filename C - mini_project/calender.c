#include<stdio.h> 

int daycode(int year)
{
    int a=((year-1)*365+(((year-1)/4)-((year-1)/100)+((year-1)/400)+1)) % 7;
    return a;
}

int main()
{
    int year,week=0;
    printf("\nEnter the year : ");
    scanf("%d",&year);
    printf("\n\t\t\t\t---YEAR CALENDER OF %d---\n",year);
    int monthday[]={31,28,31,30,31,30,31,31,30,31,30,31};
    char* monthname[]={"January","February","March","April","May","June","July","August","September","October","November","December"};
    if ((year%4==0 && year%100!=0) || year%400==0)
    {
        monthday[1]=29;
    }
    int month_first=daycode(year);
    for (int i = 0; i < 12; i++)
    {
        printf("\n\t\t%s\n",monthname[i]);
        printf("  Sun   Mon  Tues  Wed  Thr  Fri  Sat\n");
        for ( week = 0; week < month_first; week++)//mf=3 tha to ab 3 space dega phir 1 se start hoga//till when the daycode no comes till then print 5 spaces
        {
            printf("     ");//2016
        }
        for (int j = 1; j <=monthday[i]; j++)
        {
            printf("%5d",j);//1//2
            ++week;//6//7//it was at week = week ++ only that's why after the previous m in the 2nd it starts from there and when 6 completes \n
            if (week>6)
            {
                printf("\n");
                week=0;
            }
            month_first=week;//mf=6//mf=0//end of month=week jitna par khatam hua let's say 3, loop wapas chalega jisme month 1st 3 hai//assining the next month_first to be of that much spaces in week or elses in next months it will start with mon itself
        }
        printf("\n");
        
    }
    
    // printf("%d",daycode(2018));
    return 0;
}