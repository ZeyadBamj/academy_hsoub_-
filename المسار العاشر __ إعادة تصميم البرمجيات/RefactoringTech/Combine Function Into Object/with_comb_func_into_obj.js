class apiClient{
    constructor(config, userId, sessionToken) {
        this.apiUrl = config.apiUrl;
        this.apiKey = config.apiKey;
        this.userId = userId;
        this.sessionToken = sessionToken;
        this.setupConnection();
    }

    setupConnection() {
    console.log(`Setting up connection to ${this.apiUrl} with API key ${this.apiKey}, for user ${this.userId} with session ${this.sessionToken}`);
    }
    
    fetchData() {
    console.log(`Fetching data for user ${this.userId} with session ${this.sessionToken}`);
}

processData(data) {
    console.log(`Processing data ${data} for user ${this.userId} with session ${this.sessionToken}`);
}

saveData(data) {
    console.log(`Saving data ${data} for user ${this.userId} with session ${this.sessionToken}`);
}
}

apiConfig = {
    apiUrl: "http://example.com/api",
    apiKey: '123456abcd',
};

let apiClient1 = new apiClient(apiConfig, 1, "09876543abc");
apiClient1.fetchData();
apiClient1.processData({ name: "Ahmed Ali", age: "25" });
apiClient1.saveData({ name: "Ahmed Ali", age: "25" });