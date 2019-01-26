int var1;
int function1(int a){
    void function2(int b, int c){
        if (c < b)
            output(b);
        else
            output(c);
    }
    int d;
    int function3(void){
        int cd;
        cd = 0;
        switch(var1){
            case 1:
                c = 2 * a * d;
                break;
            case 2:
                c = a - 2;
                break;
            case 3:
                c = c + 1;
                break;
            default:
                c = 9;
        }
        return c;
    }
    d = 4;
    var1 = 2;
    function2(function1(), d);
    return 1;
}
int array1[5];
void main(void){
    int i;
    i = 5;
    if (function2(i) == i + 48 - var1)
       return;
    else while(i){
        array1[i = i - 1] = i;
        -37;
        output(array1[i]);
    }
}