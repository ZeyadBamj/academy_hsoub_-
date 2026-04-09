const url = "https://app.reqres.in/api/users/2000";

const HTTPStatusCode = Object.freeze({
    OK: 200,
    CREATED: 201,
    BAD_REQUEST: 400,
    NOT_FOUND: 404,
    SERVER_ERROR: 500,
});

class UserNotFoundException extends Error{
    constructor(message) {
        super(message);
        this.name = HTTPStatusCode.NOT_FOUND;
    }
}

fetch(url)
  .then((response) => {
    if (response.status == HTTPStatusCode.NOT_FOUND) {
      throw new UserNotFoundException("User not Found");
    }
    return response.json();
  })
  .then((userData) => {
    console.log("User Data:", userData);
  })
  .catch((error) => {
    console.log("Error:", error);
  });
