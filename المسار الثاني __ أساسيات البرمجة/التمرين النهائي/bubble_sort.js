let numbers = [2, 1, 5, 6, 10, 38, 29, 1, 6, 7, 9];
console.log(numbers);
let a = numbers.sort((a, b) => a - b);
// console.log(a);

// // Bubble sort
function bubbleSort(arr) {
  for (let i = 0; i < arr.length - 1; i++) {
    for (let j = 0; j < arr.length - 1 - i; j++) {
      if (arr[j] > arr[j + 1]) {
        // تبديل العناصر
        let temp = arr[j];
        arr[j] = arr[j + 1];
        arr[j + 1] = temp;
      }
    }
  }
  console.log(arr);
}

// bubbleSort(numbers);

// Bubble Sort with Trace
function bubbleSortTrace(arr) {
  const a = arr.slice();
  console.log("the original arr: ", a);
  for (let i = 0; i < a.length - 1; i++) {
    console.log(`\n--- المرور رقم ${i + 1} ---`);
    let swapped = false;
    for (let j = 0; j < a.length - 1 - i; j++) {
      console.log(`مقارنة ${a[j]} و ${a[j + 1]}`);

      if (a[j] > a[j + 1]) {
        console.log(`تبديل ${a[j]} <-> ${a[j + 1]}`);
        [a[j], a[j + 1]] = [a[j + 1], a[j]];
        swapped = true;
        console.log("الحالة الحالية:", a);
      }
    }
    if (!swapped) {
      console.log("✅ لا يوجد تبديلات، المصفوفة مرتبة بالفعل.");
      break;
    }
  }
  console.log("\nالنتيجة النهائية:", a);
  console.log(a);
}

// bubbleSortTrace(numbers);
// console.log(numbers);

// Selection Sort
function selectionSort(arr) {
  for (let i = 0; i < arr.length - 1; i++) {
    let minIndex = i;

    for (let j = i + 1; j < numbers.length; j++) {
      if (numbers[j] < numbers[minIndex]) {
        minIndex = j;
      }
    }
    if (minIndex !== i) {
      let temp = numbers[i];
      numbers[i] = numbers[minIndex];
      numbers[minIndex] = temp;
    }
  }
  console.log(arr);
}

// console.log(numbers);
// selectionSort(numbers);

// Quick Sort (fastest one)
function quickSort(arr) {
  if (arr.length <= 1) {
    return arr;
  }

  let pivot = arr[arr.length - 1]; // نختار اخر عنصر كمحور
  let left = [];
  let right = [];

  for (let i = 0; i < arr.length - 1; i++) {
    if (arr[i] < pivot) {
      left.push(arr[i]);
    } else {
      right.push(arr[i]);
    }
  }
  return [...quickSort(left), pivot, ...quickSort(right)];
}

console.log(quickSort(numbers));
