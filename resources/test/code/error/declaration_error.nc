void main(void){
    int a;
    int f(int a){
        return 3 + a;
    }
    int b;
    a[2] = 1;
    b = a[2] = 1;
    f(f);
}