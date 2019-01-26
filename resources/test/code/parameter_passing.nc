void main(void) {
    int a[10];
    int second(int a[]) {
        return a[1];
    }
    a[1] = 526;
    output(second(a));
}