// second step is creating this file for test acquire_data.js file 
const acquire_data = require('./acquire_data');

test('returns offices in India', () => {
    // Arrange
    const data = `office, country, telephone
Bangalore, India, +91 80 4064 9570
Chennai, India, +91 44 660 44766`;
    
    // Act and Assert which is .toContainEqual
    expect(acquire_data(data)).toContainEqual({
        "city": "Bangalore", "phone": "+91 80 4064 9570"
    });
});