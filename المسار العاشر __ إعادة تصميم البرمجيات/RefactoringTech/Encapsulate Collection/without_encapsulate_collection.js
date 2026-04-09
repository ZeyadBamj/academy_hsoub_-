class Department{
    constructor(name) {
        this._name = name;
        this._employees = [];
    }

    get name() { return this._name; }
    get employees() { return this._employees; }
    set employees(list) { this._employees = list; }

}

class Employee{
    constructor(name, salary) {
        this._name = name;
        this._salary = salary;
    }
}

let hr = new Department("HR");
hr.employees.push(new Employee("Ahmed Salem", 1000));
hr.employees.push(new Employee("Saleh Ali", 750));

let newEmployee = new Employee("Jaber Maher", 300);
hr.employees.push(newEmployee);
hr.employees.push(new Employee("Rashed Saleh", 800));

console.log(hr.employees);
console.log(hr.employees.filter((employee) => {
    return employee._salary < 1000;
}));