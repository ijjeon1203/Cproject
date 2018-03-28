#include "data.h"
#include "common.h"
#include "screenout.h"

extern int totalmoney;
extern moneydata money;

void showmenu()
{
	printf("-------------------------------------------\n");
	printf("사용자모드\n");
	printf("-------------------------------------------\n");
	printf("현재금액 %d\n", totalmoney);
	printf("-------------------------------------------\n");
	printf("1. 동전 투입\n");
	printf("2. 거스름돈반환\n");
	printf("5. 종료\n");
	printf("-------------------------------------------\n");

}


