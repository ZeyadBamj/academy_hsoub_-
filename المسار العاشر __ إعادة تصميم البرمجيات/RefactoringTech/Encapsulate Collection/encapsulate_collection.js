class Department{
    constructor(name) {
        this._name = name;
        this._employees = [];
    }

    get name() { return this._name; }
    get employees() { return this._employees.slice(); }

    addEmployee(employee) {
        this._employees.push(employee);
    }

    removeEmployee(employee) {
        const index = this._employees.indexOf(employee);
        if (index == -1) throw new RangeError();
        else this._employees.splice(index, 1);
    }

}

class Employee{
    constructor(name, salary) {
        this._name = name;
        this._salary = salary;
    }
}

let hr = new Department("HR");
hr.addEmployee(new Employee("Ahmed Salem", 1000));
hr.addEmployee(new Employee("Saleh Ali", 2000));

let newEmployee = new Employee("Jaber Maher", 300);
hr.addEmployee(newEmployee);
hr.addEmployee(new Employee("Rashed Saleh", 800));

console.log(hr.employees);
console.log(hr.employees.filter((employee) => {
    return employee._salary < 1000;
}));