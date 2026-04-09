const url = "https://app.reqres.in/api/users/2000";

class UserNotFoundException extends Error{
    constructor(message) {
        super(message);
        this.name = 404;
    }
}

fetch(url)
  .then((response) => {
    if (response.status == 404) {
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
