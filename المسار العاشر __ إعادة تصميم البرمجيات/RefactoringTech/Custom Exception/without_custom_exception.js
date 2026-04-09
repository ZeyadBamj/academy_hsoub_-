const url = "https://regres.in/api/users/2000";

fetch(url)
  .then((response) => {
    if (response.status == 404) {
      throw new Error("User not Found");
    }
    return response.json();
  })
  .then((userData) => {
    console.log("User Data:", userData);
  })
  .catch((error) => {
    console.log("Error:", error);
  });
