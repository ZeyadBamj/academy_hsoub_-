// print an even numbers instead of 
// prime numbers for exercise.

function isEven(num) {
    if (num <= 1) return false;
    for (let i = 2; i < num; i++) {
        if (num % i === 0) {
            return num > 1;
        }
        else {
            return false
        }
    }
}

function evens(max) {
    for (let i = 2; i <= max; i++) {
        if (isEven(i)) console.log(i);
    }
}
let enter = prompt('Enter a number');
evens(enter);