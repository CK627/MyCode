#define _CRT_SECURE_NO_WARNINGS 1
//遇到一些函数会出现不安全，而报错

// 包含一个叫stdio.h的文件
// std - 标准 standard input output 
#include <stdio.h>
// int是整型的意思
// main前面的int表示main函数调用返回一个整型值
int main()// 主函数-程序的入口-main函数有且仅有一个
{
	// 这里完成任务
	// 在屏幕上输出hello world
	// 函数-print function - printf - 打印函数
	// 库函数-C语言本身提供给我们使用的函数
	// 别人的东西 - 打招呼
	// #include
	printf("Hello World\n");
	return 0;// 返回0
}
