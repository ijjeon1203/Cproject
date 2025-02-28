#include "common.h"


int main()
{
	int choice;
	while (1)
	{
		system("cls");
		showmenu();
		puts("무엇을 하시겠습니까?");
		scanf("%d", &choice);
		
		switch (choice)
		{
		case 1:
			cashput();
			break;
		case 2:
			refund();
			break;


		}

		if (choice == 5)
		{
			printf("감사합니다.\n안녕히 가십시오.\n");
			break;
		}
	}

	return 0;
}
