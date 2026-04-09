class TelephoneNumber {
  constructor(areaCode, number) {
    this._areaCode = areaCode;
    this._number = number;
  }

  get areaCode() {
    return this._areaCode;
  }
  set areaCode(arg) {
    this._areaCode = arg;
  }

  get number() {
    return this._number;
  }
  set number(arg) {
    this._number = arg;
  }

   toString () {
    return `(${this._areaCode}) ${this._number}`;
  }
}

class Person {
  constructor(name) {
    this._name = name;
    this._telephoneNumber = new TelephoneNumber("123", "456789");
  }

  get name() {
    return this._name;
  }
  set name(arg) {
    this._name = arg;
  }

  get telephoneNumber() {
    return this._telephoneNumber.toString();
  }

  get officeAreaCode() {
    return this._telephoneNumber.areaCode;
  }
  set officeAreaCode(arg) {
    this._telephoneNumber.areaCode = arg;
  }

  get officeNumber() {
    return this._telephoneNumber.number;
  }
  set officeNumber(arg) {
    this._telephoneNumber.number = arg;
  }
}

let person1 = new Person("Ali Saleh");
console.log(person1.telephoneNumber);