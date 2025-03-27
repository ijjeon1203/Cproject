#include "common.h"
#include "data.h"
#include "screenout.h"


int totalmoney;
moneydata money;



void cashput()
{
	int won, count;
	printf("얼마짜리 동전을 넣으시겠습니까?\n");
	printf("1.10원 2. 50원 3.100원 4. 500원\n");
	scanf("%d", &won);
	printf("몇개를넣으시겠습니까?");
	+
		scanf("%d", &count);

	if (won == 1)
	{
		money.ten = count;
		totalmoney += 10 * count;
	}
	else if (won == 2)
	{
		money.fifty = count;
		totalmoney += 50 * count;
	}
	else if (won == 3)
	{
		money.hund = count;
		totalmoney += 100 * count;
	}
	else if (won == 4)
	{
		money.fhund = count;
		totalmoney += 500 * count;
	}
	if (won == 5)
	{
		printf("bye\n");
	}
	getchar();
}
