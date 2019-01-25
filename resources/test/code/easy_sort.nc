void main(void) {
    int a[6];
    int i;
    a[0] = 5;
    a[1] = 2;
    a[2] = 3;
    a[3] = 0;
    a[4] = 1;
    a[5] = 4;

    i = 0;
    while (i < 6) {
        int j;
        j = 0;
        while (j < 6) {
            if (j == i) {
                j = j + 1;
                continue;
            } else ;

            if (a[i] < a[j]) {
                int temp;
                temp = a[i];
                a[i] = a[j];
                a[j] = temp;
            } else ;

            j = j + 1;
        }
        i = i + 1;
    }

    i = 0;
    while (i < 6){
        output(a[i]);
        i = i + 1;
    }
}
