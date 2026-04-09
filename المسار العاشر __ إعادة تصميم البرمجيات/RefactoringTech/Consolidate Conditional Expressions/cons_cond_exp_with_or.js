let employee = {
  seniority: 10,
  monthsDisabled: 8,
  isPartTime: false,
  onVacation: true,
};

// function disabilityAmount(employee) {
//   if (employee.seniority < 0) return 0;
//   if (employee.monthsDisabled > 12) return 0;
//   if (employee.isPartTime) return 0;

//   return 150;
// }

function disabilityAmount(employee) {
    if (isNotEligibleForDisability(employee)) return 0;
    return 150;
}

function isNotEligibleForDisability(employee) {
  return (
    employee.seniority < 0 ||
    employee.monthsDisabled > 12 ||
    employee.isPartTime
  );
}

console.log(disabilityAmount(employee));
