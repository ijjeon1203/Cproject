#include "common.h"
#include "data.h"
#include "screenout.h"


int totalmoney;
moneydata money;



void cashput()
{
	int won, count;
	printf("��¥�� ������ �����ðڽ��ϱ�?\n");
	printf("1.10�� 2. 50�� 3.100�� 4. 500��\n");
	scanf("%d", &won);
	printf("��������ðڽ��ϱ�?");
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

void refund()
{
	printf("��ȯ\n");
	printf("�Ž������� %d���Դϴ�.\n", totalmoney);
	totalmoney = 0;
	getchar();
	getchar();
}
