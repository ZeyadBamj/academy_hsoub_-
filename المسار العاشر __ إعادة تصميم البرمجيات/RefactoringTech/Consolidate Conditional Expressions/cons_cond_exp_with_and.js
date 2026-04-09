let employee = {
  seniority: 10,
  monthsDisabled: 8,
  isPartTime: false,
  onVacation: true,
};

function disabilityAmount(employee) {
    if (employee.onVacation) {
        if (employee.seniority > 10) {
            return 1;
        }
        return 0.5
    }
}

function disabilityAmountWithAnd(employee) {
    if (employee.onVacation && employee.seniority > 10) {
        return 1;
    }
    return 0.5
}

console.log(disabilityAmount(employee))
console.log(disabilityAmountWithAnd(employee))