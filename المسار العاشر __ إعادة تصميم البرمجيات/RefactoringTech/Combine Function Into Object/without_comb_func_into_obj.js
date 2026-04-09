apiConfig = {
    apiUrl: "http://example.com/api",
    apiKey: '123456abcd',
};

function setupConnection(apiUrl, apiKey, userId, sessionToken) {
    console.log(`Setting up connection to ${apiUrl} with API key ${apiKey}, for user ${userId} with session ${sessionToken}`);
}

function fetchData(userId, sessionToken) {
    setupConnection(apiConfig.apiUrl, apiConfig.apiKey, userId, sessionToken);
    console.log(`Fetching data for user ${userId} with session ${sessionToken}`);
}

function processData(userId, sessionToken, data) {
    setupConnection(apiConfig.apiUrl, apiConfig.apiKey, userId, sessionToken);
    console.log(`Processing data ${data} for user ${userId} with session ${sessionToken}`);
}

function saveData(userId, sessionToken, data) {
    setupConnection(apiConfig.apiUrl, apiConfig.apiKey, userId, sessionToken);
    console.log(`Saving data ${data} for user ${userId} with session ${sessionToken}`);
}