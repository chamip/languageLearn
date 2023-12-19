#include <stdio.h>
#include <setjmp.h>

jmp_buf jump_buffer;

// 定义一个用于处理 longjmp 的 handler 函数
void error_handler() {
    printf("Error handled. Exiting program.\n");
    // 这里可以执行一些清理工作，然后退出程序
    exit(1);
}

void foo() {
    printf("Inside foo()\n");
    longjmp(jump_buffer, 1); // 跳转回 setjmp 处，并且带有返回值 1
}

int main() {
    // 设置 longjmp 的 handler 函数
    if (setjmp(jump_buffer) == 0) {
        printf("setjmp() returned 0\n");
        // 在这里调用 foo()，它会触发 longjmp
        foo();
    } else {
        // 当 longjmp 被调用时，执行这里的代码
        printf("Returned from longjmp()\n");
    }

    return 0;
}
