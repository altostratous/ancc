void main(void) {
    void dualprint(int a, int b) {
        output(a);
        return;
        output(b);
    }
    int girl(void) {
        return 52;
    }
    int four(int a, int b, int c, int d) {
        output(a);
        output(b);
        output(c);
        output(d);
    }
    int a;
    dualprint(1, 2);
    dualprint(2, 1);
    a = girl();
    dualprint(girl(), 1);
    four(1, 2, 3, 4);
}