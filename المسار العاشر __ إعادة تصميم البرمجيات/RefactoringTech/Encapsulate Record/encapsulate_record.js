// Step 1: Encapsulate Variable

// const organization = {
//     name: "Hsoub Academy",
//     country: "UAE"
// };

// function getRowDataOfOrganization() {
//     return organization;
// }

// console.log(`<h1>${getRowDataOfOrganization().name}</h1>`);

// organization.name = 'Mostan1';

// console.log(`<h1>${getRowDataOfOrganization().name}</h1>`);


// Step 2: Replace Dictionary to Class

// class Organization{
//     constructor(data) {
//         this._data = data
//     }
// }

// const organization = new Organization({
//     name: "Hsoub Academy",
//     country: "UAE",
// });

// function getRowDataOfOrganization() {
//     return organization._data;
// }

// function getOrganization() {
//     return organization;
// }

// console.log(`<h1>${getRowDataOfOrganization().name}</h1>`);

// organization.name = 'Mostan1';

// console.log(`<h1>${getRowDataOfOrganization().name}</h1>`);


// Step 3: Use Setter and Getter and Delete the first Function
// class Organization{
//     constructor(data) {
//         this._data = data
//     }

//     get name() {
//         return this._data.name;
//     }
//     set name(string) {
//         this._data.name = string
//     }
// }

// const organization = new Organization({
//     name: "Hsoub Academy",
//     country: "UAE",
// });

// function getOrganization() {
//     return organization;
// }

// console.log(`<h1>${getOrganization().name}</h1>`);

// getOrganization().name = 'Mostan1';

// console.log(`<h1>${getOrganization().name}</h1>`);


// Step 4
class Organization{
    constructor(data) {
        this._name = data.name;
        this._country = data.country;
    }

    get name() {
        return this._name;
    }
    set name(string) {
        this._name = string
    }

    get country() {
        return this._country;
    }
    set country(countryCode) {
        this._country = countryCode
    }
}

const organization = new Organization({
    name: "Hsoub Academy",
    country: "UAE",
});

function getOrganization() {
    return organization;
}

console.log(`<h1>${getOrganization().name}</h1>`);

getOrganization().name = 'Mostan1';

console.log(`<h1>${getOrganization().name}</h1>`);

console.log(organization.name)