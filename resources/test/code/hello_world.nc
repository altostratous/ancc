void main(void) {
    int a[10];
    int i;
    i = 1;
    a[0] = 0;
    while (i < 10){
        a[i] = a[i-1] + i * i;
        i = i+1;
    }
    output(a[9]);
}
