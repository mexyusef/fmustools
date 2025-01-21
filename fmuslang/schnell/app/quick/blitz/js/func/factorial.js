
// declarative
const factorial = ( num ) =>
    num <= 1 ?
    1 :
    num * factorial( num - 1 ); 

// imperative
function factorial2( num ) {
    let result = 1;
    while ( num > 1 ) {
        result *= num;
        num -= 1;
    }
    return result;
}
