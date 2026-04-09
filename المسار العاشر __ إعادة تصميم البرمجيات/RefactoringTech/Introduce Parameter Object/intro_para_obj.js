const station = {
    name: '201',
    readings: [
        { temp: 19, time: "2026-4-1 12:00"},
        { temp: 21, time: "2026-5-1 13:00"},
        { temp: 22, time: "2026-6-1 14:00"},
        { temp: 27, time: "2026-7-1 15:00"},
        { temp: 28, time: "2026-8-1 16:00"},
        { temp: 29, time: "2026-8-1 16:00"},
    ],
};

class NumberRange{
    constructor(min, max) {
        this._data = {min: min, max: max}
    }

    get min() {
        return this._data.min;
    }

    get max() {
        return this._data.max;
    }
}

function readingsOutsideRange(station, range) {
    return station.readings.filter((r) => r.temp < range.min || r.temp > range.max
        
    );
}

const operatingPlan = {
    tempratureFloor: 20,
    tempratureCeiling: 28,
};

const range = new NumberRange(
    operatingPlan.tempratureFloor,
    operatingPlan.tempratureCeiling
)

let alerts = readingsOutsideRange(
    station,
    range
);
console.log(alerts);
// function readingsOutsideRange(station, min, max) {
//     return station.readings.filter((r) => r.temp < min || r.temp > max
        
//     );
// }

// const operatingPlan = {
//     tempratureFloor: 20,
//     tempratureCeiling: 24,
// };
