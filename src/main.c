#include "common.h"


int main()
{
	int choice;
	while (1)
	{
		system("cls");
		showmenu();
		puts("������ �Ͻðڽ��ϱ�?");
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
			printf("�����մϴ�.\n�ȳ��� ���ʽÿ�.\n");
			break;
		}
	}

	return 0;
}
