#include "data.h"
#include "common.h"
#include "screenout.h"

extern int totalmoney;
extern moneydata money;

void refundDisplay()
{
	printf("��ȯ\n");
	printf("�Ž������� %d���Դϴ�.\n", totalmoney);
	totalmoney = 0;
	getchar();
	getchar();
}

void choiceDisplay()
{
	puts("������ �Ͻðڽ��ϱ�?");
}

void endDisplay()
{
	printf("�����մϴ�.\n�ȳ��� ���ʽÿ�.\n");
}