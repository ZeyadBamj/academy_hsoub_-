let people = [
    { name: "Ahmed Salem", age: 33, salary: 3000 },
    { name: "Mohammed Ali", age: 35, salary: 3200 },
    { name: "Fatema Majeed", age: 42, salary: 4200 },
    { name: "Duha Hussien", age: 34, salary: 3900 },
    { name: "Reda Ahmed", age: 23, salary: 5000 },
];
function averageAge() {
    let averageAge = 0;
    for (const p of people) {
        averageAge += p.age;
    }
    return averageAge
}
function totalSalary() {
    let totalSalary = 0;
    for (const p of people) {
        totalSalary += p.salary
    }
    return totalSalary
}
// for (const p of people) {
//     averageAge += p.age;
//     totalSalary += p.salary
// }

// averageAge = averageAge / people.length;
// let averageSalary = totalSalary / people.length;
averageAge = averageAge() / people.length;
let averageSalary = totalSalary() / people.length;
console.log(averageAge);
console.log(averageSalary);