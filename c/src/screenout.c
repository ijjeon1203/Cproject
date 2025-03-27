#include "data.h"
#include "common.h"
#include "screenout.h"

extern int totalmoney;
extern moneydata money;

void menuDisplay()
{
	printf("-------------------------------------------\n");
	printf("����ڸ��\n");
	printf("-------------------------------------------\n");
	printf("����ݾ� %d\n", totalmoney);
	printf("-------------------------------------------\n");
	printf("1. ���� ����\n");
	printf("2. �Ž�������ȯ\n");
	printf("5. ����\n");
	printf("-------------------------------------------\n");
}

void refundDisplay()
{
	printf("반환\n");
	printf("거스름돈은 %d원입니다.\n", totalmoney);
	totalmoney = 0;
	getchar();
	getchar();
}

void choiceDisplay()
{
	puts("무엇을 하시겠습니까?");
}

void endDisplay()
{
	printf("감사합니다.\n안녕히 가십시오.\n");
}