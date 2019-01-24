void main(void) {
    int a;
    int b;
    a = 0;
    b = 0;
    while (1){
        a = a + 1;
        if (a == 5)
            continue;
        else if (a == 20)
            break;
        else
            output(a);
    }
}
