// -*- coding = utf-8 -*-
// @Time:2023/7/17 21:33
// @Author:CK
// @File:Constants_and_Variables
// @Software:CLion

//#define _CRT_SECURE_NO_WARNINGS 1

#include <stdio.h>



int main()
{
    //为声明的标识符
    //声明extern外部符号的
    extern int a;
    printf("a=%d\n", a);
    return 0;
}



//int a = 2020;
//
//void test()//自定义函数
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
//	//局部变量的作用域
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
//	// 局部变量和全局变量的名字建议不要相同-容易误会，产生bug
//	// 当局部变量和全局变量的名字相同的时候，局部变量优先
//	printf("%d\n", a);
//	return 0;
//}



//int num2 = 20;// 全局变量 - 定义在代码块（{}）之外的变量
//
//int main()
//{
//	int unm1 = 10;// 局部变量 - 定义在代码块（{}）内部
//
//	return 0;
//}



//int main()
//{
//	// 年龄
//	// 20
//	//short age = 20;// 向内存申请2个字节= 16bit，用来存放20
//	//float weight = 95.6f;// 向内存申请4，存放小数
//	return 0;
//}