const data = [5, false, 'welcome', 4, true, 'hi'];

for (let i = 0; i < data.length; i++){
    if (typeof data[i] === 'string') {
        console.log(data[i]);
    }
}