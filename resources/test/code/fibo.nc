void main(void) {
    int a;
    int b;
    a = b = 1;
    while(a < 10) {
        int temp;
        output(a);
        temp = a;
        a = b;
        b = temp + a;
    }
}
