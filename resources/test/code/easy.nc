int var1;
int function1(int a){
    var1 = 4;
    var1 = 2;
    function1(function1(), var1);
    return 1;
}