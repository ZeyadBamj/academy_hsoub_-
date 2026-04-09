class TrackingInformation{
    get shippingCompany() {
        return this._shippingCompany;
    }

    set shippingCompany(arg) {
        this._shippingCompany = arg;
    }

    get trackingNumber() {
        return this._trackingNumber;
    }
    set trackingNumber(arg) {
        this._trackingNumber = arg;
    }

    get display() {
        return `${this.shippingCompany}: ${this.trackingNumber}`;
    }
}

class Shipment{
    constructor() {
        this._trakingInformation = new TrackingInformation();
    }

    get trackingInfo() {
        return this._trakingInformation.display;
    }

    get trackingInformation() {
        return this._trakingInformation;
    }

    set trackingInformation(aTrackingInformation) {
        this._trakingInformation = aTrackingInformation;
    }
}