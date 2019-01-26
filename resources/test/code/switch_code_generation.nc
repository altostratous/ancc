void main(void) {
    switch(2) {
        case 1:
            output(1);
        case 2:
            output(2);
        case 3:
            output(3);
    }
    switch(3) {
        case 1:
            output(1);
        case 2:
            output(2);
        case 3:
            output(3);
        default:
            output(0);
    }

    switch(5) {
        case 1:
            output(1);
        case 2:
            output(2);
        case 3:
            output(3);
        default:
            output(0);
    }

    switch(2) {
        case 1:
            output(1);
        case 2:
            output(2);
            break;
        case 3:
            output(3);
        default:
            output(0);
    }

    if (1) {
        int main;
        main = 0;
        while (main < 10) {
            output(main);
            main = main + 1;
        }
    } else ;
}