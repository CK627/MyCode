#define _CRT_SECURE_NO_WARNINGS 1

#include <stdio.h>



int main()
{
	//Ϊ�����ı�ʶ��
	//����extern�ⲿ���ŵ�
	extern int a;
	printf("a=%d\n", a);
	return 0;
} 



//int a = 2020;
//
//void test()//�Զ��庯��
//{
//	printf("test()--%d\n", a);
//}
//int main() 
//{
//	test();
//	printf("%d\n", a);
//	return 0;
//}



//int main()
//{
//	//�ֲ�������������
//	int a = 0;
//	{
//		printf("a=%d\n", a);
//	}
//	
//	return 0;
//}



//int a = 0;
//int main()
//{
//	int a = 10;
//	// �ֲ�������ȫ�ֱ��������ֽ��鲻Ҫ��ͬ-������ᣬ����bug
//	// ���ֲ�������ȫ�ֱ�����������ͬ��ʱ�򣬾ֲ���������
//	printf("%d\n", a);
//	return 0;
//}



//int num2 = 20;// ȫ�ֱ��� - �����ڴ���飨{}��֮��ı���
//
//int main()
//{
//	int unm1 = 10;// �ֲ����� - �����ڴ���飨{}���ڲ�
//
//	return 0;
//}



//int main()
//{
//	// ����
//	// 20
//	//short age = 20;// ���ڴ�����2���ֽ�= 16bit���������20
//	//float weight = 95.6f;// ���ڴ�����4�����С��
//	return 0;
//}