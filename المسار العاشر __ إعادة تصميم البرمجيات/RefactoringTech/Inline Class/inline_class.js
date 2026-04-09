class Shipment{
    constructor() {
        this._trakingInformation = new TrackingInformation();
    }

    get shippingCompany() {
        return this._shippingCompany;
    }

    get trackingNumber() {
        return this._trackingNumber;
    }
    set trackingNumber(arg) {
        this._trackingNumber = arg;
    }

    get trackingInfo() {
        return `${this.shippingCompany}: ${this.trackingNumber}`;
    }

    get trackingInformation() {
        return this._trakingInformation;
    }

    set trackingInformation(aTrackingInformation) {
        this._trakingInformation = aTrackingInformation;
    }

    set shippingCompany(arg) {
        this._trackingCompany.shippingCompany = arg;
    }
}

request = { 'vendor': 123 }
aShipment = new Shipment();
// aShipment.trackingInformation.shippingCompany = request.vendor;
aShipment.shippingCompany = request.vendor;