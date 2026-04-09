let invoice = {
  customer: "Salem Ahmed",
  orders: [
    { id: 1, amount: 300 },
    { id: 2, amount: 400 },
    { id: 3, amount: 600 },
  ],
  dueDate: Date.now(),
};

function printOwing(invoice) {
  printBanner();
  const outstanding = calculateOutstanding(invoice);
  recordDueDate();
  printDetails(invoice, outstanding);
}

function printBanner() {
  console.log("==========");
  console.log("===== Customer Owes =====");
  console.log("==========");
}

function printDetails(invoice, outstanding) {
  console.log(`name: ${invoice.customer}`);
  console.log(`amount: ${outstanding}`);
  console.log(`due: ${invoice.dueDate.toLocaleDateString()}`);
}

function calculateOutstanding(invoice) {
  let outstanding = 0;
  for (const o of invoice.orders) {
    outstanding += o.amount;
    }
    return outstanding
}

function recordDueDate() {
  let date = new Date(Date.now());
  invoice.dueDate = new Date(
    date.getFullYear(),
    date.getMonth(),
    date.getDate() + 30,
  );
}

printOwing(invoice);
