int d;
int function3(void){
    int c;
    c = 0;
    switch(d){
        case 1:
            c = d;
            break;
        case 2:
            c = d - 2;
            break;
        case 3:
            c = c + 1;
            break;
        default:
            c = 9;
    }
    return c;
}