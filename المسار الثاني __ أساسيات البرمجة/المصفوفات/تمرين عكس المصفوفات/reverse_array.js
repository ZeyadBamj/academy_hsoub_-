let num = [1, 2, 3, 4, 5, 7];

let reNum = [...num].reverse();

console.log(reNum);

function reverse(arr) {
  let temp = [];
  for (let a in arr) {
    temp.unshift(arr[a]);
  }
  return temp;
}
console.log(reverse(num));

function spliceReverse(arr) {
  for (let i in arr) {
    arr.splice(i, 0, arr.pop());
  }
  return arr;
}
console.log(spliceReverse(num));
