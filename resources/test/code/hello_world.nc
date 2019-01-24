void main(void) {
    int a[6];
    a[0] = 5;
    a[1] = 2;
    a[2] = 4;
    a[3] = 3;
    a[4] = 1;
    a[5] = 0;
    while (i < 10){
        int tmp;
        tmp = a[a[i]];
        a[a[i]] = a[i];
        a[i] = tmp;
        i = i+1;
    }
    i = 0;
    while (i < 10){
        output(a[i]);
    }
}
