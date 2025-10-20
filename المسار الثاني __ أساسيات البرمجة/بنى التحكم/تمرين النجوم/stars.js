// make a dimoned with stars

let row = parseInt(prompt('Enter a Number'));
for (let i = 1; i <= row; i++) {
    let upStars = '';
    for (let j = 1; j <= row - i; j++) {
        upStars += ' '; 
    }
    for (let uS = 1; uS <= (2 * i - 1); uS++) {
        upStars += '*'; 
    }
    console.log(upStars); 
}

for (let i = row - 1; i >= 1; i--) {
    let downStars = '';
    for (let j = 1; j <= row - i; j++) {
        downStars += ' ';
    }
    for (let dS = 1; dS <= (2 * i - 1); dS++) {
        downStars += '*';
    }
    console.log(downStars);
}